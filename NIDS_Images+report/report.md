# **PROJECT TITLE** 

_(This page will have the project title and the project group members)_ 

**_Group Members:_** 

**NAME, COLLEGE NAME, UNIVERSITY REGISTRATION NUMBER NAME, COLLEGE NAME, UNIVERSITY REGISTRATION NUMBER NAME, COLLEGE NAME, UNIVERSITY REGISTRATION NUMBER NAME, COLLEGE NAME, UNIVERSITY REGISTRATION NUMBER NAME, COLLEGE NAME, UNIVERSITY REGISTRATION NUMBER** 

## **Table of Contents** 

- **Acknowledgement** 

- **Project Objective** 

- **Project Scope** 

- **Data Description** 

- **Model Building** 

- **Code** 

- **Future Scope of Improvements** 

- **Project Certificate** 

## **Acknowledgement** 

I take this opportunity to express my profound gratitude and deep regards to my faculty (Dr. Arnab Chakraborty / Mentor / Faculty Name) for his exemplary guidance, monitoring, and constant encouragement throughout the course of this project. The blessing, help and guidance given by him/her time to time shall carry me a long way in the journey of life on which I am about to embark. 

I am obliged to my project team members for the valuable information provided by them in their respective fields. I am grateful for their cooperation during the period of my assignment. 

_(All Group Member Names)_ 

## **Project Objective** 

####  Problem Description:
Modern computer networks handle massive volumes of data traffic every second. This expansion creates significant exposure to cyber threats such as Denial of Service (DoS) attacks, unauthorized network probing, and remote system exploitation. Manually inspecting millions of network packets is computationally impossible and prone to human oversight. Security Operations Centers (SOCs) require automated, intelligent systems that can rapidly distinguish benign operations from malicious intrusions in real time.

#### Project Objective:
The objective of this research project is to build an automated binary classification machine learning pipeline that accurately predicts whether a given network connection record is Normal traffic or an Anomaly (intrusion).

#### Plan of Action (How to Solve):
1. Data Exploration & Understanding: Audit dataset shape, feature types, missing values, duplicates, skewness, and target distribution.
2. Data Preprocessing: Clean dataset duplicates, apply One-Hot Encoding to categorical variables, standardize continuous features using StandardScaler, and partition data into stratified training and validation sets.
3. Model Benchmark & Training: Train and evaluate six distinct machine learning algorithms:
- K-Nearest Neighbors (KNN)
- Naive Bayes (GaussianNB)
- Random Forest Classifier
- Logistic Regression
- XGBoost Classifier
- Simple Neural Network (Multi-Layer Perceptron - MLP)
#### Model Selection & Final Inference: 
Select the top-performing model based on validation metrics (Accuracy, F1-Score, ROC-AUC), retrain it on the full training dataset, and generate threat predictions on unlabeled test instances (Test.csv).

## **Project Scope** 

#### In-Scope Boundary Conditions:
- Tabular Packet Telemetry Processing: Processing offline tabular network telemetry consisting of 41 raw attributes (connection duration, protocol type, service, TCP flags, byte counts, error rates).
- Binary Classification: Classifying network records strictly into two categories: Normal (0) vs Anomaly (1).
- Algorithm Benchmarking: Comparing linear models, instance-based classifiers, tree ensembles, and neural networks on an 80/20 stratified validation split.
- Output Generation: Generating an exported .csv file (test_predictions.csv) containing predicted binary labels and probability scores for 22,487 test connection records.
---
#### Out-of-Scope Boundary Conditions:
- Live Network Sniffing: Real-time hardware packet capturing (e.g., live Wireshark/PCAP network streaming) is out of scope for this phase.
- Multi-Class Attack Profiling: Sub-categorizing anomalies into specific attack vectors (e.g., DoS vs. Probe vs. Buffer Overflow) is excluded.
- Graphical Dashboard Deployment: Web-based GUI integration (e.g., Streamlit/Flask app) is reserved for future implementation.
----

## **Data Description** 

#### Data Source:
## Dataset Overview & Dimensions

- **Training Dataset (`Train.csv`):** 25,192 records and 42 columns (41 feature predictors + 1 target variable `class`).
- **Test Dataset (`Test.csv`):** 22,544 records and 41 columns (features only; target class is absent as expected).
- Data Description: The given train dataset has 25192 rows and 42 columns
| # | Column Name | dtype | Type | Target / Attribute | Description |
|---|---|---|---|---|---|
| 0 | `duration` | int64 | Non-categorical | Attribute | Duration of the connection in seconds |
| 1 | `protocol_type` | object | Categorical | Attribute | Type of protocol used (e.g., tcp, udp, icmp) |
| 2 | `service` | object | Categorical | Attribute | Destination network service used (e.g., http, ftp, smtp) |
| 3 | `flag` | object | Categorical | Attribute | Status of the connection (e.g., SF, S0, REJ) |
| 4 | `src_bytes` | int64 | Non-categorical | Attribute | Number of data bytes sent from source to destination |
| 5 | `dst_bytes` | int64 | Non-categorical | Attribute | Number of data bytes sent from destination to source |
| 6 | `land` | int64 | Categorical | Attribute | 1 if connection is from/to the same host/port; 0 otherwise |
| 7 | `wrong_fragment` | int64 | Non-categorical | Attribute | Number of wrong fragments in the connection |
| 8 | `urgent` | int64 | Non-categorical | Attribute | Number of urgent packets in the connection |
| 9 | `hot` | int64 | Non-categorical | Attribute | Number of "hot" indicators (e.g., accessing system directories) |
| 10 | `num_failed_logins` | int64 | Non-categorical | Attribute | Number of failed login attempts |
| 11 | `logged_in` | int64 | Categorical | Attribute | 1 if successfully logged in; 0 otherwise |
| 12 | `num_compromised` | int64 | Non-categorical | Attribute | Number of compromised conditions |
| 13 | `root_shell` | int64 | Categorical | Attribute | 1 if root shell is obtained; 0 otherwise |
| 14 | `su_attempted` | int64 | Categorical | Attribute | 1 if `su root` command attempted; 0 otherwise |
| 15 | `num_root` | int64 | Non-categorical | Attribute | Number of accesses to root directory |
| 16 | `num_file_creations` | int64 | Non-categorical | Attribute | Number of file creation operations |
| 17 | `num_shells` | int64 | Non-categorical | Attribute | Number of shell prompts |
| 18 | `num_access_files` | int64 | Non-categorical | Attribute | Number of operations on access control files |
| 19 | `num_outbound_cmds` | int64 | Non-categorical | Attribute | Number of outbound commands in an FTP session |
| 20 | `is_host_login` | int64 | Categorical | Attribute | 1 if the login belongs to the "hot" list; 0 otherwise |
| 21 | `is_guest_login` | int64 | Categorical | Attribute | 1 if the login is a guest login; 0 otherwise |
| 22 | `count` | int64 | Non-categorical | Attribute | Number of connections to the same host in the past 2 seconds |
| 23 | `srv_count` | int64 | Non-categorical | Attribute | Number of connections to the same service in the past 2 seconds |
| 24 | `serror_rate` | float64 | Non-categorical | Attribute | % of connections with SYN errors among `count` |
| 25 | `srv_serror_rate` | float64 | Non-categorical | Attribute | % of connections with SYN errors among `srv_count` |
| 26 | `rerror_rate` | float64 | Non-categorical | Attribute | % of connections with REJ errors among `count` |
| 27 | `srv_rerror_rate` | float64 | Non-categorical | Attribute | % of connections with REJ errors among `srv_count` |
| 28 | `same_srv_rate` | float64 | Non-categorical | Attribute | % of connections to the same service among `count` |
| 29 | `diff_srv_rate` | float64 | Non-categorical | Attribute | % of connections to different services among `count` |
| 30 | `srv_diff_host_rate` | float64 | Non-categorical | Attribute | % of connections to different hosts among `srv_count` |
| 31 | `dst_host_count` | int64 | Non-categorical | Attribute | Number of connections to the same destination host (past 100) |
| 32 | `dst_host_srv_count` | int64 | Non-categorical | Attribute | Number of connections to the same host and service (past 100) |
| 33 | `dst_host_same_srv_rate` | float64 | Non-categorical | Attribute | % of same-service connections among `dst_host_count` |
| 34 | `dst_host_diff_srv_rate` | float64 | Non-categorical | Attribute | % of different-service connections among `dst_host_count` |
| 35 | `dst_host_same_src_port_rate` | float64 | Non-categorical | Attribute | % of same-source-port connections among `dst_host_srv_count` |
| 36 | `dst_host_srv_diff_host_rate` | float64 | Non-categorical | Attribute | % of different-host connections among `dst_host_srv_count` |
| 37 | `dst_host_serror_rate` | float64 | Non-categorical | Attribute | % of SYN errors among `dst_host_count` |
| 38 | `dst_host_srv_serror_rate` | float64 | Non-categorical | Attribute | % of SYN errors among `dst_host_srv_count` |
| 39 | `dst_host_rerror_rate` | float64 | Non-categorical | Attribute | % of REJ errors among `dst_host_count` |
| 40 | `dst_host_srv_rerror_rate` | float64 | Non-categorical | Attribute | % of REJ errors among `dst_host_srv_count` |
| 41 | `class` | object | Categorical | **Target** | Target label (e.g., normal, anomaly) |

