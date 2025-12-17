import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px

# Page config with custom theme
st.set_page_config(
    page_title="AIL-2045 Bitcoin & Crypto Finance Platform", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "AIL-2045 Bitcoin & Crypto Finance Platform for African Infrastructure"
    }
)

# Simple Password Protection
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.markdown("<h1 style='text-align: center; color: #F7931A;'>🔐 Demo Access</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        password = st.text_input("Enter Password:", type="password", key="pwd_input")
        if st.button("Access Demo", use_container_width=True):
            if password == "demo2024":  # Change this password
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Incorrect password")
        st.info("💡 Password: demo2024")
    st.stop()

# App content starts here (password is correct)

# Custom CSS for beautiful styling with DARK MODE
st.markdown("""
<style>
    /* Main app background - DARK MODE */
    .stApp {
        background: linear-gradient(to bottom right, #1a1a2e, #16213e);
    }
    
    /* Headers */
    h1 {
        color: #F7931A;
        text-align: center;
        font-size: 3rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        padding: 20px 0;
        animation: glow 2s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 0 5px #F7931A, 0 0 10px #F7931A; }
        to { text-shadow: 0 0 10px #F7931A, 0 0 20px #F7931A, 0 0 30px #F7931A; }
    }
    h3 {
        color: #00d4ff;
        text-align: center;
        font-size: 1.3rem !important;
    }
    
    /* Metric cards */
    .stMetric {
        background: linear-gradient(135deg, rgba(247, 147, 26, 0.1), rgba(0, 212, 255, 0.1));
        padding: 20px;
        border-radius: 15px;
        border: 2px solid rgba(247, 147, 26, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
    }
    .stMetric label {
        color: #00d4ff !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
    }
    .stMetric [data-testid="stMetricValue"] {
        color: #F7931A !important;
        font-size: 2rem !important;
        font-weight: bold !important;
    }
    .stMetric [data-testid="stMetricDelta"] {
        color: #4ade80 !important;
    }
    
    /* Sidebar - CLEAN & BEAUTIFUL DESIGN */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0f1e 0%, #1a1a2e 50%, #16213e 100%);
        border-right: 2px solid rgba(247, 147, 26, 0.3);
        box-shadow: 4px 0 20px rgba(247, 147, 26, 0.1);
    }
    section[data-testid="stSidebar"] > div {
        background: transparent;
        padding: 20px 15px;
    }
    
    /* Sidebar text colors - CLEAN & READABLE */
    section[data-testid="stSidebar"] label {
        color: #e0e0e0 !important;
        font-size: 0.8rem !important;
        font-weight: 500 !important;
        margin-bottom: 3px !important;
    }
    section[data-testid="stSidebar"] .stMarkdown {
        color: white !important;
    }
    section[data-testid="stSidebar"] h2 {
        color: #F7931A !important;
    }
    section[data-testid="stSidebar"] h3 {
        color: #00d4ff !important;
    }
    section[data-testid="stSidebar"] p {
        color: #b0b0b0 !important;
        font-size: 0.9rem !important;
    }
    
    /* Sidebar sliders - EXTRA COMPACT DESIGN */
    section[data-testid="stSidebar"] .stSlider {
        padding: 6px 5px;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 8px;
        margin: 5px 0;
        border: 1px solid rgba(247, 147, 26, 0.15);
        transition: all 0.3s ease;
    }
    section[data-testid="stSidebar"] .stSlider:hover {
        background: rgba(255, 255, 255, 0.05);
        border-color: rgba(247, 147, 26, 0.3);
        box-shadow: 0 0 15px rgba(247, 147, 26, 0.2);
    }
    
    /* Slider track styling */
    section[data-testid="stSidebar"] div[role="slider"] {
        background: linear-gradient(90deg, #F7931A 0%, #00d4ff 100%) !important;
    }
    
    /* Slider value display */
    section[data-testid="stSidebar"] .stSlider > div > div > div {
        color: #F7931A !important;
        font-weight: 600 !important;
    }
    
    /* Project card */
    .project-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid rgba(247, 147, 26, 0.3);
        margin: 10px 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(247, 147, 26, 0.1);
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        color: #00d4ff;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(247, 147, 26, 0.3), rgba(0, 212, 255, 0.3));
        color: #F7931A;
    }
    
    /* General text colors - DARK MODE */
    .stMarkdown, p, span, label, div {
        color: white;
    }
    
    /* Selectbox and slider styling - DARK MODE */
    .stSelectbox label, .stSlider label {
        color: white !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
    }
    
    /* Selectbox dropdown - DARK MODE with visibility */
    div[data-baseweb="select"] > div {
        background-color: #2d3748 !important;
        color: white !important;
        border: 1px solid rgba(247, 147, 26, 0.5) !important;
    }
    [data-baseweb="popover"] {
        background-color: #2d3748 !important;
    }
    [role="listbox"] {
        background-color: #2d3748 !important;
        border: 1px solid rgba(247, 147, 26, 0.5) !important;
    }
    [role="option"] {
        background-color: #2d3748 !important;
        color: white !important;
        padding: 10px !important;
    }
    [role="option"]:hover {
        background-color: rgba(247, 147, 26, 0.2) !important;
        color: #F7931A !important;
    }
    
    /* Slider value display */
    .stSlider [data-testid="stTickBarMin"],
    .stSlider [data-testid="stTickBarMax"] {
        color: white !important;
    }
    
    /* DataFrame */
    .dataframe {
        color: white !important;
        background-color: rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Download button - VISIBLE */
    .stDownloadButton > button {
        background-color: #F7931A !important;
        color: white !important;
        border: 2px solid #F7931A !important;
        font-weight: bold !important;
        padding: 0.75rem 1.5rem !important;
        font-size: 1rem !important;
    }
    .stDownloadButton > button:hover {
        background-color: #e68a17 !important;
        border-color: #e68a17 !important;
        transform: scale(1.05);
    }
    .stDownloadButton > button p {
        color: white !important;
        margin: 0 !important;
    }
    
    /* Settings menu (hamburger) - VISIBLE */
    button[kind="header"] {
        color: white !important;
        background-color: rgba(247, 147, 26, 0.2) !important;
    }
    button[kind="header"]:hover {
        background-color: rgba(247, 147, 26, 0.4) !important;
    }
    
    /* Top right menu items */
    [data-testid="stHeader"] {
        background: transparent !important;
    }
    [data-testid="stHeader"] button {
        color: white !important;
    }
    
    /* Make sure all buttons are visible */
    button {
        color: white !important;
    }
    
    /* Info box */
    .stAlert {
        background-color: rgba(0, 212, 255, 0.1) !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("AIL-2045 Bitcoin & Crypto Finance Platform")
st.markdown("### Test $4T industrial leap with BTC, Bond, FDI & NFT (2026-2045)")

# Sidebar with enhanced styling
st.sidebar.markdown("""<div style='background: linear-gradient(135deg, rgba(247,147,26,0.1) 0%, rgba(0,212,255,0.1) 100%); padding: 8px 10px; border-radius: 8px; border: 1px solid rgba(247,147,26,0.3); margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);'><h3 style='color: #F7931A; font-size: 16px; font-weight: bold; margin: 0; text-shadow: 0 0 5px rgba(247,147,26,0.3); letter-spacing: 0.3px; text-align: center;'>⚙️ Model Parameters</h3></div>""", unsafe_allow_html=True)
btc_seed = st.sidebar.slider("BTC Seed ($B)", 5.0, 100.0, 35.0, 5.0)
btc_cagr = st.sidebar.slider("BTC CAGR (%)", 1.0, 30.0, 15.0, 1.0) / 100
years = st.sidebar.slider("Forecast Years", 5, 30, 19)
bond_amount = st.sidebar.slider("Tokenized Bonds ($B)", 10.0, 400.0, 200.0, 25.0)
bond_yield = st.sidebar.slider("Bond Yield (%)", 1.0, 8.0, 4.0, 0.5) / 100
fdi_amount = st.sidebar.slider("Crypto FDI ($B)", 5.0, 150.0, 50.0, 10.0)
nft_amount = st.sidebar.slider("Carbon NFTs ($B)", 1.0, 100.0, 15.0, 5.0)

# Calculations
btc_final = btc_seed * (1 + btc_cagr) ** years
btc_gain = btc_final - btc_seed
bond_interest = bond_amount * bond_yield * 10
fdi_return = fdi_amount * (1.20 ** 10)
nft_return = nft_amount * (1.12 ** years)
total_unlocked = btc_final + bond_interest + fdi_return + nft_return
gap_covered = total_unlocked / 1.5  # Africa's $1.5T gap
roi_crypto = ((total_unlocked - (btc_seed + bond_amount + fdi_amount + nft_amount)) / 
              (btc_seed + bond_amount + fdi_amount + nft_amount)) * 100

# Traditional finance comparison
trad_cost = (bond_amount * 0.07 * 10) + (fdi_amount * 0.08 * 10) + (btc_seed * 0.03 * years)
savings = (bond_interest + fdi_return + btc_gain + nft_return) - trad_cost
jobs = int(total_unlocked * 100_000)

# Key Metrics Dashboard
st.markdown("## 📈 Key Performance Indicators")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🪙 BTC Value 2045", 
        f"${btc_final:,.1f}B", 
        f"+${btc_gain:,.1f}B ({(btc_gain/btc_seed)*100:.0f}%)"
    )
    st.metric(
        "💎 Total Capital Unlocked", 
        f"${total_unlocked:,.1f}B",
        f"↑ {total_unlocked/btc_seed:.1f}x multiplier"
    )

with col2:
    st.metric(
        "🎯 Financing Gap Covered", 
        f"{gap_covered:.1%}",
        f"${total_unlocked:,.1f}B / $1.5T target"
    )
    st.metric(
        "📊 Crypto ROI", 
        f"{roi_crypto:,.0f}%",
        f"vs {(trad_cost/(btc_seed + bond_amount + fdi_amount))*100:.0f}% traditional"
    )

with col3:
    st.metric(
        "💵 Savings vs Traditional", 
        f"${savings:,.1f}B",
        f"{(savings/trad_cost)*100:.0f}% cost reduction"
    )
    st.metric(
        "👷 Jobs Created", 
        f"{jobs:,}",
        f"{jobs/1_000_000:.1f}M employment"
    )

# Interactive Charts in Tabs
st.markdown("## 📊 Visual Analytics")
tab1, tab2, tab3, tab4 = st.tabs(["📈 Growth Trajectory", "🥧 Capital Breakdown", "⚡ ROI Comparison", "🌍 Impact Metrics"])

with tab1:
    # Enhanced Matplotlib chart with dark theme
    years_list = list(range(2026, 2026 + years + 1))
    btc_curve = np.array([btc_seed * (1 + btc_cagr) ** i for i in range(years + 1)])
    
    fig, ax = plt.subplots(figsize=(14, 8), facecolor='#1a1a2e')
    ax.set_facecolor('#16213e')
    
    # Main BTC growth line
    ax.plot(years_list, btc_curve, label="BTC Growth Trajectory", 
            color="#F7931A", linewidth=4, marker='o', markersize=6, 
            markerfacecolor='#FFD700', markeredgecolor='#F7931A', markeredgewidth=2)
    
    # $1.5T Gap line
    ax.axhline(1500, color="#ff4757", linestyle="--", linewidth=3, 
               label="$1.5T Financing Gap", alpha=0.8)
    
    # Shaded areas
    below_mask = btc_curve <= 1500
    ax.fill_between(years_list, btc_curve, 0, where=below_mask, 
                     color="#F7931A", alpha=0.2, label="Gap Closure Progress")
    ax.fill_between(years_list, btc_curve, 1500, where=below_mask, 
                     color="#F7931A", alpha=0.1)
    
    above_mask = btc_curve > 1500
    ax.fill_between(years_list, btc_curve, 1500, where=above_mask, 
                     color="#4ade80", alpha=0.3, label="Capital Surplus")
    
    # Annotations with better styling
    ax.text(years_list[0] - 0.5, btc_seed + 80, 
            f"🚀 Start\n${btc_seed:.0f}B", 
            color="#00d4ff", fontsize=13, fontweight='bold', 
            ha='right', bbox=dict(boxstyle='round', facecolor='#1a1a2e', alpha=0.8))
    ax.text(years_list[-1] + 0.5, btc_curve[-1], 
            f"🎯 Target\n${btc_curve[-1]:.0f}B", 
            color="#4ade80", fontsize=13, fontweight='bold', 
            ha='left', bbox=dict(boxstyle='round', facecolor='#1a1a2e', alpha=0.8))
    
    # Styling
    ax.set_title("How Bitcoin Growth Closes Africa's $1.5T Financing Gap", 
                 fontsize=18, pad=25, color='white', fontweight='bold')
    ax.set_xlabel("Year", fontsize=14, color='white')
    ax.set_ylabel("Capital ($ Billion)", fontsize=14, color='white')
    ax.set_ylim(0, max(1500, btc_curve.max() * 1.15))
    ax.set_xlim(years_list[0] - 1, years_list[-1] + 1)
    ax.grid(True, alpha=0.2, linestyle='--', color='white')
    ax.legend(loc='upper left', frameon=True, fancybox=True, 
              shadow=True, fontsize=11, facecolor='#1a1a2e', 
              edgecolor='#F7931A', labelcolor='white')
    ax.tick_params(colors='white', labelsize=10)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:.0f}B"))
    
    st.pyplot(fig)

with tab2:
    # Pie chart with Plotly - dark theme
    labels = ['BTC Holdings', 'Bond Interest', 'Crypto FDI Returns', 'Carbon NFTs']
    values = [btc_final, bond_interest, fdi_return, nft_return]
    colors = ['#F7931A', '#00d4ff', '#4ade80', '#a78bfa']
    
    fig_pie = go.Figure(data=[go.Pie(
        labels=labels, 
        values=values,
        hole=0.4,
        marker=dict(colors=colors, line=dict(color='#1a1a2e', width=2)),
        textinfo='label+percent',
        textfont=dict(size=14, color='white'),
        hovertemplate='<b>%{label}</b><br>$%{value:.1f}B<br>%{percent}<extra></extra>'
    )])
    
    fig_pie.update_layout(
        title="Capital Source Breakdown 2045",
        title_font=dict(size=20, color='white'),
        paper_bgcolor='#1a1a2e',
        plot_bgcolor='#16213e',
        showlegend=True,
        legend=dict(font=dict(color='white')),
        height=500
    )
    
    st.plotly_chart(fig_pie, use_container_width=True)

with tab3:
    # ROI Comparison Bar Chart - dark theme
    comparison_data = pd.DataFrame({
        'Financing Method': ['Crypto Model', 'Traditional Finance'],
        'ROI (%)': [roi_crypto, (trad_cost/(btc_seed + bond_amount + fdi_amount))*100],
        'Total Return ($B)': [total_unlocked, trad_cost]
    })
    
    fig_bar = go.Figure(data=[
        go.Bar(
            x=comparison_data['Financing Method'],
            y=comparison_data['ROI (%)'],
            text=comparison_data['ROI (%)'].apply(lambda x: f'{x:.0f}%'),
            textposition='auto',
            marker=dict(
                color=['#F7931A', '#ff4757'],
                line=dict(color='white', width=2)
            ),
            hovertemplate='<b>%{x}</b><br>ROI: %{y:.0f}%<extra></extra>'
        )
    ])
    
    fig_bar.update_layout(
        title="ROI Comparison: Crypto vs Traditional Financing",
        title_font=dict(size=20, color='white'),
        xaxis=dict(title="Financing Method", color='white'),
        yaxis=dict(title="Return on Investment (%)", color='white'),
        paper_bgcolor='#1a1a2e',
        plot_bgcolor='#16213e',
        height=500,
        showlegend=False
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)

with tab4:
    # Impact metrics visualization
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🌍 Socioeconomic Impact")
        impact_data = {
            "Metric": ["Jobs Created", "GDP Impact", "Carbon Credits", "Infrastructure Projects"],
            "Value": [
                f"{jobs:,}",
                f"${total_unlocked * 0.3:,.1f}B",
                f"{nft_return * 100:,.0f}M tons",
                f"{int(total_unlocked / 0.5):,}"
            ]
        }
        st.dataframe(
            pd.DataFrame(impact_data),
            use_container_width=True,
            hide_index=True
        )
    
    with col2:
        st.markdown("### ⚡ Efficiency Gains")
        efficiency_data = {
            "Metric": ["Cost Savings", "Time Reduction", "Transparency", "Access to Capital"],
            "Improvement": [
                f"{(savings/trad_cost)*100:.0f}%",
                "60%",
                "95%",
                f"{(total_unlocked/1500)*100:.0f}%"
            ]
        }
        st.dataframe(
            pd.DataFrame(efficiency_data),
            use_container_width=True,
            hide_index=True
        )

# Option 1: Grid Cards Layout (COMPACT VERSION) for Projects Section
# Smaller cards and investment section

st.markdown("## 🏗️ Real 6 African Infrastructure Projects - Afreximbank/AfDB/World Bank")

# Projects data
projects_grid = {
    "LAPSSET": {
        "name": "LAPSSET Corridor",
        "icon": "🚄",
        "budget": "$1.2B",
        "country": "Kenya, Ethiopia",
        "type": "BTC Bond",
        "description": "Lamu Port-South Sudan-Ethiopia Transport",
        "min": 100, "max": 1000, "default": 500
    },
    "Rufiji": {
        "name": "Rufiji Hydro Dam",
        "icon": "⚡",
        "budget": "$0.5B",
        "country": "Tanzania",
        "type": "Crypto FDI",
        "description": "2,100 MW Hydroelectric Power",
        "min": 50, "max": 500, "default": 200
    },
    "Angola": {
        "name": "Eastern Angola Agri",
        "icon": "🌾",
        "budget": "$211M",
        "country": "Angola",
        "type": "BTC Bond",
        "description": "Agricultural Development Zone",
        "min": 50, "max": 300, "default": 100
    },
    "Egypt": {
        "name": "Egypt Pharma Hub",
        "icon": "💊",
        "budget": "$746M",
        "country": "Egypt",
        "type": "BTC Bond",
        "description": "Pharmaceutical Manufacturing",
        "min": 100, "max": 1000, "default": 300
    },
    "Nacala": {
        "name": "Nacala Corridor",
        "icon": "🚂",
        "budget": "$2.7B",
        "country": "Mozambique",
        "type": "BTC Bond",
        "description": "Railway and Port Development",
        "min": 300, "max": 1500, "default": 800
    },
    "Nigeria": {
        "name": "Nigeria Mfg Zones",
        "icon": "🏭",
        "budget": "$300M+",
        "country": "Nigeria",
        "type": "Crypto FDI",
        "description": "Special Economic Zones",
        "min": 50, "max": 500, "default": 150
    }
}

# Session state for selected project
if 'selected_project_grid' not in st.session_state:
    st.session_state.selected_project_grid = None

# Compact card style
def render_compact_card(project_key, project_data, column):
    with column:
        # Determine badge color based on type
        badge_bg = "rgba(247, 147, 26, 0.2)" if "Bond" in project_data['type'] else "rgba(0, 212, 255, 0.2)"
        badge_color = "#F7931A" if "Bond" in project_data['type'] else "#00d4ff"
        
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, rgba(247, 147, 26, 0.08), rgba(0, 212, 255, 0.08));
            padding: 12px;
            border-radius: 10px;
            border: 1px solid rgba(247, 147, 26, 0.25);
            box-shadow: 0 4px 12px rgba(31, 38, 135, 0.25);
            transition: all 0.3s ease;
            height: 100%;
        " onmouseover="this.style.borderColor='rgba(247, 147, 26, 0.5)'; this.style.boxShadow='0 6px 20px rgba(247, 147, 26, 0.25)';" 
           onmouseout="this.style.borderColor='rgba(247, 147, 26, 0.25)'; this.style.boxShadow='0 4px 12px rgba(31, 38, 135, 0.25)';">
            <div style="text-align: center; margin-bottom: 8px;">
                <span style="font-size: 2rem;">{project_data['icon']}</span>
            </div>
            <h4 style="color: #F7931A; font-size: 1rem; margin: 0 0 5px 0; text-align: center;">
                {project_data['name']}
            </h4>
            <p style="color: #00d4ff; font-size: 1.3rem; font-weight: bold; margin: 6px 0; text-align: center;">
                {project_data['budget']}
            </p>
            <p style="color: #a0a0a0; font-size: 0.8rem; margin: 5px 0; text-align: center;">
                📍 {project_data['country']}
            </p>
            <div style="text-align: center; margin: 8px 0;">
                <span style="background: {badge_bg}; padding: 3px 8px; border-radius: 10px; 
                             color: {badge_color}; font-size: 0.7rem;">
                    {project_data['type']}
                </span>
            </div>
            <p style="color: #b0b0b0; font-size: 0.75rem; margin: 8px 0; text-align: center; min-height: 32px; line-height: 1.3;">
                {project_data['description']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Select", key=f"btn_{project_key}", use_container_width=True):
            st.session_state.selected_project_grid = project_key

# Create compact grid
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

# Row 1
col1, col2, col3 = st.columns(3)
render_compact_card("LAPSSET", projects_grid["LAPSSET"], col1)
render_compact_card("Rufiji", projects_grid["Rufiji"], col2)
render_compact_card("Angola", projects_grid["Angola"], col3)

# Row 2
col4, col5, col6 = st.columns(3)
render_compact_card("Egypt", projects_grid["Egypt"], col4)
render_compact_card("Nacala", projects_grid["Nacala"], col5)
render_compact_card("Nigeria", projects_grid["Nigeria"], col6)

# Compact Investment Calculator (appears when project selected)
if st.session_state.selected_project_grid:
    selected_proj = st.session_state.selected_project_grid
    selected_data = projects_grid[selected_proj]
    
    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <h4 style="color: #F7931A; font-size: 1.2rem; text-align: center; margin-bottom: 15px;">
        💵 Investment Calculator - {selected_data['icon']} {selected_data['name']}
    </h4>
    """, unsafe_allow_html=True)
    
    # Compact slider
    tranche = st.slider(
        f"Investment Amount ($M)",
        min_value=selected_data['min'],
        max_value=selected_data['max'],
        value=selected_data['default'],
        step=25,
        key=f"grid_slider_{selected_proj}",
        help=f"Range: ${selected_data['min']}M - ${selected_data['max']}M"
    )
    
    # Compact investment display
    st.markdown(f"""
    <div style="text-align: center; margin: 12px 0; padding: 10px; background: rgba(247, 147, 26, 0.1); border-radius: 10px;">
        <h3 style="color: #F7931A; font-size: 1.8rem; margin: 0;">${tranche:,}M</h3>
        <p style="color: #00d4ff; font-size: 0.85rem; margin: 3px 0;">Your Investment</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Calculate returns
    if "Bond" in selected_data['type']:
        value = tranche / 1000 * (1 + btc_cagr) ** years
        investment_period = years
        annual_return = btc_cagr * 100
    else:  # FDI
        fdi_years = 10
        if selected_proj == "Rufiji":
            value = tranche / 1000 * (1.22 ** fdi_years)
            annual_return = 22
        else:
            value = tranche / 1000 * (1.25 ** fdi_years)
            annual_return = 25
        investment_period = fdi_years
    
    roi_project = ((value * 1000 - tranche) / tranche) * 100
    gain = value - tranche/1000
    jobs_created = int(value * 100_000)
    
    # Compact results row
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.metric("💎 Final Value", f"${value:.2f}B", f"+{roi_project:,.0f}%")
    
    with col_b:
        st.metric("📈 Total Gain", f"${gain:.2f}B", f"{investment_period}yr")
    
    with col_c:
        st.metric("👷 Jobs", f"{jobs_created:,}", f"{annual_return:.1f}%")
# Export Section
st.markdown("## 📥 Export & Documentation")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    # Forecast data
    years_list = list(range(2026, 2026 + years + 1))
    btc_curve = [btc_seed * (1 + btc_cagr) ** i for i in range(years + 1)]
    
    df_forecast = pd.DataFrame({
        "Year": years_list,
        "BTC Value ($B)": [f"${x:.2f}" for x in btc_curve],
        "Cumulative Gain ($B)": [f"${x - btc_seed:.2f}" for x in btc_curve],
        "Gap Coverage (%)": [f"{(x/1.5)*100:.1f}%" for x in btc_curve]
    })
    
    csv_forecast = df_forecast.to_csv(index=False)
    st.download_button(
        "📊 Download Full Forecast (CSV)",
        csv_forecast,
        "ail2045_forecast.csv",
        "text/csv",
        use_container_width=True
    )

with col2:
    # Summary report
    summary_data = {
        "Metric": [
            "BTC Seed Capital",
            "BTC Final Value 2045",
            "Total Capital Unlocked",
            "Financing Gap Covered",
            "Crypto ROI",
            "Jobs Created",
            "Cost Savings"
        ],
        "Value": [
            f"${btc_seed:.1f}B",
            f"${btc_final:.1f}B",
            f"${total_unlocked:.1f}B",
            f"{gap_covered:.1%}",
            f"{roi_crypto:.0f}%",
            f"{jobs:,}",
            f"${savings:.1f}B"
        ]
    }
    df_summary = pd.DataFrame(summary_data)
    csv_summary = df_summary.to_csv(index=False)
    
    st.download_button(
        "📋 Download Summary Report (CSV)",
        csv_summary,
        "ail2045_summary.csv",
        "text/csv",
        use_container_width=True
    )

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #00d4ff; padding: 20px;">
    <h4 style="color: #F7931A;">🚀 Bitcoin & Crypto Finance Platform | AIF 2025 Ready</h4>
    <p style="color: white;">Revolutionizing African Infrastructure Finance through Bitcoin & Crypto Innovation</p>
    <p style="color: #F7931A;"><strong>Built with ❤️ for Africa's Future</strong></p>
    <p style="font-size: 0.9rem; color: gray;">
        Data sources: AfDB, Afreximbank, World Bank | Model: AIL-2045 v2.0
    </p>
</div>
""", unsafe_allow_html=True)
