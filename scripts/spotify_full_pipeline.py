import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import os

# 1. SETUP & ADVANCED LOADING
if not os.path.exists('visuals'): os.makedirs('visuals')
df = pd.read_csv('data/spotify_songs.csv')

# --- SECTION 1: ADVANCED EDA ---
print("Performing Deep-Dive EDA...")

# A. Feature Distributions by Genre (Boxplots)
# This shows how 'Danceability' differs between EDM and Classical
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='playlist_genre', y='danceability', palette='coolwarm')
plt.title('Danceability Distribution Across Genres')
plt.savefig('visuals/genre_danceability_comparison.png')

# B. Tempo vs Energy (Scatter Plot)
# Checking if faster songs are always higher energy
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df.sample(2000), x='tempo', y='energy', hue='playlist_genre', alpha=0.5)
plt.title('Tempo vs Energy (Sample of 2000 songs)')
plt.savefig('visuals/tempo_energy_scatter.png')


# --- SECTION 2: FEATURE ENGINEERING ---
# Converting duration from milliseconds to minutes for better readability
df['duration_min'] = df['duration_ms'] / 60000


# --- SECTION 3: PROFESSIONAL CLUSTERING ---
features = ['danceability', 'energy', 'loudness', 'speechiness', 
            'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
X = df[features]
