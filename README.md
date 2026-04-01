# 📊 Data Science Portfolio

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📁 Projects
1. **[Titanic Survival Predictor](./scripts/titanic_analysis.py)** - Binary Classification (~80% Accuracy)
2. **[House Price Estimator](./scripts/house_prediction.py)** - Linear Regression (Predicting USD values)
3. **[Spotify Song Clustering](./scripts/spotify_full_pipeline.py)** - Unsupervised Learning (Grouping 32k+ tracks)

### 📦 Versions Used
- Pandas: `2.x`
- Scikit-Learn: `1.x`
- Python: `3.10+`

# Python Data Science Journey 🚀

This repo tracks my progress as I master the Python data stack.

## 🛠 Tools I'm Learning
- **Pandas:** Data manipulation & cleaning
- **Matplotlib/Seaborn:** Advanced EDA & Statistical Visualization
- **Scikit-Learn:** Supervised & Unsupervised Machine Learning

## 📈 Progress
- [x] Create GitHub account
- [x] Build survival prediction model (Titanic)
- [x] Complete House Price Estimator (Regression)
- [x] Implement Spotify Audio Analysis (Clustering)
- [ ] Deploy a model using a Streamlit Web App

## 🧠 Data Science Concepts Mastered
* **Supervised Learning:** Classification (Logistic Regression) vs. Regression (Linear Regression)
* **Unsupervised Learning:** Pattern recognition and grouping using K-Means Clustering
* **Data Preprocessing:** Handling missing values, feature scaling (`StandardScaler`), and encoding categorical variables
* **Model Evaluation:** Accuracy scores, Mean Absolute Error (MAE), and the "Elbow Method" for clusters

---

## 🏡 Project 1: Titanic Analysis
- **Data Cleaning:** Using `.fillna()` to handle missing values in the Age column.
- **Aggregation:** Using `.groupby()` to compare survival rates across demographics.
- **Feature Engineering:** Transforming categorical text (Sex) into numeric values.

---

## 🏡 Project 2: House Price Predictor
**Goal:** Predict the sale price of a house based on its features.
- **Status:** Completed ✅
- **Features Used:** Overall Quality, Lot Area, Year Built, and Garage Capacity.
- **Key Skill:** Implemented model persistence (saving/loading models with `joblib`).

---

## 🎵 Project 3: Spotify Song Clustering
**Goal:** Discover hidden "Audio Archetypes" in 32,000+ tracks to build automated playlists.
- **Process:** - Conducted deep-dive EDA with **Correlation Heatmaps** and **Boxplots**.
    - Scaled audio features (Tempo, Energy, Danceability) for fair mathematical weight.
    - Used **K-Means Clustering** to identify 5 distinct musical segments.
- **Insight:** Successfully isolated a "High-Energy" cluster (BPM > 125, Energy > 0.8) to generate an automated **Workout Playlist**.

---

## 🛠️ Internal Tools
- **[Roadmap Tracker](./utils/roadmap_tracker.py):** A custom Pandas script I built to track my learning progress using DataFrame filtering.

## 📊 Data Sources
- **Titanic & House Prices:** [Kaggle Datasets](https://www.kaggle.com/)
- **Spotify Tracks:** [30,000 Spotify Songs Dataset](https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs)
