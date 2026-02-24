import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/Housing.csv')

# Create a boxplot to show how price rises with quality
plt.figure(figsize=(10, 6))
sns.boxplot(x='OverallQual', y='SalePrice', data=df)
plt.title('House Price Distribution by Quality')
plt.savefig('visuals/price_dist.png') # Saves the chart to a folder
print("Visualization saved to visuals/price_dist.png")
