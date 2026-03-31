import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import os

# 1. SETUP & ADVANCED LOADING
if not os.path.exists('visuals'): os.makedirs('visuals')
df = pd.read_csv('data/spotify_songs.csv')