---

### Summary above Table
#### Type(Categorical/Non-categorical)

| Type | Count | Columns |
|---|---|---|
| **Categorical** | **10** | `protocol_type`, `service`, `flag`, `land`, `logged_in`, `root_shell`, `su_attempted`, `is_host_login`, `is_guest_login`, `class` |
| **Non-categorical** | **32** | All remaining numerical columns (durations, bytes, counts, rates) |
#### Datetype

| dtype | Count | Columns |
|---|---|---|
| **int64** | 24 | `duration`, `src_bytes`, `dst_bytes`, `land`, `wrong_fragment`, `urgent`, `hot`, `num_failed_logins`, `logged_in`, `num_compromised`, `root_shell`, `su_attempted`, `num_root`, `num_file_creations`, `num_shells`, `num_access_files`, `num_outbound_cmds`, `is_host_login`, `is_guest_login`, `count`, `srv_count`, `dst_host_count`, `dst_host_srv_count` |
| **float64** | 14 | `serror_rate`, `srv_serror_rate`, `rerror_rate`, `srv_rerror_rate`, `same_srv_rate`, `diff_srv_rate`, `srv_diff_host_rate`, `dst_host_same_srv_rate`, `dst_host_diff_srv_rate`, `dst_host_same_src_port_rate`, `dst_host_srv_diff_host_rate`, `dst_host_serror_rate`, `dst_host_srv_serror_rate`, `dst_host_rerror_rate`, `dst_host_srv_rerror_rate` |
| **object (str)** | 4 | `protocol_type`, `service`, `flag`, `class` |

#### Target 
| Role | Count | Details |
|---|---|---|
| **Attribute (Features)** | **41** | All columns from `duration` to `dst_host_srv_rerror_rate` |
| **Target (Label)** | **1** | `class` |
---
### Train Dataset Statistics:
| Statistic | duration | src_bytes | dst_bytes | land | wrong_fragment | urgent | hot | num_failed_logins | logged_in | num_compromised | ... | dst_host_count | dst_host_srv_count | dst_host_same_srv_rate | dst_host_diff_srv_rate | dst_host_same_src_port_rate | dst_host_srv_diff_host_rate | dst_host_serror_rate | dst_host_srv_serror_rate | dst_host_rerror_rate | dst_host_srv_rerror_rate |
|-----------|----------|-----------|-----------|------|----------------|--------|-----|-------------------|-----------|-----------------|-----|----------------|--------------------|------------------------|------------------------|-----------------------------|-----------------------------|----------------------|--------------------------|----------------------|--------------------------|
| **count** | 25192.0 | 2.5192e+04 | 2.5192e+04 | 25192.0 | 25192.0 | 25192.0 | 25192.0 | 25192.0 | 25192.0 | 25192.0 | ... | 25192.0 | 25192.0 | 25192.0 | 25192.0 | 25192.0 | 25192.0 | 25192.0 | 25192.0 | 25192.0 | 25192.0 |
| **mean** | 305.0541 | 2.4331e+04 | 3.4918e+03 | 0.0001 | 0.0237 | 0.0000 | 0.1980 | 0.0012 | 0.3948 | 0.2279 | ... | 182.5321 | 115.0630 | 0.5167 | 0.0842 | 0.1436 | 0.0267 | 0.2851 | 0.2794 | 0.1172 | 0.1184 |
| **std** | 2686.5556 | 2.4108e+06 | 8.8831e+04 | 0.0089 | 0.2602 | 0.0063 | 2.1542 | 0.0454 | 0.4888 | 10.4174 | ... | 98.9939 | 110.6469 | 0.4539 | 0.1891 | 0.3106 | 0.1111 | 0.4459 | 0.4464 | 0.3063 | 0.3178 |
| **min** | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ... | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| **25%** | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ... | 84.0 | 10.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| **50%** | 0.0 | 44.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | ... | 255.0 | 61.0 | 0.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| **75%** | 0.0 | 279.0 | 530.25 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 | ... | 255.0 | 255.0 | 1.0 | 0.1 | 0.1 | 0.0 | 1.0 | 1.0 | 0.0 | 0.0 |
| **max** | 42862.0 | 3.8171e+08 | 5.1514e+06 | 1.0 | 3.0 | 1.0 | 77.0 | 4.0 | 1.0 | 884.0 | ... | 255.0 | 255.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
---

## Feature Characterization

- **Numerical Features (38 features):** Includes continuous rates (`serror_rate`, `dst_host_same_srv_rate`), connection counts (`count`, `srv_count`, `dst_host_count`), and traffic metrics (`duration`, `src_bytes`, `dst_bytes`).
- **Categorical Features (3 features):**
  - `protocol_type`: Network protocol used (e.g., tcp, udp, icmp).
  - `service`: Network service on destination (e.g., ftp_data, other, private, http, telnet).
  - `flag`: Connection status flag (e.g., SF, S0, REJ, RSTO).
- **Target Feature (1 feature):**
  - `class`: Binary target present in training data (`normal` vs `anomaly`).

---

## Key Findings & Insights

### A. Target Variable Distribution

- **normal:** 13,449 instances (53.39%)
- **anomaly:** 11,743 instances (46.61%)
![alt text](image-1.png)



---

### B. Data Quality & Integrity Audit

- **Missing Values:** 
![alt text](image-4.png)
0 missing values detected across all columns in both training and testing datasets. No imputation step is required.

- **Duplicate Records:**
![alt text](image-5.png)
  - **Train Set:** 0 duplicate rows.
  - **Test Set:** 57 duplicate rows identified. These should be removed during preprocessing to maintain testing integrity.
  

---

### C. Feature Distributions & Outliers

Key metrics such as `duration`, `src_bytes`, and `dst_bytes` exhibit **extreme right-skewness** and **extreme magnitude variance**:

- **`src_bytes`:** Ranges from 0 to 3.81 × 10⁸ bytes (75th percentile is only 279).
- **`dst_bytes`:** Ranges from 0 to 5.15 × 10⁶ bytes.
![alt text](image-3.png)

---

### D. Correlation & Multicollinearity

Strong positive correlations exist among error-rate features:

- `serror_rate`, `srv_serror_rate`, `dst_host_serror_rate`, `dst_host_srv_serror_rate` show high pairwise correlation (*r* > 0.90).
- `num_compromised`, `num_root`, and `root_shell` are heavily collinear.
![alt text](image-2.png)

# Pre-Preprocessing Data Description Report (Raw Data Audit)

---

## 1. Dataset Dimensions & Memory Usage

- **Training Set Shape:** 25,192 rows × 42 columns
- **Testing Set Shape:** 22,544 rows × 41 columns
- **Train Memory Usage:** ~8.48 MB
- **Test Memory Usage:** ~7.28 MB

---

## 2. Data Types Breakdown

| Data Type | Train Count | Test Count |
| :--- | :---: | :---: |
| **`int64`** | 23 | 23 |
| **`float64`** | 15 | 15 |
| **`str` (Object)** | 4 | 3 |

- **Categorical Columns (4):** `protocol_type`, `service`, `flag`, `class` *(target column absent in test set)*
- **Numerical Columns (38):** Continuous and discrete numeric features

---

## 3. Raw Categorical Feature Cardinality

| Feature | Train Unique Count | Test Unique Count | Sample Train Categories |
| :--- | :---: | :---: | :--- |
| **`protocol_type`** | 3 | 3 | `['icmp', 'tcp', 'udp']` |
| **`service`** | 66 | 64 | `['ftp_data', 'http', 'other', 'private', 'remote_job']...` |
| **`flag`** | 11 | 11 | `['REJ', 'RSTR', 'S0', 'SF', 'SH']...` |

