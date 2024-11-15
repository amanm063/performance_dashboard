import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page config
st.set_page_config(page_title="One Punch Code Performance", layout="wide")

# Custom CSS for One Punch Man theme
st.markdown("""
    <style>
        /* Page Background */
        body {
            background-color: #F8F8F8;
        }
        
        /* Title and header */
        .title {
            color: #FF6F61; /* Heroic red */
            font-weight: bold;
            font-size: 36px;
        }

        .header {
            color: #FF9B9B; /* Light red for headers */
        }

        /* Sidebar */
        .sidebar .sidebar-content {
            background-color: #3E3E3E;
            color: white;
        }
        
        .sidebar .sidebar-header {
            color: #FF6F61; /* Heroic red for sidebar header */
        }
        
        /* Metrics */
        .stMetricValue {
            color: #4CAF50; /* Green for positive improvements */
        }

        /* Button and Highlights */
        .stButton>button {
            background-color: #FF6F61;  /* Red button */
            color: white;
            font-weight: bold;
        }

        .stButton>button:hover {
            background-color: #FF3D2A;  /* Darker red on hover */
        }

        /* Plotly colors */
        .plotly-graph-div {
            background-color: #FFFFFF;  /* Light background for charts */
        }

        .st-expanderHeader {
            color: #FF6F61;  /* Red for expanders */
        }

        .st-expanderContent {
            color: #4CAF50;  /* Green text inside expanders */
        }
    </style>
""", unsafe_allow_html=True)

# Title and introduction
st.markdown('<p class="title">💥 One Punch Code Performance Analysis: Original vs Optimized Version</p>', unsafe_allow_html=True)
st.markdown("""
Welcome to the **One Punch** code performance analysis! 🚀 Here, you'll witness how the optimized code obliterates inefficiencies with a single punch, leaving the original version trembling.
Select different metrics and scenarios to explore how the **Optimized Code** effortlessly crushes the competition.
""")

# Sample data
@st.cache_data
def load_performance_data():
    time_data = pd.DataFrame({
        'Scenario': ['Small (1 file)', 'Medium (5 files)', 'Large (10 files)'] * 2,
        'Version': ['Original', 'Original', 'Original', 'Optimized', 'Optimized', 'Optimized'],
        'Processing Time (s)': [2.3, 12.5, 35.2, 1.8, 5.8, 12.3],
        'Memory Usage (MB)': [150, 450, 1200, 95, 180, 320],
        'DB Connections': [5, 25, 50, 1, 1, 1],
        'Files': [1, 5, 10, 1, 5, 10],
        'File Size (MB)': [1, 10, 50, 1, 10, 50]
    })
    return time_data

# Load data
df = load_performance_data()

# Sidebar for filtering
st.sidebar.header("🔧 Training Controls")
metric = st.sidebar.selectbox(
    "Select Metric to Analyze",
    ["Processing Time (s)", "Memory Usage (MB)", "DB Connections"]
)

# Main content area split into columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("💥 Heroic Performance Comparison")
    
    # Create comparative bar chart
    fig = px.bar(
        df,
        x='Scenario',
        y=metric,
        color='Version',
        barmode='group',
        title=f'{metric} Comparison: Original vs Optimized',
        color_discrete_map={'Original': '#FF9B9B', 'Optimized': '#4CAF50'}
    )
    
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

    # Calculate and display improvements
    improvements = []
    for scenario in df['Scenario'].unique():
        orig = df[(df['Scenario'] == scenario) & (df['Version'] == 'Original')][metric].values[0]
        opt = df[(df['Scenario'] == scenario) & (df['Version'] == 'Optimized')][metric].values[0]
        imp = ((orig - opt) / orig) * 100
        improvements.append({'Scenario': scenario, 'Improvement': imp})

    improvement_df = pd.DataFrame(improvements)
    
    st.subheader("🔥 Performance Gains in Percentage")
    fig2 = px.line(
        improvement_df,
        x='Scenario',
        y='Improvement',
        title='Heroic Improvement by Scenario',
        markers=True
    )
    fig2.update_traces(line_color='#4CAF50')
    fig2.update_layout(height=400)
    fig2.update_yaxes(title='Improvement (%)')
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.subheader("💪 Key Improvements")
    
    # Calculate average improvement
    avg_improvement = improvement_df['Improvement'].mean()
    
    # Display metrics
    st.metric(
        "Total Heroic Improvement",
        f"{avg_improvement:.1f}%",
        f"Across all test scenarios!"
    )
    
    # Show scenario-specific improvements
    st.subheader("🔍 Scenario-Specific Analysis")
    for idx, row in improvement_df.iterrows():
        st.metric(
            row['Scenario'],
            f"{row['Improvement']:.1f}%",
            f"Epic performance boost!"
        )

# Additional analysis section
st.markdown("---")
st.subheader("💣 Detailed Analysis: The Secret to Power")

# Three columns for different aspects
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ⚡ Processing Efficiency - One Punch Power")
    st.write("""
    - Concurrent file processing like a lightning-fast Saitama punch!
    - Optimized header parsing with zero hesitation
    - Reduced database calls, keeping the fight smooth and swift
    """)

with col2:
    st.markdown("### 🧠 Memory Management - Intelligent Control")
    st.write("""
    - Efficient resource handling to keep the system cool like Mumen Rider
    - Connection pooling, no wasted energy
    - Streaming file processing without breaking a sweat
    """)

with col3:
    st.markdown("### ⚙️ Code Improvements - The Hero's Arsenal")
    st.write("""
    - Type hints for an unbreakable structure
    - Better error handling for those unexpected villains
    - Modular code design that adapts to any battle!
    """)


# Methodology expander
with st.expander("📚 Methodology - The Hero's Strategy"):
    st.markdown("""
    ### Test Scenarios - Preparing for Battle:
    
    1. **Small**: 1 file, 1MB - A quick warm-up
    2. **Medium**: 5 files, 10MB each - A decent challenge
    3. **Large**: 10 files, 50MB each - The ultimate test
    
    ### Metrics Measured:
    - Processing time (How fast the punch lands)
    - Memory usage (How efficiently we manage our energy)
    - Database connections (How many hits we take)
    
    ### Test Environment:
    - Controlled environment
    - Multiple iterations for perfect precision
    - High-performance hardware - only the best for our hero
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Built with Streamlit • One Punch Code Performance Dashboard</p>
</div>
""", unsafe_allow_html=True)
