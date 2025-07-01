import pandas as pd

# Load the raw CSV file
df = pd.read_csv('data/raw/retail_sales.csv')

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Show column names
print("\nColumns:")
print(df.columns)