---

## 4. Data Integrity Audit (Nulls & Duplicates)

- **Training Set Null Values:** 0 (0.00%)
- **Testing Set Null Values:** 0 (0.00%)
- **Training Set Duplicates:** 0 (0.00%)
- **Testing Set Duplicates:** 57 (0.25%) *(Identified for purge during preprocessing)*

---

## 5. Target Class Distribution (`class` Column in `Train.csv`)

| Target Class | Raw Count | Percentage (%) |
| :--- | :---: | :---: |
| **`normal`** | 13,449 | 53.39% |
| **`anomaly`** | 11,743 | 46.61% |

> **Insight:** Class Imbalance Ratio (Normal : Anomaly) = **1.15 : 1** *(Well-Balanced, no resampling/SMOTE required)*.

---

## 6. Sample Numerical Feature Distributions (Raw Data Ranges)

| Feature | Min | Mean | Std Dev | Median (50%) | Max | Skewness |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`duration`** | 0.0 | 305.054 | 2,686.556 | 0.0 | 42,862.0 | +11.533 |
| **`src_bytes`** | 0.0 | 24,330.628 | 2,410,805.402 | 44.0 | 381,709,090.0 | +157.559 |
| **`dst_bytes`** | 0.0 | 3,491.847 | 88,830.718 | 0.0 | 5,151,385.0 | +54.778 |
| **`wrong_fragment`** | 0.0 | 0.024 | 0.260 | 0.0 | 3.0 | +11.184 |
| **`count`** | 1.0 | 84.591 | 114.673 | 14.0 | 511.0 | +1.504 |
| **`same_srv_rate`** | 0.0 | 0.661 | 0.440 | 1.0 | 1.0 | -0.570 |

> **Key Finding:** Extreme right-skewness observed in traffic metrics (`src_bytes`, `dst_bytes`, `duration`) highlights the critical necessity for standardized scaling (`StandardScaler`) prior to model training.
## **DATA PREPROCESSING** 
### A. Data Cleaning & Deduplication

- **Action:** Identified and eliminated duplicate samples present in `Test.csv`.
![alt text](image-7.png)
- **Result:** Test instances reduced from 22,544 to 22,487 records (57 duplicates purged). Train dataset remained intact at 25,192 records.

---

### B. Target Variable Encoding

- **Action:** Encoded the categorical binary target attribute (`class`) into integer format.
![alt text](image-11.png)
- **Mapping:**
  - `normal` → **0** (13,449 instances)
  - `anomaly` → **1** (11,743 instances)

---

### C. Categorical Feature Encoding & Alignment

- **Action:** Converted multi-class nominal features (`protocol_type`, `service`, `flag`) using One-Hot Encoding with `drop_first=True` to avoid the dummy variable trap.

 ![alt text](image-8.png)

- **Result:** Total feature dimension expanded from 41 raw attributes to **116** processed feature columns.
- **Verification:** Column structural alignment between training and test features was verified using strict assertion checking (116 × 116 matching column vectors).

---

### D. Stratified Dataset Splitting

- **Action:** Partitioned the full training set into dedicated sub-training and validation subsets using an **80/20** ratio.
![alt text](image-9.png)
- **Stratification:** Class ratios were preserved across both splits to mirror the true baseline distribution (~53.39% Normal vs ~46.61% Anomaly).
![alt text](image-12.png)
- **Final Subsets:**
  - `X_train`: 20,153 samples, 116 features
  - `X_val`: 5,039 samples, 116 features
  - `X_test`: 22,487 samples, 116 features

---

### E. Feature Standardization (Scaling)

- **Action:** Applied `StandardScaler` to ensure zero mean (μ = 0) and unit variance (σ = 1) across all predictor columns.
![alt text](image-10.png)
- **Data Leakage Mitigation:** The scaler was fitted strictly on `X_train` and subsequently used to transform `X_val` and `X_test`.
- **Validation:** Sample feature statistics after transformation confirmed exact standardized metrics: Mean = 0.0, Standard Deviation = 1.0.

# Post-Preprocessing Dataset Summary Dashboard

Following feature engineering, categorical encoding, deduplication, stratified splitting, and standardization, the dataset integrity was verified across four key dimensions. The **Post-Preprocessing Dataset Summary Dashboard** provides empirical validation that data leakage was prevented, class distributions were preserved, and feature scaling was applied accurately.

---

## 1. Dashboard Overview 

![alt text](image-22.png)

---

## 2. Panel-by-Panel Technical Breakdown

### Panel 1: Dataset Partition Row Counts
- **`X_train_scaled`**: **20,153 records** ($80\%$ of training set)
- **`X_val_scaled`**: **5,039 records** ($20\%$ of training set)
- **`X_test_scaled`**: **22,487 records** (Deduplicated test set; 57 duplicate rows purged from raw 22,544 count)
- **Feature Dimension**: **116 columns** across all three partitions following one-hot encoding (`drop_first=True`).

---

### Panel 2: Target Class Balance Across Splits (%)
To prevent class ratio distortion during data splitting, stratified sampling was applied. The validation split mirrors the training class distribution down to sub-decimal precision:

| Partition | Normal Traffic (Class 0) | Anomaly / Intrusion (Class 1) | Total Samples |
| :--- | :---: | :---: | :---: |
| **Train Set** | 10,759 (53.39%) | 9,394 (46.61%) | 20,153 |
| **Validation Set** | 2,690 (53.38%) | 2,349 (46.62%) | 5,039 |
| **Delta ($\Delta$)** | **-0.01%** | **+0.01%** | **Exact Stratification** |

> **Audit Result:** Zero class imbalance bias was introduced during partition creation.

---

### Panel 3: Distribution of Post-Scaling Feature Means ($\mu = 0$)
- **Mathematical Target:** $\mu_j = 0, \quad \forall j \in \{1, 2, \dots, 116\}$
- **Observed Distribution:** Centered tightly at $0.0$, with floating-point residual values operating at the magnitude scale of $10^{-16}$ (e.g., $-1.5 \times 10^{-16}$ to $+0.8 \times 10^{-16}$).
- **Validation:** Confirms successful subtraction of the sample mean ($\bar{x}$) during `StandardScaler.transform()`.

---

### Panel 4: Distribution of Post-Scaling Feature Standard Deviations ($\sigma = 1$)
- **Mathematical Target:** $\sigma_j = 1.0, \quad \forall j \in \{1, 2, \dots, 116\}$
- **Observed Distribution:** A strong, dominant spike at exactly $1.0$ across active variance predictors.
- **Validation:** Confirms division by sample standard deviation ($s$) was correctly computed on `X_train` and propagated without leakage to validation and test vectors. *(Note: Low-variance or constant zero-padded dummy columns sit near $0.0$).*

---

## 3. Data Integrity & Verification Summary Table

| Quality Audit Metric | Raw State | Post-Preprocessing State |
| :--- | :--- | :--- |
| **Test Set Duplicate Rows** | 57 duplicate instances | 0 duplicate instances (22,487 records remaining) |
| **Missing Values (NaN / Null)** | 0 missing values | 0 missing values across all 116 columns |
| **Categorical Variable Types** | 3 string objects (`protocol`, `service`, `flag`) | 116 binary numeric indicator vectors |
| **Train / Test Vector Alignment** | Mismatched categories | Strictly matched $116 \times 116$ column space |
| **Scaler Fit Constraint** | Unscaled | Fitted **strictly** on `X_train` (Zero Data Leakage) |
---


# Model Building
# Model Building & In-Depth Algorithm Analysis

In this project, we trained and evaluated **six different machine learning algorithms** to detect network intrusions. We intentionally selected models from different machine learning families—instance-based learning, probabilistic learning, ensemble learning, linear classification, gradient boosting, and neural networks—so we could compare which technique performs best for cybersecurity data.

Below is a complete breakdown of each algorithm, explaining what it is, how it works internally (with mathematical formulas and diagrams), where it shines, and most importantly, *why* we chose to include it in this network intrusion detection project.

---

## 🧭 1. K-Nearest Neighbors (KNN)

### **What is KNN?**

K-Nearest Neighbors is one of the simplest yet most intuitive machine learning algorithms. It is called a **"lazy learner"** because it doesn't actually learn an explicit function during training. Instead, it memorizes the entire training dataset and makes decisions *only* when a new data point arrives.

