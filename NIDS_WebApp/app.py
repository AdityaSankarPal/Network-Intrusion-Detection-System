import time
import os
import textwrap
from datetime import datetime
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from nids_engine import NIDSEngine


# 1. PAGE SETUP

st.set_page_config(
    page_title="NIDS — AI Network Defense Console",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# 2. SAPPHIRE / MIDNIGHT BLUE DESIGN SYSTEM (CUSTOM CSS)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background-color: #060b14 !important;
    background-image: 
        radial-gradient(circle at 85% 15%, rgba(56, 189, 248, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 15% 85%, rgba(37, 99, 235, 0.10) 0%, transparent 40%),
        linear-gradient(180deg, #060b14 0%, #0a1224 50%, #04070e 100%) !important;
    color: #e2e8f0;
}

#MainMenu, header, footer {visibility: hidden;}

.brand-logo {
    display: flex;
    align-items: center;
    gap: 12px;
    font-weight: 800;
    font-size: 1.45rem;
    color: #ffffff;
    letter-spacing: -0.02em;
}

.brand-icon {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #38bdf8, #2563eb);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    font-size: 19px;
    box-shadow: 0 0 20px rgba(56, 189, 248, 0.35);
}

.pill-badge {
    background: rgba(56, 189, 248, 0.08);
    border: 1px solid rgba(56, 189, 248, 0.25);
    color: #7dd3fc;
    padding: 0.35rem 0.95rem;
    border-radius: 9999px;
    font-size: 0.8rem;
    font-weight: 500;
}

.eyebrow-tag {
    color: #38bdf8;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 1.2rem;
}

.hero-heading {
    font-size: 3.8rem;
    font-weight: 800;
    line-height: 1.08;
    color: #ffffff;
    letter-spacing: -0.03em;
    margin-bottom: 1.4rem;
}

.hero-heading span {
    color: #38bdf8;
}

.hero-subtitle {
    font-size: 1.05rem;
    line-height: 1.6;
    color: #94a3b8;
    max-width: 490px;
    margin-bottom: 2rem;
    font-weight: 400;
}

.stButton>button {
    background-color: #ffffff !important;
    color: #060b14 !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    padding: 0.6rem 1.4rem !important;
    border-radius: 9999px !important;
    border: none !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 2px 10px rgba(255, 255, 255, 0.12);
}
.stButton>button:hover {
    background-color: #bae6fd !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 16px rgba(56, 189, 248, 0.35);
}

.step-card {
    background: rgba(15, 26, 46, 0.65);
    border: 1px solid rgba(56, 189, 248, 0.15);
    border-radius: 20px;
    padding: 1.8rem;
    backdrop-filter: blur(12px);
    transition: all 0.3s ease;
    height: 100%;
}
.step-card:hover {
    border-color: rgba(56, 189, 248, 0.4);
    background: rgba(20, 35, 62, 0.8);
    transform: translateY(-3px);
}

.step-number {
    font-size: 0.85rem;
    color: #38bdf8;
    font-weight: 600;
    margin-bottom: 1rem;
}

.step-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 0.6rem;
}

.step-desc {
    font-size: 0.9rem;
    line-height: 1.55;
    color: #94a3b8;
}

.hero-graphic-card {
    background: radial-gradient(circle at 70% 30%, #172c4c 0%, #0d1a2f 60%, #08111e 100%);
    border: 1px solid rgba(56, 189, 248, 0.22);
    border-radius: 28px;
    padding: 2.5rem;
    position: relative;
    overflow: hidden;
    min-height: 380px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: flex-end;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.45);
}

.ai-badge {
    background: rgba(6, 11, 20, 0.7);
    border: 1px solid rgba(56, 189, 248, 0.35);
    color: #bae6fd;
    padding: 0.35rem 0.85rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    backdrop-filter: blur(8px);
    position: relative;
    z-index: 2;
}

.tool-box {
    background: rgba(15, 26, 46, 0.7);
    border: 1px solid rgba(56, 189, 248, 0.15);
    border-radius: 20px;
    padding: 1.8rem;
    margin-bottom: 1.5rem;
}

.terminal-box {
    background: rgba(6, 11, 20, 0.85);
    border-left: 3px solid #38bdf8;
    padding: 0.8rem 1.2rem;
    border-radius: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    color: #e2e8f0;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)


# 3. BACKEND ENGINE INITIALIZATION

@st.cache_resource
def get_engine():
    try:
        return NIDSEngine("network_intrusion_model.joblib")
    except Exception:
        return None

engine = get_engine()


# 4. SESSION STATE NAVIGATION (TOP PILL NAVBAR)

if 'current_tab' not in st.session_state:
    st.session_state.current_tab = "Home"

nav_col1, nav_col2, nav_col3 = st.columns([1.1, 3.4, 1.1])

with nav_col1:
    st.markdown("""<div class="brand-logo"><div class="brand-icon">🌐</div><div>NIDS</div></div>""", unsafe_allow_html=True)

with nav_col2:
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        if st.button("Home", use_container_width=True):
            st.session_state.current_tab = "Home"
            st.rerun()
    with c2:
        if st.button("Live Stream", use_container_width=True):
            st.session_state.current_tab = "Live Stream"
            st.rerun()
    with c3:
        if st.button("Batch Scanner", use_container_width=True):
            st.session_state.current_tab = "Batch Scanner"
            st.rerun()
    with c4:
        if st.button("Deep Forensics", use_container_width=True):
            st.session_state.current_tab = "Deep Forensics"
            st.rerun()
    with c5:
        if st.button("Specs & Telemetry", use_container_width=True):
            st.session_state.current_tab = "Specs & Telemetry"
            st.rerun()

with nav_col3:
    st.markdown("""<div style="text-align: right;"><span class="pill-badge">Secure network, better defense.</span></div>""", unsafe_allow_html=True)

st.markdown("<div style='margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True)


# TAB 1: HOME (LANDING HERO + NETWORK GRAPHIC)

if st.session_state.current_tab == "Home":
    hero_left, hero_right = st.columns([1.1, 0.9], gap="large")

    with hero_left:
        st.markdown('<div class="eyebrow-tag">SMART NETWORK DEFENSE • POWERED BY XGBOOST</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-heading">See what your<br><span>network is</span><br>saying.</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-subtitle">Upload raw connection logs or inspect real-time packet flows to get an instant, intelligent security health check for your infrastructure.</div>', unsafe_allow_html=True)

        if st.button("Start a network scan →"):
            st.session_state.current_tab = "Batch Scanner"
            st.rerun()

    with hero_right:
        # Fully unindented SVG block to prevent Markdown code-block interpretation
        hero_svg_html = (
            '<div class="hero-graphic-card">'
            '<svg viewBox="0 0 320 260" width="100%" height="100%" style="position: absolute; top: 10px; left: 10px; opacity: 0.95;">'
            '<circle cx="80" cy="150" r="55" fill="#38bdf8" fill-opacity="0.25" />'
            '<circle cx="230" cy="70" r="32" fill="#2563eb" fill-opacity="0.35" />'
            '<path d="M 60 140 Q 160 80 260 120" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6,4" fill="none" />'
            '<path d="M 80 210 Q 160 160 230 70" stroke="#60a5fa" stroke-width="3" stroke-linecap="round" fill="none" />'
            '<path d="M 120 70 Q 160 180 200 230" stroke="#1d4ed8" stroke-width="2" fill="none" />'
            '<circle cx="160" cy="140" r="14" fill="#38bdf8" />'
            '<circle cx="160" cy="140" r="22" stroke="#38bdf8" stroke-width="1.5" fill="none" />'
            '<circle cx="230" cy="70" r="10" fill="#60a5fa" />'
            '<circle cx="80" cy="210" r="8" fill="#93c5fd" />'
            '<circle cx="260" cy="120" r="9" fill="#38bdf8" />'
            '<circle cx="120" cy="115" r="4" fill="#ffffff" />'
            '<circle cx="200" cy="100" r="4" fill="#ffffff" />'
            '<circle cx="180" cy="180" r="3.5" fill="#ffffff" />'
            '</svg>'
            '<div class="ai-badge">AI-POWERED • 99.7% ACC</div>'
            '</div>'
        )
        st.markdown(hero_svg_html, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 3.5rem;'></div>", unsafe_allow_html=True)

    # 3-Step Information Grid (01 Intercept, 02 Analyze, 03 Protect)
    card1, card2, card3 = st.columns(3, gap="medium")

    with card1:
        st.markdown("""<div class="step-card"><div class="step-number">01</div><div class="step-title">Intercept</div><div class="step-desc">Feed unlabelled network logs or live socket connection payloads directly into the inspection pipeline.</div></div>""", unsafe_allow_html=True)

    with card2:
        st.markdown("""<div class="step-card"><div class="step-number">02</div><div class="step-title">Analyze</div><div class="step-desc">Our trained XGBoost model evaluates 116 high-dimensional statistical and protocol features in microseconds.</div></div>""", unsafe_allow_html=True)

    with card3:
        st.markdown("""<div class="step-card"><div class="step-number">03</div><div class="step-title">Protect</div><div class="step-desc">Execute immediate automated firewall rules—quarantine suspicious hosts and drop zero-day attack payloads.</div></div>""", unsafe_allow_html=True)


# TAB 2: LIVE STREAM (REAL-TIME SOCKET SIMULATOR)

elif st.session_state.current_tab == "Live Stream":
    st.markdown('<div class="eyebrow-tag">LIVE TELEMETRY MONITOR</div>', unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 2.2rem; font-weight: 800; color: #ffffff; margin-top: -10px;'>Real-Time Packet Radar</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; font-size: 1rem; margin-bottom: 1.5rem;'>Simulates incoming network packets on interface <code>eth0</code> and applies instant AI threat detection.</p>", unsafe_allow_html=True)

    if engine is None:
        st.error("Model file `network_intrusion_model.joblib` not found.")
    else:
        ctrl1, ctrl2, ctrl3 = st.columns([1.5, 1.5, 2])
        with ctrl1:
            stream_speed = st.slider("Streaming Rate (packets/sec)", 1, 10, 4)
        with ctrl2:
            packet_limit = st.number_input("Capture Buffer Limit", min_value=10, max_value=100, value=25)
        with ctrl3:
            st.write("")
            st.write("")
            start_btn = st.button("Start Live Capture", use_container_width=True)

        if start_btn:
            status_box = st.empty()
            chart_box = st.empty()
            table_box = st.empty()

            live_records = []
            chart_times = []
            chart_scores = []

            for i in range(packet_limit):
                is_anomaly = np.random.choice([0, 1], p=[0.70, 0.30])
                if is_anomaly:
                    pkt = {
                        'duration': np.random.choice([0, 1, 4]),
                        'protocol_type': np.random.choice(['tcp', 'icmp']),
                        'service': np.random.choice(['ecr_i', 'private', 'eco_i']),
                        'flag': np.random.choice(['S0', 'REJ', 'RSTO']),
                        'src_bytes': np.random.choice([0, 1032, 28, 512]),
                        'dst_bytes': 0,
                        'wrong_fragment': np.random.choice([0, 1, 3]),
                        'count': np.random.randint(120, 511),
                        'same_srv_rate': np.random.uniform(0.01, 0.15)
                    }
                else:
                    pkt = {
                        'duration': 0,
                        'protocol_type': np.random.choice(['tcp', 'udp']),
                        'service': np.random.choice(['http', 'domain_u', 'smtp']),
                        'flag': 'SF',
                        'src_bytes': np.random.randint(200, 3800),
                        'dst_bytes': np.random.randint(500, 10000),
                        'wrong_fragment': 0,
                        'count': np.random.randint(1, 20),
                        'same_srv_rate': 1.0
                    }

                res = engine.analyze_traffic(pd.DataFrame([pkt])).iloc[0]
                t_stamp = datetime.now().strftime("%H:%M:%S")

                chart_times.append(t_stamp)
                chart_scores.append(res['anomaly_score'])

                live_records.insert(0, {
                    "Time": t_stamp,
                    "Protocol": pkt['protocol_type'].upper(),
                    "Service": pkt['service'],
                    "Payload (Bytes)": f"{pkt['src_bytes']} in / {pkt['dst_bytes']} out",
                    "Verdict": res['prediction'],
                    "Anomaly Risk": f"{res['anomaly_score']:.1f}%",
                    "Severity": res['threat_level'],
                    "Firewall Action": res['action_required']
                })

                with status_box.container():
                    if res['prediction'] == 'ANOMALY':
                        st.markdown(f"""<div class="terminal-box" style="border-left-color: #ef4444; color: #fca5a5;">⚠️ <b>[ALERT] Threat Intercepted at {t_stamp}</b> | Protocol: <b>{pkt['protocol_type'].upper()} ({pkt['service']})</b> | Risk: <b>{res['anomaly_score']:.1f}%</b> | Action: <code>{res['action_required']}</code></div>""", unsafe_allow_html=True)
                    else:
                        st.markdown(f"""<div class="terminal-box"><b>[NORMAL] Packet #{i+1} at {t_stamp}</b> | {pkt['protocol_type'].upper()} • {pkt['service']} | Status: Verified Safe</div>""", unsafe_allow_html=True)

                fig_stream = go.Figure()
                fig_stream.add_trace(go.Scatter(
                    x=chart_times[-20:],
                    y=chart_scores[-20:],
                    mode='lines+markers',
                    line=dict(color='#38bdf8', width=2.5),
                    marker=dict(size=6, color='#93c5fd'),
                    fill='tozeroy',
                    fillcolor='rgba(56, 189, 248, 0.12)'
                ))
                fig_stream.add_hline(y=50, line_dash="dash", line_color="#ef4444", annotation_text="Threat Cutoff (50%)")
                fig_stream.update_layout(
                    title=dict(text="Real-Time Intrusion Risk Score (%)", font=dict(size=13, color="#94a3b8")),
                    paper_bgcolor='rgba(15, 26, 46, 0.7)',
                    plot_bgcolor='rgba(6, 11, 20, 0.8)',
                    font=dict(color='#cbd5e1', size=11),
                    margin=dict(l=30, r=20, t=40, b=20),
                    height=220,
                    yaxis=dict(range=[0, 105], gridcolor='rgba(56, 189, 248, 0.1)'),
                    xaxis=dict(gridcolor='rgba(56, 189, 248, 0.1)')
                )
                chart_box.plotly_chart(fig_stream, use_container_width=True)
                table_box.dataframe(pd.DataFrame(live_records[:8]), use_container_width=True)
                time.sleep(1.0 / stream_speed)


# TAB 3: BATCH SCANNER (CSV AUDITOR)

elif st.session_state.current_tab == "Batch Scanner":
    st.markdown('<div class="eyebrow-tag">BULK FILE AUDITING</div>', unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 2.2rem; font-weight: 800; color: #ffffff; margin-top: -10px;'>Log Traffic Health Check</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; font-size: 1rem; margin-bottom: 1.5rem;'>Upload connection telemetry files (<code>Test.csv</code>) to perform bulk automated threat detection.</p>", unsafe_allow_html=True)

    if engine is None:
        st.error("Model file `network_intrusion_model.joblib` not found.")
    else:
        st.markdown('<div class="tool-box">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload Traffic Log CSV", type=["csv"], label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

        if uploaded_file is not None:
            raw_data = pd.read_csv(uploaded_file)
            st.caption(f"Loaded `{uploaded_file.name}` containing **{len(raw_data):,}** connection records.")

            if st.button("Run Full Security Scan"):
                with st.spinner("Analyzing high-dimensional feature vectors..."):
                    t0 = time.time()
                    results = engine.analyze_traffic(raw_data)
                    elapsed = time.time() - t0

                st.success(f"Audit completed in **{elapsed:.2f}s** ({len(results)/elapsed:,.0f} connections/sec)")

                total_p = len(results)
                anom_p = len(results[results['prediction'] == 'ANOMALY'])
                crit_p = len(results[results['threat_level'] == 'CRITICAL'])
                safe_p = total_p - anom_p
                rate = (anom_p / total_p) * 100

                m1, m2, m3, m4 = st.columns(4)
                with m1:
                    st.markdown(f"""<div class="step-card"><div class="step-number">TOTAL SCANNED</div><div style="font-size: 1.8rem; font-weight: 800; color: #ffffff;">{total_p:,}</div><div class="step-desc">Flow records</div></div>""", unsafe_allow_html=True)
                with m2:
                    st.markdown(f"""<div class="step-card" style="border-color: rgba(239, 68, 68, 0.3);"><div class="step-number" style="color: #f87171;">INTRUSIONS</div><div style="font-size: 1.8rem; font-weight: 800; color: #f87171;">{anom_p:,}</div><div class="step-desc">{rate:.1f}% threat rate</div></div>""", unsafe_allow_html=True)
                with m3:
                    st.markdown(f"""<div class="step-card" style="border-color: rgba(245, 158, 11, 0.3);"><div class="step-number" style="color: #fbbf24;">CRITICAL</div><div style="font-size: 1.8rem; font-weight: 800; color: #fbbf24;">{crit_p:,}</div><div class="step-desc">Immediate drop</div></div>""", unsafe_allow_html=True)
                with m4:
                    st.markdown(f"""<div class="step-card"><div class="step-number">CLEAN</div><div style="font-size: 1.8rem; font-weight: 800; color: #38bdf8;">{safe_p:,}</div><div class="step-desc">Normal packets</div></div>""", unsafe_allow_html=True)

                st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

                c_left, c_right = st.columns(2)
                with c_left:
                    st.markdown("##### Threat Severity Breakdown")
                    sev_df = results['threat_level'].value_counts().reset_index()
                    sev_df.columns = ['Severity', 'Count']
                    fig_pie = px.pie(
                        sev_df, values='Count', names='Severity', hole=0.5,
                        color='Severity',
                        color_discrete_map={
                            'SAFE': '#38bdf8', 'LOW': '#60a5fa', 'MEDIUM': '#fbbf24',
                            'HIGH': '#f97316', 'CRITICAL': '#ef4444'
                        }
                    )
                    fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#cbd5e1'), height=240, margin=dict(l=10, r=10, t=10, b=10))
                    st.plotly_chart(fig_pie, use_container_width=True)

                with c_right:
                    st.markdown("##### Threat Count by Protocol")
                    if 'protocol_type' in results.columns:
                        proto_df = results.groupby(['protocol_type', 'prediction']).size().reset_index(name='Count')
                        fig_bar = px.bar(
                            proto_df, x='protocol_type', y='Count', color='prediction',
                            barmode='group',
                            color_discrete_map={'NORMAL': '#38bdf8', 'ANOMALY': '#ef4444'}
                        )
                        fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(6, 11, 20, 0.8)', font=dict(color='#cbd5e1'), height=240, margin=dict(l=10, r=10, t=10, b=10))
                        st.plotly_chart(fig_bar, use_container_width=True)

                st.markdown("##### Incident Telemetry Table")
                display_cols = [c for c in ['protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'prediction', 'anomaly_score', 'threat_level', 'action_required'] if c in results.columns]
                st.dataframe(results[display_cols].head(100), use_container_width=True)

                csv_file = results.to_csv(index=False).encode('utf-8')
                st.download_button("Download Security Incident Report (CSV)", data=csv_file, file_name="nids_threat_summary.csv", mime="text/csv")


# TAB 4: DEEP FORENSICS (SINGLE PACKET DIAGNOSTIC)

elif st.session_state.current_tab == "Deep Forensics":
    st.markdown('<div class="eyebrow-tag">MANUAL PACKET FORENSICS</div>', unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 2.2rem; font-weight: 800; color: #ffffff; margin-top: -10px;'>Single Connection Diagnostic</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; font-size: 1rem; margin-bottom: 1.5rem;'>Configure packet attributes to test how the model classifies rare or novel network payloads.</p>", unsafe_allow_html=True)

    st.markdown('<div class="tool-box">', unsafe_allow_html=True)
    fc1, fc2, fc3 = st.columns(3)

    with fc1:
        st.markdown("<span style='font-size: 0.85rem; font-weight: 600; color: #38bdf8;'>Protocol Specs</span>", unsafe_allow_html=True)
        in_proto = st.selectbox("Protocol Type", ['tcp', 'udp', 'icmp'])
        in_service = st.selectbox("Target Service", ['http', 'private', 'domain_u', 'smtp', 'ftp_data', 'eco_i', 'ecr_i', 'telnet'])
        in_flag = st.selectbox("Connection Flag", ['SF', 'S0', 'REJ', 'RSTO', 'RSTR'])

    with fc2:
        st.markdown("<span style='font-size: 0.85rem; font-weight: 600; color: #38bdf8;'>Payload & Size</span>", unsafe_allow_html=True)
        in_src = st.number_input("Source Bytes (Outbound)", min_value=0, max_value=10000000, value=215)
        in_dst = st.number_input("Destination Bytes (Inbound)", min_value=0, max_value=10000000, value=4500)
        in_duration = st.number_input("Duration (seconds)", min_value=0, max_value=50000, value=0)

    with fc3:
        st.markdown("<span style='font-size: 0.85rem; font-weight: 600; color: #38bdf8;'>Rate Metrics</span>", unsafe_allow_html=True)
        in_count = st.slider("SYN Count in 2s Window", 0, 511, 10)
        in_same_srv = st.slider("Same Service Rate", 0.0, 1.0, 1.0)
        in_wrong_frag = st.selectbox("Wrong Fragment Count", [0, 1, 3])

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Inspect Connection"):
        if engine is not None:
            input_df = pd.DataFrame([{
                'duration': in_duration,
                'protocol_type': in_proto,
                'service': in_service,
                'flag': in_flag,
                'src_bytes': in_src,
                'dst_bytes': in_dst,
                'wrong_fragment': in_wrong_frag,
                'count': in_count,
                'same_srv_rate': in_same_srv
            }])

            res = engine.analyze_traffic(input_df).iloc[0]
            r_col1, r_col2 = st.columns([1, 1], gap="medium")

            with r_col1:
                fig_g = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=res['anomaly_score'],
                    number={'suffix': "%", 'font': {'color': "#ffffff", 'size': 34}},
                    title={'text': "Calculated Risk Score", 'font': {'color': "#94a3b8", 'size': 13}},
                    gauge={
                        'axis': {'range': [0, 100], 'tickcolor': "#38bdf8"},
                        'bar': {'color': "#ef4444" if res['prediction'] == "ANOMALY" else "#38bdf8", 'thickness': 0.22},
                        'bgcolor': "rgba(15, 26, 46, 0.8)",
                        'steps': [
                            {'range': [0, 50], 'color': "rgba(56, 189, 248, 0.1)"},
                            {'range': [50, 75], 'color': "rgba(251, 191, 36, 0.1)"},
                            {'range': [75, 100], 'color': "rgba(239, 68, 68, 0.15)"}
                        ],
                        'threshold': {'line': {'color': "#ef4444", 'width': 3}, 'thickness': 0.8, 'value': 85}
                    }
                ))
                fig_g.update_layout(paper_bgcolor='rgba(0,0,0,0)', height=220, margin=dict(l=20, r=20, t=30, b=20))
                st.plotly_chart(fig_g, use_container_width=True)

            with r_col2:
                st.markdown(f"""<div class="step-card" style="height: 220px; display: flex; flex-direction: column; justify-content: center;"><div class="step-number">VERDICT</div><div style="font-size: 1.8rem; font-weight: 800; color: {'#f87171' if res['prediction'] == 'ANOMALY' else '#38bdf8'}; margin-bottom: 0.5rem;">{res['prediction']}</div><div style="font-size: 0.9rem; color: #cbd5e1; line-height: 1.6;">• <b>Severity:</b> {res['threat_level']}<br>• <b>Policy Action:</b> {res['action_required']}<br>• <b>Confidence Score:</b> {res['anomaly_score']:.2f}%</div></div>""", unsafe_allow_html=True)


# TAB 5: SPECS & TELEMETRY
elif st.session_state.current_tab == "Specs & Telemetry":
    st.markdown('<div class="eyebrow-tag">AI CORE TELEMETRY</div>', unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 2.2rem; font-weight: 800; color: #ffffff; margin-top: -10px;'>System Architecture & Topology</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; font-size: 1rem; margin-bottom: 1.5rem;'>Technical breakdown of the trained Extreme Gradient Boosting engine and attack vector coverage.</p>", unsafe_allow_html=True)

    col_a, col_b = st.columns(2, gap="medium")
    with col_a:
        st.markdown("""<div class="step-card"><div class="step-number">ML PIPELINE SPECIFICATIONS</div><ul style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.8; padding-left: 1.2rem;"><li><b>Primary Model:</b> Extreme Gradient Boosting (XGBoost)</li><li><b>Input Dimensionality:</b> 116 Features (Post One-Hot Encoding)</li><li><b>Normalization:</b> StandardScaler (Mean = 0, Std = 1)</li><li><b>Validation Accuracy:</b> 99.70%</li><li><b>Receiver Operating Characteristic (ROC-AUC):</b> 1.0000</li><li><b>Anomaly Recall / Sensitivity:</b> 99.57%</li></ul></div>""", unsafe_allow_html=True)

    with col_b:
        st.markdown("""<div class="step-card"><div class="step-number">ATTACK VECTOR SIGNATURES</div><ul style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.8; padding-left: 1.2rem;"><li><b>Denial of Service (DoS):</b> ICMP Ping Flood (<code>service_ecr_i</code>), Teardrop (<code>wrong_fragment</code>)</li><li><b>Port Scanning / Probing:</b> Stealth sweeps, SYN floods (<code>serror_rate</code>, <code>same_srv_rate</code>)</li><li><b>Data Exfiltration & R2L:</b> Abnormal payload surges (<code>src_bytes</code>, <code>dst_bytes</code>)</li></ul></div>""", unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)
    st.markdown("##### Top Predictive Feature Discriminators")

    feat_df = pd.DataFrame({
        "Feature": ["service_ecr_i (ICMP)", "service_http (Web)", "src_bytes (Outflow)", "wrong_fragment (Teardrop)", "count (Rate)"],
        "Importance (%)": [39.2, 20.5, 13.1, 6.1, 4.5]
    })

    fig_f = px.bar(
        feat_df, x="Importance (%)", y="Feature", orientation='h',
        color="Importance (%)",
        color_continuous_scale=['#1d4ed8', '#38bdf8']
    )
    fig_f.update_layout(
        paper_bgcolor='rgba(15, 26, 46, 0.7)',
        plot_bgcolor='rgba(6, 11, 20, 0.8)',
        font=dict(color='#cbd5e1', size=11),
        yaxis=dict(gridcolor='rgba(56, 189, 248, 0.1)'),
        xaxis=dict(gridcolor='rgba(56, 189, 248, 0.1)'),
        margin=dict(l=10, r=10, t=10, b=10),
        height=220,
        coloraxis_showscale=False
    )
    st.plotly_chart(fig_f, use_container_width=True)
