import pandas as pd

# 1. Load the data
df = pd.read_csv('data/titanic.csv')

# 2. Look at the data
print("--- First 5 Passengers ---")
print(df.head())

# 3. Calculate survival rate by Gender (The 'Pandas' way)
survival_by_sex = df.groupby('Sex')['Survived'].mean()

print("\n--- Survival Rate by Sex ---")
print(survival_by_sex)

# 4. Filter for high-paying passengers
elite_group = df[df['Fare'] > 50]
print("\n--- Passengers who paid more than $50 ---")
print(elite_group)
