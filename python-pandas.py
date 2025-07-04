import pandas as pd

df = pd.read_csv('customers_raw.csv')
print("Datatypes:")
# df["City"] = df["City"].astype("string[pyarrow]")
print(df.dtypes)
print(df.isnull().sum())
df["Age"] = df["Age"].fillna((df["Age"].mean()).round())
df_cleaned = df.dropna(subset=["Name", "Email"])
print(df_cleaned.isnull().sum())
print(df_cleaned)
# print(df.memory_usage())