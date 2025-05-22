import sys
import os
import streamlit as st
import pandas as pd
import plotly.express as px


class Config:
    BENIN_DATA_PATH = 'clean_data/benin_clean.csv'
    SIERRALEONE_DATA_PATH = 'clean_data/sierraleone_clean.csv'
    TOGO_DATA_PATH = 'clean_data/togo_clean.csv'
    BENIN = 'benin'
    SIERRALEONE = "sierraleone"
    TOGO = 'togo'


@st.cache_data
def load_country_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def top_regions_by_ghi(df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
    return df.groupby("Timestamp")["GHI"].mean().sort_values(ascending=False).head(top_n).reset_index()


def plot_ghi_distribution(df: pd.DataFrame, country: str):
    fig = px.box(
        df, x='Timestamp', y='GHI',
        color_discrete_sequence=['#FDB813'],
        title=f"GHI Distribution in {country}",
        template='plotly_white'
    )
    fig.update_layout(xaxis_title="Region",
                      yaxis_title="GHI (kWh/m²/day)", showlegend=False)
    return fig


# Stream lit UI implementation
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
