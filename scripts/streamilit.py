import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px


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
