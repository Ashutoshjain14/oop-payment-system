import pandas as pd

# Load the data
df = pd.read_csv('data/raw/retail_sales.csv')

# 1. Show data types
print("📌 Data Types:")
print(df.dtypes)

# 2. Show basic summary statistics
print("\n📊 Summary Statistics:")
print(df.describe())

# 3. Show number of missing values
print("\n❓ Missing Values:")
print(df.isnull().sum())