### Detailed Parameter Breakdown

| Parameter | Value Used | Default | Deep Explanation |
| :--- | :--- | :--- | :--- |
| **`n_neighbors` (K)** | `5` | `5` | Determines how many surrounding training points vote on the class of a new network packet. |
| **`weights`** | `'uniform'` | `'uniform'` | All 5 voters have equal influence. |
| **`metric`** | `'minkowski'` | `'minkowski'` | Mathematical formula for measuring distance between two points. |
| **`p`** | `2` | `2` | Power parameter inside Minkowski → with $p=2$, this becomes the Euclidean distance formula. |
| **`algorithm`** | `'auto'` | `'auto'` | Scikit-learn automatically chooses the fastest search method (Ball Tree, KD Tree, or Brute Force). |


### **How does it work? (Step by Step)**

1. **Store Training Data:** KNN memorizes all 20,153 training records along with their class labels (Normal or Anomaly).
2. **New Record Arrives:** When a new connection is observed, KNN calculates the distance between this new record and every single training record across all 116 features.
3. **Pick k Nearest:** It selects the $k$ closest training records (we used $k = 5$).
4. **Majority Vote:** The new record is assigned the class that appears most frequently among those 5 neighbors.

### ** The Core Formula (Euclidean Distance):**

To determine "closeness," KNN uses Euclidean distance between two points $x$ and $y$ in n-dimensional space:

$$
d(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}
$$

For our 116-feature dataset, this means calculating the square root of the sum of squared differences between 116 pairs of values.

### **Visual Diagram of KNN Classification:**
![alt text](image-13.png)

### **Why KNN was used here?**

Network connections of the same category naturally form geometric clusters in feature space. Normal HTTP traffic tends to "look similar" to other normal HTTP traffic, while attack patterns (like DoS flood packets) share similar byte spikes and flag patterns. KNN tests whether this simple geometric similarity is enough to flag intrusions.

Because KNN is entirely distance-dependent, our Step 2 Feature Scaling (`StandardScaler`) was essential—otherwise, large features like `src_bytes` (max 381M) would dominate smaller features like `count` (max 511).

### **Advantages & Disadvantages:**

|  Advantages |  Disadvantages |
| :--- | :--- |
| Simple and intuitive | Slow prediction on large datasets |
| No training phase | Memory-intensive (stores entire dataset) |
| Works well with clustered data | Highly sensitive to feature scaling |

---

##  2. Naive Bayes (GaussianNB)

### **What is Naive Bayes?**

Naive Bayes is a **probabilistic classifier** built on **Bayes' Theorem**. It calculates the probability that a given network connection is Normal or an Anomaly based on observed feature values. It is called "naive" because it makes one very strong assumption: *all features are independent of each other.*

### ** Core Formula: Bayes' Theorem:**

$$
P(C \mid X) = \frac{P(X \mid C) \cdot P(C)}{P(X)}
$$

Where:

- $P(C \mid X)$ = Probability that the connection belongs to class $C$ (Normal/Anomaly) given features $X$
- $P(X \mid C)$ = Likelihood of seeing features $X$ given class $C$
- $P(C)$ = Prior probability of class $C$ in training data
- $P(X)$ = Overall probability of features $X$ (acts as a normalizer)

Because our features are continuous (byte counts, rates, durations), Gaussian Naive Bayes assumes each feature follows a Gaussian (normal) distribution:

$$
P(x_i \mid C) = \frac{1}{\sqrt{2\pi\sigma_C^2}} \exp\left( -\frac{(x_i - \mu_C)^2}{2\sigma_C^2} \right)
$$

### **Visual Diagram of Naive Bayes:**

![alt text](image-14.png)
### Detailed Parameter Breakdown

| Parameter | Value Used | Default | Deep Explanation |
| :--- | :--- | :--- | :--- |
| **`priors`** | `None` | `None` | The prior probability $P(Y)$ of each class. |
| **`var_smoothing`** | `1e-9` | `1e-9` | A small positive constant added to the variance of all features to stabilize calculations. |

### Why Minimal Hyperparameters?

Naive Bayes is **non-parametric in configuration** — it directly calculates mean $\mu$ and standard deviation $\sigma$ from the data. There is nothing to "tune" because the mathematics are deterministic.

### Why `var_smoothing = 1e-9`?

Consider the Gaussian Probability Density Formula:

$$P(x_j | Y=c) = \frac{1}{\sqrt{2\pi\sigma_{c,j}^2}} \exp\left(-\frac{(x_j - \mu_{c,j})^2}{2\sigma_{c,j}^2}\right)$$

If any feature in the training data has a variance of **zero** (e.g., a constant value), the denominator $\sigma^2$ becomes 0 → **Division by Zero Error**. Adding $10^{-9}$ to the variance prevents this catastrophe without affecting the probability distribution meaningfully.

### Why Priors Were Left as None

By leaving priors empty, scikit-learn automatically calculates:

$$P(Y=\text{Normal}) = \frac{10{,}759}{20{,}153} = 0.5338$$

$$P(Y=\text{Anomaly}) = \frac{9{,}394}{20{,}153} = 0.4662$$

### **Why Naive Bayes was used here?**

We included Naive Bayes as a lightweight probabilistic baseline. Its training time is almost instantaneous (just 0.06 seconds), making it attractive for real-time systems. However, as we expected, it underperformed significantly on this dataset.

### ** Why it failed (71.48% Accuracy & 39% Recall):**

In network traffic, features are heavily correlated. For example, `serror_rate`, `srv_serror_rate`, `dst_host_serror_rate`, and `dst_host_srv_serror_rate` all spike together during a SYN flood attack. Naive Bayes' independence assumption is deeply violated here, leading it to misestimate class probabilities and miss over 60% of attacks.

---

##  3. Random Forest Classifier

### **What is Random Forest?**

Random Forest is an **ensemble learning** method built on the principle that *"a group of weak learners together is stronger than one strong learner."* It constructs a "forest" of many independent decision trees and combines their votes through majority voting.

### **How does it work? (Step by Step)**

1. **Bootstrap Sampling:** Create 100 random subsets of training data (with replacement).
2. **Build Trees:** For each subset, grow a decision tree using Gini Impurity as the splitting criterion.
3. **Feature Randomization:** At each tree node, consider only a random subset of features to split on (this decorrelates trees).
4. **Majority Voting:** When a new record arrives, all 100 trees cast a vote — the majority class wins.

### ** Core Formula: Gini Impurity:**

$$
\text{Gini}(S) = 1 - \sum_{i=1}^{C} p_i^2
$$

Where $p_i$ is the proportion of samples belonging to class $i$ at a node. Lower Gini means a purer node.

### **Visual Diagram of Random Forest:**

![alt text](image-15.png)
### Detailed Parameter Breakdown

| Parameter | Value Used | Default | Deep Explanation |
| :--- | :--- | :--- | :--- |
| **`n_estimators`** | `100` | `100` | Number of decision trees built in parallel. |
| **`criterion`** | `'gini'` | `'gini'` | The mathematical function for measuring the quality of a split at each node. |
| **`max_depth`** | `None` | `None` | Trees grow until all leaves are pure or contain less than `min_samples_split` samples. |
| **`min_samples_split`** | `2` | `2` | Minimum number of samples required to split an internal node. |
| **`min_samples_leaf`** | `1` | `1` | Minimum samples required in a leaf (terminal) node. |
| **`max_features`** | `'sqrt'` | `'sqrt'` | At each split, only $\sqrt{116} \approx 10$ features are evaluated. |
| **`bootstrap`** | `True` | `True` | Each tree uses a random sample with replacement from the training data. |
| **`random_state`** | `42` | `None` | Seeds the random generator for reproducible results. |

### Why n_estimators = 100

- **10 Trees:** Not enough diversity — single bad trees could skew the vote.
- **1000 Trees:** Marginal accuracy gain but 10× slower.
- **100 Trees (Chosen):** Sweet spot. Delivers 99.66% accuracy in just 0.94 seconds.

The error rate of a Random Forest decreases exponentially with more trees but plateaus around 100–200 for most tabular datasets.

### Why Gini Impurity Over Entropy

Both measure node purity, but Gini is faster because it avoids logarithm calculations:

$$\text{Gini}(t) = 1 - \sum_{k=0}^{1} p_k^2$$

