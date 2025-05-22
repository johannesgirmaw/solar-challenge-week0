import sys
import os
import streamlit as st
from scripts.streamilit import load_country_data, plot_ghi_distribution, top_regions_by_ghi
from utils.config import Config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


st.set_page_config(page_title="Solar Insights Dashboard", layout="wide")

st.title("Solar Energy Insights Dashboard")
st.markdown(
    "Analyze and compare solar energy potential across Benin, Sierra Leone, and Togo.")

# --- Sidebar ---
st.sidebar.header("Filters")
country = st.sidebar.selectbox(
    "Select a country", [Config.BENIN.capitalize(), Config.SIERRALEONE.capitalize(), Config.TOGO.capitalize()])

# --- Load and Display Data ---
df = load_country_data(Config.BENIN_DATA_PATH)
st.subheader(f"{Config.BENIN} - Global Horizontal Irradiance (GHI) Analysis")

# --- Boxplot ---
st.plotly_chart(plot_ghi_distribution(df, country))

# --- Top Regions ---
st.markdown("### 📍 Top 5 Regions by GHI")
top_df = top_regions_by_ghi(df)
st.dataframe(top_df)
