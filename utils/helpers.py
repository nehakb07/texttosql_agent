import pandas as pd
import os

def clean_sales_data(input_path="data/sales.csv",
                     output_path="data/sales_cleaned.csv"):

    df = pd.read_csv(input_path)

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert date columns to datetime
    date_cols = ["Order Date", "Ship Date"]
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Convert numeric columns
    numeric_cols = [
        "Units Sold",
        "Unit Price",
        "Unit Cost",
        "Total Revenue",
        "Total Cost",
        "Total Profit",
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df[numeric_cols] = df[numeric_cols].fillna(0)

    # Save cleaned copy for visibility
    df.to_csv(output_path, index=False)

    return df