Versus Entropy:

$$H(t) = -\sum_{k=0}^{1} p_k \log_2(p_k)$$

For 20,153 training samples × 100 trees × multiple splits, that logarithm computation adds up significantly.

### Why max_features = sqrt(116)

This is the secret weapon of Random Forest. Instead of letting every tree see all 116 features (which would make all trees identical), each split randomly considers only ~10 features. This forces **diversity** among trees, ensuring they make uncorrelated errors that cancel out during voting.

### Why random_state = 42

Without fixing the random seed, the bootstrap sampling and feature selection would produce different trees every run, causing accuracy to fluctuate ±0.3%. Setting `random_state=42` guarantees your mentor can reproduce your exact 99.66% result.

---

### **Why Random Forest was used here?**

Network intrusion detection often involves nested, conditional rules. For example:

IF protocol is TCP AND flag is REJ AND src_bytes = 0, THEN the connection is likely a probe scan attack.

Random Forest excels at discovering such hierarchical patterns. It is extremely robust to outliers, handles mixed feature types naturally, and doesn't require tuning to perform well. In our evaluation, it delivered an outstanding **99.66% accuracy** with the highest precision (**99.87%**) of all models.

---

##  4. Logistic Regression

### **What is Logistic Regression?**

Despite its misleading name, Logistic Regression is actually a **binary classification algorithm**. It estimates the probability that a given input belongs to a specific class using a linear combination of features transformed by the sigmoid (logistic) function.

### ** Core Formulas:**

**Linear Combination of Features:**

$$
z = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_n x_n
$$

**Sigmoid Activation (Converts z → probability between 0 and 1):**

$$
P(y=1 \mid X) = \sigma(z) = \frac{1}{1 + e^{-z}}
$$

**Classification Rule:**

- If $P(y=1 \mid X) \geq 0.5$ → Predict **Anomaly**
- If $P(y=1 \mid X) < 0.5$ → Predict **Normal**

### **Visual Diagram of the Sigmoid Decision:**

![alt text](image-17.png)
### Detailed Parameter Breakdown

| Parameter | Value Used | Default | Deep Explanation |
| :--- | :--- | :--- | :--- |
| **`max_iter`** | `1000` | `100` | Maximum iterations the solver attempts to converge to the optimal weights. |
| **`penalty`** | `'l2'` | `'l2'` | Regularization type to prevent weights from growing too large. |
| **`C`** | `1.0` | `1.0` | Inverse of regularization strength (smaller values = stronger regularization). |
| **`solver`** | `'lbfgs'` | `'lbfgs'` | Mathematical optimization algorithm (Limited-memory BFGS). |
| **`random_state`** | `42` | `None` | Seeds the solver for reproducibility. |
| **`tol`** | `1e-4` | `1e-4` | Tolerance for stopping criterion (model stops when improvement is below this value). |

### Why max_iter = 1000 (Critical Adjustment)

The scikit-learn default of `max_iter=100` was **insufficient** for our dataset. Here's why:

Logistic Regression uses **Gradient Descent** to minimize the Log Loss function:

$$L = -\frac{1}{N}\sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1-y_i) \log(1-\hat{y}_i) \right]$$

With 116 features (dimensions), the optimizer must navigate a 116-dimensional space to find the global minimum. 100 iterations caused this warning:

```
ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.
```

Increasing to 1000 gave the solver enough iterative steps to reach the true optimum, boosting accuracy from ~95% to **97.30%**.

### Why L2 Regularization

L2 adds the squared sum of weights to the loss function:

$$L_{\text{regularized}} = L + \frac{1}{2C}\sum_{j=1}^{116} w_j^2$$

This penalizes large weight values, preventing any single feature (like `src_bytes` which has huge raw values) from dominating the model. It smooths out the decision boundary and improves generalization.

### Why solver = lbfgs

The LBFGS (Limited-memory Broyden-Fletcher-Goldfarb-Shanno) algorithm:

- Works excellently for small-to-medium datasets (< 100K samples ✓).
- Supports L2 regularization natively.
- Converges faster than standard Gradient Descent by approximating the inverse Hessian matrix.

---

### **Why Logistic Regression was used here?**

We needed a solid **linear baseline** to answer a fundamental question: *"Can network intrusions be separated using a simple linear boundary, or do we need complex non-linear models?"*

Logistic Regression is highly interpretable—we can examine which features (e.g., `service_http`, `src_bytes`) have the strongest positive or negative weight coefficients for predicting attacks. It achieved a strong **97.30% accuracy**, confirming that many intrusions have clear linear signatures but complex attacks still require non-linear models.

### **Key Parameters we used:**

- `max_iter=1000` — Ensured full solver convergence
- `penalty='l2'` — L2 Ridge regularization to prevent overfitting

---

## 🚀 5. XGBoost (Extreme Gradient Boosting) — *Our Winning Model*

### **What is XGBoost?**

XGBoost is a cutting-edge, highly optimized implementation of **Gradient Boosting Decision Trees (GBDT)**. Unlike Random Forest (which builds trees independently), XGBoost builds trees **sequentially**, where each new tree is specifically designed to correct the errors of the previous trees.

### **How does it work? (Step by Step)**

1. Start with a weak initial prediction (e.g., average log-odds).
2. Calculate residuals (how wrong the prediction is for each record).
3. Build a new decision tree to predict these residuals.
4. Add this tree's output (scaled by a learning rate) to the previous prediction.
5. Repeat for 100 iterations, each time becoming more accurate.

### ** Core Mathematical Formula:**

**Objective Function to Minimize:**

$$
\text{Obj} = \sum_{i=1}^{n} L(y_i, \hat{y}_i) + \sum_{k=1}^{K} \Omega(f_k)
$$

Where:

- $L(y_i, \hat{y}_i)$ = **Loss function** (we used LogLoss for binary classification)
- $\Omega(f_k)$ = **Regularization term** to penalize overly complex trees

**Binary Cross-Entropy Loss (LogLoss):**

$$
L = -\frac{1}{n} \sum_{i=1}^{n} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]
$$

### **Visual Diagram of Gradient Boosting:**

![alt text](image-18.png)
### Detailed Parameter Breakdown

| Parameter | Value Used | Default | Deep Explanation |
| :--- | :--- | :--- | :--- |
| **`eval_metric`** | `'logloss'` | *None* | Metric for evaluating model performance during training. |
| **`n_estimators`** | `100` | `100` | Number of sequential boosting rounds (trees added). |
| **`max_depth`** | `6` | `6` | Maximum depth of each tree. |
| **`learning_rate` (η)** | `0.3` | `0.3` | Shrinkage factor applied to each new tree's contribution. |
| **`gamma`** | `0` | `0` | Minimum loss reduction required to make a split (regularization). |
| **`subsample`** | `1.0` | `1.0` | Fraction of training samples randomly selected for each tree. |
| **`colsample_bytree`** | `1.0` | `1.0` | Fraction of features randomly selected per tree. |
| **`reg_alpha`** | `0` | `0` | L1 regularization on weights. |
| **`reg_lambda`** | `1` | `1` | L2 regularization on weights. |
| **`random_state`** | `42` | `None` | Seeds the random generator. |

### Why eval_metric = logloss (Explicitly Set)

Without this parameter, XGBoost prints the warning:

```
UserWarning: eval_metric is not specified. Default will be used.
```

Setting `logloss` explicitly aligns the evaluation with our binary classification objective:

$$\text{LogLoss} = -\frac{1}{N}\sum_{i=1}^{N} \left[ y_i \log(p_i) + (1-y_i) \log(1-p_i) \right]$$

This metric heavily penalizes **confident wrong predictions** (e.g., predicting 99% Normal when actually Anomaly), which is critical for intrusion detection where false negatives are dangerous.

### Why Learning Rate (η) = 0.3

Each new tree updates the ensemble prediction via:

$$F_m(x) = F_{m-1}(x) + \eta \cdot h_m(x)$$

- **η = 1.0:** Each tree makes aggressive corrections. Fast training but prone to overfitting.
- **η = 0.01:** Tiny updates. Very robust but requires 3000+ trees to achieve similar accuracy.
- **η = 0.3 (Default):** Balanced. 100 trees are sufficient to achieve excellent performance.

### Why max_depth = 6

Tree depth controls the complexity of interactions the model can capture:

