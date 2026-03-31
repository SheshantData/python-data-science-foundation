import pandas as pd

# 1. Load the data
df = pd.read_csv('data/spotify_songs.csv')

# 2. Select only the numeric audio features for clustering
features = ['danceability', 'energy', 'loudness', 'speechiness', 
            'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']

X = df[features]

print(f"Dataset loaded with {X.shape[0]} songs and {X.shape[1]} features.")
