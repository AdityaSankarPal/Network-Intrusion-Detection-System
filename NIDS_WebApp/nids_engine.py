"""
================================================================================
NIDS CORE ML INFERENCE ENGINE (nids_engine.py)
Production pipeline wrapper for Network Intrusion Detection
================================================================================
"""

import os
import joblib
import numpy as np
import pandas as pd

class NIDSEngine:
    def __init__(self, model_path="network_intrusion_model.joblib"):
        """Loads the trained model pipeline and schema artifacts."""
        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"[ERROR] Model artifact '{model_path}' not found!\n"
                "Please make sure you have saved 'network_intrusion_model.joblib' in this directory."
            )
        
        self.artifacts = joblib.load(model_path)
        self.model = self.artifacts['model']
        self.scaler = self.artifacts['scaler']
        self.feature_columns = self.artifacts['feature_columns']
        self.categorical_cols = self.artifacts['categorical_cols']
        self.label_map = self.artifacts.get('label_map', {0: 'normal', 1: 'anomaly'})

    def preprocess_input(self, raw_df: pd.DataFrame) -> np.ndarray:
        """
        Converts raw network packet dataframe into aligned, scaled 116-dimensional matrix.
        """
        df = raw_df.copy()
        
        # Drop target column if present
        if 'class' in df.columns:
            df = df.drop('class', axis=1)
            
        # One-hot encode categorical features
        present_cats = [col for col in self.categorical_cols if col in df.columns]
        df_encoded = pd.get_dummies(df, columns=present_cats, drop_first=True)
        
        # Align with the exact 116 training features
        df_aligned = df_encoded.reindex(columns=self.feature_columns, fill_value=0)
        df_aligned.columns = df_aligned.columns.astype(str)
        
        # Standard scale
        scaled_matrix = self.scaler.transform(df_aligned)
        return scaled_matrix

    def analyze_traffic(self, raw_df: pd.DataFrame) -> pd.DataFrame:
        """
        Runs full inference on raw network traffic and returns enriched security audit table.
        """
        if raw_df.empty:
            return pd.DataFrame()
            
        scaled_features = self.preprocess_input(raw_df)
        
        # Predictions
        raw_preds = self.model.predict(scaled_features)
        raw_probs = self.model.predict_proba(scaled_features)[:, 1] # Probability of Anomaly
        
        results_df = raw_df.copy().reset_index(drop=True)
        results_df['prediction'] = [self.label_map[p].upper() for p in raw_preds]
        results_df['anomaly_score'] = np.round(raw_probs * 100, 2)
        
        # Categorize Threat Severity
        def assign_severity(row):
            if row['prediction'] == 'NORMAL':
                return 'SAFE'
            score = row['anomaly_score']
            if score >= 90.0:
                return 'CRITICAL'
            elif score >= 70.0:
                return 'HIGH'
            elif score >= 50.0:
                return 'MEDIUM'
            else:
                return 'LOW'
                
        results_df['threat_level'] = results_df.apply(assign_severity, axis=1)
        results_df['action_required'] = results_df['threat_level'].map({
            'SAFE': 'Allow Traffic',
            'LOW': 'Log & Monitor',
            'MEDIUM': 'Rate Limit Host',
            'HIGH': 'Quarantine IP',
            'CRITICAL': 'BLOCK INSTANTLY (DROP PACKET)'
        })
        
        return results_df