- **Depth 1:** Only considers one feature per path (too simple).
- **Depth 15:** Can model very complex feature interactions but overfits.
- **Depth 6:** Can capture 6-feature interactions (e.g., "if service=http AND src_bytes>1000 AND flag=SF AND wrong_fragment=0 AND count>50 AND same_srv_rate<0.3 → Anomaly").

### **Why XGBoost was selected as the Final Model?**

XGBoost is widely considered the gold-standard algorithm for structured/tabular datasets. In data science competitions (like Kaggle), it dominates leaderboards for classification problems. In our project, it delivered:

- **99.70% Validation Accuracy** (Highest)
- **99.68% F1-Score** (Highest)
- **Perfect 1.0000 ROC-AUC** (Flawless class separation)
- **Blazing fast 0.55-second training time**

It elegantly handles correlated features, outliers, and non-linear feature interactions—all of which are commonplace in network traffic data.

---

## 6. Simple Neural Network (Multi-Layer Perceptron - MLP)

### **What is a Neural Network?**

A Multi-Layer Perceptron (MLP) is a type of **feedforward artificial neural network** inspired by the human brain. It consists of layers of interconnected artificial neurons that pass signals forward through weighted connections, eventually producing a classification decision.

### **How does it work? (Step by Step)**

1. **Input Layer:** Receives all 116 scaled features.
2. **Hidden Layers:** Apply weighted sums + activation functions to extract patterns.
3. **Output Layer:** Produces a probability between 0 and 1.
4. **Backpropagation:** Compares prediction to actual label, calculates error, and adjusts neuron weights.
5. **Epoch Repetition:** Repeats this process over 300 epochs until weights stabilize.

### ** Core Mathematical Formulas:**

**Weighted Sum at a Neuron:**

$$
z = \sum_{i=1}^{n} w_i x_i + b
$$

**ReLU Activation (For Hidden Layers):**

$$
f(z) = \max(0, z)
$$

**Sigmoid Activation (For Output Layer):**

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

### **Visual Diagram of our MLP Architecture:**

![alt text](image-19.png)

### Detailed Parameter Breakdown

| Parameter | Value Used | Default | Deep Explanation |
| :--- | :--- | :--- | :--- |
| **`hidden_layer_sizes`** | `(64, 32)` | `(100,)` | Tuple defining the number of neurons in each hidden layer. |
| **`max_iter`** | `300` | `200` | Maximum number of training epochs (full passes through data). |
| **`activation`** | `'relu'` | `'relu'` | Non-linear activation function applied in hidden layers. |
| **`solver`** | `'adam'` | `'adam'` | Weight optimization algorithm. |
| **`alpha`** | `0.0001` | `0.0001` | L2 regularization strength. |
| **`batch_size`** | `'auto'` | `'auto'` | Mini-batch size (default = min(200, n_samples)). |
| **`learning_rate_init`** | `0.001` | `0.001` | Initial step size for weight updates. |
| **`random_state`** | `42` | `None` | Seeds initial weight assignments. |
| **`tol`** | `1e-4` | `1e-4` | Loss improvement threshold for early stopping. |

### Why Architecture (64, 32) — "Funnel Design"

Our network architecture:

```
Input Layer (116 neurons) → Hidden 1 (64) → Hidden 2 (32) → Output (1)
```

This is a **compression funnel** that progressively distills features:

- **Layer 1 (116 → 64):** Compresses raw features into higher-level patterns (like "ICMP flood signatures").
- **Layer 2 (64 → 32):** Combines these patterns into attack categories (DoS, Probe, R2L).
- **Output (32 → 1):** Final binary probability (Normal vs Anomaly).

### Why max_iter = 300

MLPClassifier's default (200 epochs) was insufficient — the model stopped improving but hadn't fully converged, leaving ~0.5% accuracy on the table. Increasing to 300 allowed the Adam optimizer additional epochs to fine-tune weights without overfitting.

### Why ReLU Activation

ReLU (Rectified Linear Unit) is defined as:

$$\text{ReLU}(z) = \max(0, z)$$

Advantages over older activations like sigmoid/tanh:

- **No Vanishing Gradient:** Gradient is exactly 1 for positive inputs, enabling deep networks to train faster.
- **Computational Efficiency:** Just a `max()` operation, far faster than calculating $e^x$.
- **Sparsity:** Negative values become 0, making the network more efficient.

### Why Adam Optimizer

Adam (Adaptive Moment Estimation) combines two powerful ideas:

1. **Momentum:** Accelerates updates in consistent directions.
2. **RMSProp:** Adapts learning rate per parameter based on recent gradient magnitudes.

The update rule involves bias-corrected first moment $\hat{m}_t$ and second moment $\hat{v}_t$:

$$w_t = w_{t-1} - \eta \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$

Adam works remarkably well across diverse problems without needing manual learning rate tuning — perfect for our 116-feature dataset.

### **Why the Neural Network was used here?**

We wanted to test whether a **deep learning approach** could beat traditional ML algorithms on tabular network data. Neural networks are famous for their ability to automatically learn complex hierarchical representations of input features.

Our MLP achieved an excellent **99.44% accuracy**, confirming it successfully learned the attack patterns. However, it took **11.94 seconds** to train (nearly 20× slower than XGBoost) and offered no accuracy advantage—making it less practical for real-time security operations where millisecond latency is critical.

---
# SECTION 4: COMPARISON OF THE MODELS TRAINED

## 4.1 Overview and Evaluation Metrics

Evaluating machine learning models for Network Intrusion Detection Systems (NIDS) requires balancing raw classification accuracy with domain-specific security constraints. In a real-world security operations center (SOC), **False Negatives** (misclassifying a malicious attack as normal traffic) can result in undetected system breaches, data exfiltration, or ransomware deployment. Conversely, **False Positives** (misclassifying legitimate user traffic as an anomaly) lead to severe alert fatigue for security analysts.

To provide a rigorous, multi-dimensional assessment, six distinct machine learning algorithms—ranging from simple linear classifiers to deep neural networks and gradient-boosted ensembles—were trained on the preprocessed training set ($20{,}153$ records) and evaluated on an independent validation set ($5{,}039$ records).

Each algorithm was evaluated using five core statistical metrics alongside computational execution time:

1. **Accuracy**: The overall percentage of correctly identified network connection instances across both normal and anomaly classes:

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

2. **Precision (Anomaly)**: The ratio of correctly identified network intrusions out of all instances flagged as anomalies. High precision minimizes false alarms:

$$\text{Precision} = \frac{TP}{TP + FP}$$

3. **Recall / Sensitivity (Anomaly)**: The ratio of correctly identified network intrusions out of all actual intrusion events present in the network traffic. High recall minimizes missed attacks:

$$\text{Recall} = \frac{TP}{TP + FN}$$

4. **F1-Score (Anomaly)**: The harmonic mean of Precision and Recall, serving as the single unified benchmark for overall anomaly detection quality:

$$\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

5. **ROC-AUC (Receiver Operating Characteristic - Area Under Curve)**: Evaluates the model's ability to discriminate between normal and malicious packets across all possible probability classification thresholds ($0.0$ to $1.0$).

---

## 4.2 Comparative Performance Summary

Table 4.1 provides a detailed quantitative comparison of all six trained models on the $5{,}039$-record validation dataset, ordered from highest to lowest by ROC-AUC score.

### Table 4.1: Empirical Model Evaluation & Performance Metrics Summary

| Rank | Model Name | Validation Accuracy | Precision (Anomaly) | Recall (Anomaly) | F1-Score (Anomaly) | ROC-AUC | Training Time (Seconds) | Model Complexity / Architecture |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **XGBoost (Extreme Gradient Boosting)** | **99.70%** | **99.79%** | **99.57%** | **99.68%** | **1.0000** | **0.55s** | Sequential Gradient Boosted Trees ($100$ Estimators) |
| **2** | **Random Forest Classifier** | **99.66%** | **99.87%** | **99.40%** | **99.64%** | **0.9999** | **0.94s** | Parallel Ensemble Trees ($100$ Estimators, Gini) |
| **3** | **Simple Neural Network (MLP)** | **99.44%** | **99.36%** | **99.45%** | **99.40%** | **0.9990** | **11.94s** | 4-Layer Feedforward ($116 \to 64 \to 32 \to 1$, ReLU) |
| **4** | **K-Nearest Neighbors (KNN)** | **99.27%** | **99.49%** | **98.94%** | **99.21%** | **0.9974** | **2.46s** | Instance-Based Memory ($K=5$, Euclidean Distance) |
| **5** | **Logistic Regression** | **97.30%** | **97.96%** | **96.21%** | **97.08%** | **0.9940** | **0.39s** | Linear Generalized Model ($L_2$ Penalty, $1000$ max_iter) |
| **6** | **Gaussian Naive Bayes** | **71.48%** | **99.46%** | **39.04%** | **56.07%** | **0.9796** | **0.06s** | Probabilistic Density Estimator ($\text{var\_smoothing}=10^{-9}$) |

