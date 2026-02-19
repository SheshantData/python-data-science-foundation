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

# 7. FEATURE ENGINEERING
# Convert 'Sex' to a numeric 'Gender' column (0 for male, 1 for female)
df['Gender'] = df['Sex'].map({'male': 0, 'female': 1})

# Create a 'FarePerPerson' column (if they traveled in groups)
# This is a common way to see the "real" cost of a ticket
df['FarePerPerson'] = df['Fare'] # Simplified for now
print("\nNew columns 'Gender' and 'FarePerPerson' added.")

# 8. CORRELATION MATRIX
# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=['number'])
correlation = numeric_df.corr()

print("\n--- Correlation with Survival ---")
print(correlation['Survived'].sort_values(ascending=False))

# 9. SAVE CLEANED DATA
df.to_csv('data/titanic_processed.csv', index=False)
print("\nProcessed data saved to 'data/titanic_processed.csv'!")

# 10. FARE ANALYSIS
print(f"Most expensive ticket: {df['Fare'].max()}")
print(f"Cheapest ticket: {df['Fare'].min()}")

# 11. EMBARKED ANALYSIS (C = Cherbourg, Q = Queenstown, S = Southampton)
print("\n--- Survival by Port of Embarkation ---")
# Using fillna('S') because 'S' is the most common port
df['Embarked'] = df['Embarked'].fillna('S') 
print(df.groupby('Embarked')['Survived'].mean())
