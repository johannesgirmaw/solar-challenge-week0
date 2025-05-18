import pandas as pd


def clean_data(df: pd.DataFrame, unnecessary_columns: list = []) -> pd.DataFrame:

    # 1. Describe all numeric columns
    print("--- Descriptive Statistics for Numeric Columns ---")
    print(df.describe())

    # 2. Calculate the number of missing values per column
    print("\n--- Missing Value Counts per Column ---")
    missing_counts = df.isna().sum()
    print(missing_counts)

    # 3. Identify columns with > 5% nulls
    total_rows = len(df)
    null_percentage_threshold = 0.05  # 5%

    columns_with_high_nulls = missing_counts[missing_counts /
                                             total_rows > null_percentage_threshold].index.tolist()

    print("\n--- Columns with > 5% Missing Values ---")
    if columns_with_high_nulls:
        print(columns_with_high_nulls)
    else:
        print("No columns have more than 5% missing values.")