---

## 4.3 Detailed Model-by-Model Analysis

![alt text](image-20.png)

### 1. XGBoost (Extreme Gradient Boosting) — *Top Performing Model*

- **Validation Performance**: **99.70% Accuracy**, **1.0000 ROC-AUC**, **99.68% F1-Score**.
- **Key Findings**: XGBoost outperformed all competing architectures across almost every evaluation metric. By iteratively fitting decision trees to the negative gradients (residuals) of preceding models, XGBoost effectively isolated subtle non-linear attack signatures across continuous network variables (`src_bytes`, `dst_bytes`, `count`) and discrete categorical flags (`service_http`, `service_ecr_i`).
- **Strengths**: Incorporates second-order Taylor expansion for objective optimization alongside explicit $L_1$ and $L_2$ regularization parameters (`reg_alpha`, `reg_lambda`), completely suppressing overfitting. Training completed in a fast **0.55 seconds**.

### 2. Random Forest Classifier — *Runner-Up Ensemble*

- **Validation Performance**: **99.66% Accuracy**, **0.9999 ROC-AUC**, **99.87% Precision**.
- **Key Findings**: Random Forest achieved the highest overall Precision score (**99.87%**), registering only $3$ false alarms out of $2{,}349$ validation predictions.
- **Strengths**: Utilizing Bootstrap Aggregation (Bagging) across $100$ parallel decision trees combined with random feature subspace sampling ($\sqrt{116} \approx 10$ features per split) produced an extremely robust model immune to variance fluctuations in network packet traffic.

### 3. Multi-Layer Perceptron (MLP Neural Network) — *Deep Learning Baseline*

- **Validation Performance**: **99.44% Accuracy**, **0.9990 ROC-AUC**, **99.45% Recall**.
- **Key Findings**: The funnel architecture ($116 \to 64 \to 32 \to 1$) successfully learned dense, high-order non-linear feature representations using the Adam optimizer and ReLU activation functions.
- **Trade-Offs**: While achieving outstanding accuracy, training required **11.94 seconds**—over $21\times$ longer than XGBoost and $30\times$ longer than Logistic Regression. The lack of structural tree partitioning makes single-prediction decision trails uninterpretable compared to tree ensembles.

### 4. K-Nearest Neighbors (KNN, $K=5$) — *Instance-Based Classifier*

- **Validation Performance**: **99.27% Accuracy**, **0.9974 ROC-AUC**, **98.94% Recall**.
- **Key Findings**: Standardizing features via Z-score scaling ($Z = \frac{X - \mu}{\sigma}$) proved critical for KNN. Because distance calculations occur across $116$ orthogonal dimensions, standardized features prevented large-scale variables (`src_bytes`) from overwhelming normalized rate metrics (`same_srv_rate`).
- **Trade-Offs**: KNN requires storing the entire training set in memory ($O(N \cdot D)$ space complexity) and computing $20{,}153$ Euclidean distances per query packet during inference, creating scaling bottlenecks for real-time high-throughput backbones.

### 5. Logistic Regression — *Linear Baseline Model*

- **Validation Performance**: **97.30% Accuracy**, **0.9940 ROC-AUC**, **96.21% Recall**.
- **Key Findings**: Serving as a linear decision boundary baseline, Logistic Regression proved surprisingly effective, correctly identifying over $96\%$ of network anomalies.
- **Strengths & Limitations**: Extremely lightweight and fast (**0.39s training time**). However, because network intrusion patterns involve complex non-linear feature interactions (e.g., conditional dependencies between specific connection flags and port services), a single linear decision hyperplane $\mathbf{w}^T \mathbf{X} + b = 0$ is inherently capped in mathematical capacity compared to decision trees.

### 6. Gaussian Naive Bayes — *Diagnostic Failure Case Analysis*

- **Validation Performance**: **71.48% Accuracy**, **0.9796 ROC-AUC**, **39.04% Recall**.
- **Root Cause of Performance Drop**: Gaussian Naive Bayes exhibited a severe failure mode in Anomaly Recall (**39.04%**), missing over $60\%$ of active network intrusions in the validation set.
- **Mathematical Explanation**: Naive Bayes relies on the strict assumption of **Conditional Class Independence**:

$$P(X_1, X_2, \dots, X_{116} \mid Y) = \prod_{j=1}^{116} P(X_j \mid Y)$$

In network traffic data, this assumption is fundamentally violated. Rate metrics such as `serror_rate` (percentage of connections with SYN errors), `srv_serror_rate`, `rerror_rate`, and `same_srv_rate` are strongly multi-collinear. Naive Bayes repeatedly multiplied probabilities of correlated features, artificially over-inflating confidence scores and severely distorting the posterior probability boundary.

---

## 4.4 ROC Curves Comparison--Validation Set

The Receiver Operating Characteristic (ROC) curves for all six trained models are plotted below on the $5{,}039$-record validation set. Each curve illustrates the trade-off between the **True Positive Rate (Recall)** and the **False Positive Rate (1 − Specificity)** across all classification probability thresholds from $0.0$ to $1.0$.
![alt text](image-6.png)

### Interpretation

- The **diagonal dashed line** (AUC = 0.50) represents a random classifier with zero discriminative power.
- All six models significantly outperform the random baseline, confirming that the preprocessed 116-feature space contains strong predictive signal for intrusion detection.
- **XGBoost** achieves a mathematically perfect AUC of **1.0000**, meaning there exists at least one probability threshold at which the model simultaneously achieves 100% True Positive Rate and 0% False Positive Rate — flawless separation of normal and anomalous traffic.
- **Random Forest** (0.9999) and **MLP** (0.9990) hug the top-left corner almost identically, indicating negligible practical difference in ranking quality despite architectural differences.
- **Gaussian Naive Bayes** (0.9796), while still above the "excellent" threshold of 0.90, shows visible deviation from the top-left corner — consistent with its poor Recall of 39.04% caused by the violated independence assumption.
---

## 4.5 Production Model Selection Rationale

Based on the empirical findings documented in Table 4.1 and the visual evidence generated in the metric comparison charts (`roc_curves_comparison.png` and `model_comparison_bargraph.png`), **XGBoost (Extreme Gradient Boosting)** was selected as the final production algorithm for deployment.

### Summary of Selection Rationale:

- **Superior Accuracy & ROC-AUC**: Achieved the highest validation accuracy ($99.70\%$) and perfect ROC-AUC ($1.0000$).
- **Critical Attack Recall**: Successfully detected **$99.57\%$** of all malicious network intrusions, minimizing enterprise risk.
- **Low Alert Fatigue**: Delivered **$99.79\%$** Precision, preventing unnecessary administrative overhead for security teams.
- **Deployment Readiness**: The fully retrained XGBoost model artifact (`network_intrusion_model.joblib`) compiles into a compact binary format ($< 2 \text{ MB}$), enabling real-time deployment into live network firewall pipelines.
---
## Model Training Time Comparison

Computational efficiency during training is a critical metric for production Network Intrusion Detection Systems (NIDS), especially in dynamic environments where models must be frequently retrained on fresh network traffic logs.

The bar chart below summarizes the total wall-clock training time (in seconds) required by each algorithm on the preprocessed training set ($20{,}153$ records across $116$ features).

---

### Empirical Training Time Breakdown

| Rank | Model | Training Time (s) | Relative Speed Factor | Complexity Class |
| :---: | :--- | :---: | :---: | :--- |
| **1** | **Gaussian Naive Bayes** | **0.06s** | **1.0×** *(Baseline)* | $O(N \cdot D)$ — Closed-form statistics |
| **2** | **XGBoost** | **0.33s** | **5.5× slower** | $O(K \cdot D \cdot N \log N)$ — Parallel C++ gradient boosting |
| **3** | **Logistic Regression** | **0.37s** | **6.2× slower** | $O(I \cdot N \cdot D)$ — L-BFGS gradient descent ($1000$ max_iter) |
| **4** | **K-Nearest Neighbors (KNN)** | **0.44s** | **7.3× slower** | $O(N \cdot D)$ — Data indexing into memory |
| **5** | **Random Forest** | **0.91s** | **15.2× slower** | $O(K \cdot D \cdot N \log N)$ — $100$ full unpruned parallel trees |
| **6** | **MLP (Neural Network)** | **12.65s** | **210.8× slower** | $O(E \cdot N \cdot \sum L_i L_{i+1})$ — Backpropagation across 300 epochs |

