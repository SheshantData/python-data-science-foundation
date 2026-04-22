import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 1. Setup - making sure we have a place for the charts
if not os.path.exists('visuals'): 
    os.makedirs('visuals')

# Loading the built-in dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
target_names = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
df['species_name'] = df['species'].map(target_names)

# --- 2. THE EDA (Exploratory Data Analysis) ---
print("Crunching the visuals...")

# The "Overview" - Pairplot
# This is the classic way to see how features overlap
plt.figure(figsize=(10, 8))
sns.pairplot(df.drop('species', axis=1), hue='species_name', palette='husl')
plt.savefig('visuals/iris_pairplot.png')

# The "Deep Dive" - Violin Plots
# Good for seeing the density and spread of each measurement
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
for i, col in enumerate(iris.feature_names):
    sns.violinplot(ax=axes[i//2, i%2], x='species_name', y=col, data=df, palette='muted')
plt.tight_layout()
plt.savefig('visuals/iris_violin_plots.png')
