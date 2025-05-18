import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def inspect_data(df, columns_to_inspect):
    """
    Looks for missing values, potential outliers, and basic statistics
    for the specified columns in the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        columns_to_inspect (list): A list of column names to inspect.
    """
    print(f"--- Inspecting Columns: {columns_to_inspect} ---")

    for col in columns_to_inspect:
        print(f"\n--- Column: {col} ---")

        # 1. Missing Values
        missing_count = df[col].isnull().sum()
        missing_percentage = (missing_count / len(df)) * 100
        print(f"Missing Value Count: {missing_count}")
        print(f"Missing Value Percentage: {missing_percentage:.2f}%")

        # 2. Basic Statistics
        print("\n--- Basic Statistics ---")
        print(df[col].describe())

        # 3. Outlier Detection (using IQR and Visualization)
        print("\n--- Outlier Detection (IQR) ---")
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers_iqr = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        print(f"Number of potential outliers (IQR): {len(outliers_iqr)}")
        if not outliers_iqr.empty:
            print(f"Example outlier values:\n{outliers_iqr[col].head()}")

        # 4. Visualization (Box Plot for Outliers)
        plt.figure(figsize=(6, 4))
        sns.boxplot(x=df[col])
        plt.title(f"Box Plot of {col}")
        plt.xlabel(col)
        plt.show()

        # 5. Potential Incorrect Entries (based on domain knowledge - adjust as needed)
        print("\n--- Potential Incorrect Entries ---")
        if col in ['GHI', 'DNI', 'DHI', 'ModA', 'ModB']:
            # Allowing a small negative due to potential sensor noise
            negative_values = df[df[col] < -5][col]
            if not negative_values.empty:
                print(
                    f"Number of potentially incorrect (significantly negative) values: {len(negative_values)}")
                print(f"Example negative values:\n{negative_values.head()}")
            else:
                print("No significantly negative values found.")
        elif col in ['WS', 'WSgust']:
            # Wind speed should generally be non-negative
            negative_ws = df[df[col] < 0][col]
            if not negative_ws.empty:
                print(
                    f"Number of potentially incorrect (negative) wind speed values: {len(negative_ws)}")
                print(
                    f"Example negative wind speed values:\n{negative_ws.head()}")
            else:
                print("No negative wind speed values found.")
