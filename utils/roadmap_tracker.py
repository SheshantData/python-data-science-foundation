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
