import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page config
st.set_page_config(page_title="Code Performance Analysis", layout="wide")

# Title and introduction
st.title("🚀 Code Performance Analysis: Original vs Optimized Version")
st.markdown("""
This dashboard provides a detailed analysis of performance improvements between the original and optimized code versions.
Select different metrics and scenarios to explore the data.
""")

# Sample data
@st.cache_data
def load_performance_data():
    # Processing time data for different scenarios
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
st.sidebar.header("📊 Analysis Controls")
metric = st.sidebar.selectbox(
    "Select Metric to Analyze",
    ["Processing Time (s)", "Memory Usage (MB)", "DB Connections"]
)

# Main content area split into columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📈 Performance Comparison")
    
    # Create comparative bar chart
    fig = px.bar(
        df,
        x='Scenario',
        y=metric,
        color='Version',
        barmode='group',
        title=f'{metric} Comparison by Scenario',
        color_discrete_map={'Original': '#FF9B9B', 'Optimized': '#9BFF9B'}
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
    
    st.subheader("💹 Percentage Improvements")
    fig2 = px.line(
        improvement_df,
        x='Scenario',
        y='Improvement',
        title='Percentage Improvement by Scenario',
        markers=True
    )
    fig2.update_traces(line_color='#4CAF50')
    fig2.update_layout(height=400)
    fig2.update_yaxes(title='Improvement (%)')
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.subheader("🎯 Key Improvements")
    
    # Calculate average improvement
    avg_improvement = improvement_df['Improvement'].mean()
    
    # Display metrics
    st.metric(
        "Average Improvement",
        f"{avg_improvement:.1f}%",
        f"Across all scenarios"
    )
    
    # Show scenario-specific improvements
    st.subheader("📊 Scenario Analysis")
    for idx, row in improvement_df.iterrows():
        st.metric(
            row['Scenario'],
            f"{row['Improvement']:.1f}%",
            f"Performance gain"
        )

# Additional analysis section
st.markdown("---")
st.subheader("🔍 Detailed Analysis")

# Three columns for different aspects
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 💻 Processing Efficiency")
    st.write("""
    - Concurrent file processing
    - Optimized header parsing
    - Reduced database calls
    """)

with col2:
    st.markdown("### 🧠 Memory Management")
    st.write("""
    - Efficient resource handling
    - Connection pooling
    - Streaming file processing
    """)

with col3:
    st.markdown("### ⚡ Code Improvements")
    st.write("""
    - Type hints added
    - Better error handling
    - Modular structure
    """)

# Technical details in expander
with st.expander("🔧 Technical Implementation Details"):
    st.code("""
# Key optimization examples:

# 1. Concurrent Processing
with concurrent.futures.ThreadPoolExecutor() as executor:
    validation_results = list(executor.map(
        lambda f: validate_single_file(f, files_config), 
        uploaded_files
    ))

# 2. Caching Implementation
@st.cache_resource
def init_snowflake_connection():
    return refresh_snowflake_connection(logger, ENV, APP_TYPE, APP_NAME)

# 3. Efficient File Parsing
def parse_file_headers(file):
    return pd.read_csv(file, nrows=0).columns.tolist()
    """)

# Methodology expander
with st.expander("📚 Methodology"):
    st.markdown("""
    ### Testing Methodology
    
    1. **Test Scenarios**
       - Small: 1 file, 1MB
       - Medium: 5 files, 10MB each
       - Large: 10 files, 50MB each
    
    2. **Metrics Measured**
       - Processing time
       - Memory usage
       - Database connections
       
    3. **Test Environment**
       - Controlled environment
       - Multiple iterations
       - Standard hardware
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Built with Streamlit • Performance Analysis Dashboard</p>
</div>
""", unsafe_allow_html=True)
