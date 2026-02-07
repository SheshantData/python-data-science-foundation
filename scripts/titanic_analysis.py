import pandas as pd

# 1. Load the data
df = pd.read_csv('data/titanic.csv')

# 2. Look at the data
print("--- First 5 Passengers ---")
print(df.head())

# 3. Checking Missing Values
print("Missing values per column:\n", df.isnull().sum())
