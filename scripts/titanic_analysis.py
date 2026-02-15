import pandas as pd

# 1. Load the data
df = pd.read_csv('data/titanic.csv')

# 2. Look at the data
print("--- First 5 Passengers ---")
print(df.head())

# 3. Checking Missing Values
print("Missing values per column:\n", df.isnull().sum())

# 4. CLEANING DATA
# Fill missing age values with the median (a common ML practice)
df['Age'] = df['Age'].fillna(df['Age'].median())

# 5: STATISTICAL SUMMARY ---
print("\nDataset Summary Statistics:\n", df.describe())

# 6. SURVIVAL ANALYSIS BY GROUP
# Does gender play a role?
print("\n--- Survival Rate by Sex ---")
print(df.groupby('Sex')['Survived'].mean())
