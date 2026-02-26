import pandas as pd

# Creating a tiny dataset manually
data = {
    'Topic': ['Pandas', 'EDA', 'Machine Learning'],
    'Status': ['Learning', 'Pending', 'Goal'],
    'Difficulty': [3, 4, 5]
}

df = pd.DataFrame(data)

print("--- My Learning Roadmap ---")
print(df)

# A quick Pandas trick: Filter for high difficulty
# This demonstrates Boolean Indexing in Pandas
hard_stuff = df[df['Difficulty'] >= 4]
print("\n--- Hardest Topics ---")
print(hard_stuff)

# Adding a new column to the tracker
df['Weeks_Estimated'] = [2, 3, 6]

# Calculate total time
total_weeks = df['Weeks_Estimated'].sum()
print(f"\nTotal estimated time to mastery: {total_weeks} weeks")