---

### Visualization of Training Times

![alt text](image-21.png)

---

### Analytical Insights & Engineering Takeaways

1. **The Deep Learning Bottleneck (MLP at 12.65s):**
   - The Multi-Layer Perceptron was by far the slowest algorithm to train, taking **12.65 seconds** (over **38× longer than XGBoost**).
   - *Reason:* Neural networks require iterative forward passes, loss computation, and backpropagation of weight gradients across multiple epochs ($300$ max iterations) and hidden layers ($116 \to 64 \to 32 \to 1$). Despite this overhead, it yielded lower accuracy ($99.44\%$) than XGBoost ($99.70\%$).

2. **The XGBoost Efficiency Advantage (0.33s):**
   - XGBoost achieved a remarkably low training time of **0.33 seconds** while simultaneously delivering the highest accuracy ($99.70\%$) and ROC-AUC ($1.0000$).
   - *Reason:* XGBoost uses highly optimized C++ parallelization, histogram-based feature binning, and cache-aware memory access patterns, making it extremely fast even when growing $100$ sequential trees.

3. **Random Forest vs. XGBoost (0.91s vs 0.33s):**
   - Random Forest took nearly **3× longer to train (0.91s)** than XGBoost.
   - *Reason:* Random Forest grows unpruned trees until pure leaves are formed ($100\%$ depth), requiring significantly more split evaluations compared to XGBoost's depth-capped trees (`max_depth=6`).

4. **Lightweight Baselines (Naive Bayes & Logistic Regression):**
   - **Naive Bayes (0.06s)** is almost instantaneous because it performs a single pass over the data to calculate per-feature means ($\mu$) and variances ($\sigma^2$) without any iterative optimization.
   - **Logistic Regression (0.37s)** converges rapidly via the L-BFGS optimizer, making it an excellent lightweight linear baseline.

 **Final Assessment:** **XGBoost** provides the best efficiency-to-performance ratio in the benchmark, delivering top-tier detection capabilities with sub-second training convergence.
# 7. Test Dataset & Final Inference

### **Test Set Execution Strategy:**
The selected **XGBoost** model was retrained on 100% of the training dataset (25,192 instances) using full standardization. Inference was then executed on the 22,487 deduplicated test connection records.

### **Final Test Predictions Distribution:**
* **Total Test Connection Records Analyzed:** 22,487
* **Predicted Normal Traffic (`normal`):** **13,762 instances (61.20%)**
* **Predicted Anomalies / Intrusions (`anomaly`):** **8,725 instances (38.80%)**
* **Output Artifact:** Successfully exported to `test_predictions.csv` containing predicted class labels and threat probability scores.

| Category | Count | Ratio |
| :--- | :---: | :---: |
| **Normal Traffic (0)** | 13,762 | 61.20% |
| **Anomaly / Intrusion (1)** | 8,725 | 38.80% |

### **Top Cybersecurity Features Identified (XGBoost Feature Importance):**
1. **`service_ecr_i` (39.2% Importance):** ICMP echo request packets, commonly associated with Ping Flood DoS attacks.
2. **`service_http` (20.5% Importance):** Web traffic protocols; deviations flag HTTP exploit payloads.
3. **`src_bytes` (13.1% Importance):** Outbound data volume from source, indicating automated data exfiltration.
4. **`wrong_fragment` (6.1% Importance):** Fragmented packet count, pointing to Teardrop firewall bypass attacks.

---


## Test Dataset & Final Inference

### Test Set Execution Strategy

The selected XGBoost model was retrained on **100% of the training dataset** (25,192 instances) using full standardization. Inference was then executed on the **22,487** deduplicated test connection records.

---

### Final Test Predictions Distribution

- **Total Test Connection Records Analyzed:** 22,487
- **Predicted Normal Traffic (`normal`):** 13,762 instances (61.20%)
- **Predicted Anomalies / Intrusions (`anomaly`):** 8,725 instances (38.80%)
- **Output Artifact:** Successfully exported to `test_predictions.csv` containing predicted class labels and threat probability scores.

| Category                | Count  | Ratio  |
|-------------------------|--------|--------|
| Normal Traffic (0)      | 13,762 | 61.20% |
| Anomaly / Intrusion (1) | 8,725  | 38.80% |

---

### Top Cybersecurity Features Identified (XGBoost Feature Importance)

1. **`service_ecr_i`** (39.2% Importance): ICMP echo request packets, commonly associated with Ping Flood DoS attacks.
2. **`service_http`** (20.5% Importance): Web traffic protocols; deviations flag HTTP exploit payloads.
3. **`src_bytes`** (13.1% Importance): Outbound data volume from source, indicating automated data exfiltration.
4. **`wrong_fragment`** (6.1% Importance): Fragmented packet count, pointing to Teardrop firewall bypass attacks.

# Code:
![alt text](MLfinal_page-0001-1.jpg) ![alt text](MLfinal_page-0002-1.jpg) ![alt text](MLfinal_page-0003-1.jpg) ![alt text](MLfinal_page-0004-1.jpg) ![alt text](MLfinal_page-0005-1.jpg) ![alt text](MLfinal_page-0006-1.jpg) ![alt text](MLfinal_page-0007-1.jpg) ![alt text](MLfinal_page-0008-1.jpg) ![alt text](MLfinal_page-0009-1.jpg) ![alt text](MLfinal_page-0010-1.jpg) ![alt text](MLfinal_page-0011-1.jpg) ![alt text](MLfinal_page-0012-1.jpg) ![alt text](MLfinal_page-0013-1.jpg) ![alt text](MLfinal_page-0014-1.jpg) ![alt text](MLfinal_page-0015-1.jpg) ![alt text](MLfinal_page-0016-1.jpg) ![alt text](MLfinal_page-0017-1.jpg) ![alt text](MLfinal_page-0018-1.jpg) ![alt text](MLfinal_page-0019-1.jpg) ![alt text](MLfinal_page-0020-1.jpg) ![alt text](MLfinal_page-0021-1.jpg) ![alt text](MLfinal_page-0022-1.jpg) ![alt text](MLfinal_page-0023-1.jpg) ![alt text](MLfinal_page-0024-1.jpg) ![alt text](MLfinal_page-0025-1.jpg) ![alt text](MLfinal_page-0026-1.jpg) ![alt text](MLfinal_page-0027-1.jpg) ![alt text](MLfinal_page-0028-1.jpg) ![alt text](MLfinal_page-0029-1.jpg) ![alt text](MLfinal_page-0030-1.jpg) ![alt text](MLfinal_page-0031-1.jpg) ![alt text](MLfinal_page-0032-1.jpg) ![alt text](MLfinal_page-0033-1.jpg) ![alt text](MLfinal_page-0034-1.jpg) ![alt text](MLfinal_page-0035-1.jpg) ![alt text](MLfinal_page-0036-1.jpg) ![alt text](MLfinal_page-0037-1.jpg) ![alt text](MLfinal_page-0038-1.jpg) ![alt text](MLfinal_page-0039-1.jpg) ![alt text](MLfinal_page-0040-1.jpg) ![alt text](MLfinal_page-0041-1.jpg)![alt text](MLfinal_page-0042-1.jpg) 


## Future Scope of Improvements

* **Live Network Packet Capture (PCAP):** Extend the pipeline to capture real-time network traffic from live network interfaces using tools like Wireshark/PyShark.
* **Multi-Class Attack Profiling:** Expand the classification objective from binary detection (Normal vs Anomaly) to granular attack categorization (e.g., Denial of Service, Remote to Local, User to Root, Probing).
* **Web Security Dashboard:** Build an interactive web dashboard (using Streamlit or Flask) allowing Security Operations Center (SOC) analysts to view real-time threat maps, alert confidence scores, and connection distributions.
* **Automated SIEM Integration:** Integrate model outputs directly into enterprise Security Information and Event Management (SIEM) systems to trigger automatic firewall IP blocking when high-probability intrusions are detected.

