import pandas as pd


def read_csv_file():
    df = pd.read_csv('data/benin-malanville.csv')
    return df
