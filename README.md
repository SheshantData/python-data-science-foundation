# 📊 Data Science Portfolio

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📁 Projects
1. **[Titanic Survival Predictor](./scripts/titanic_model.py)** - Binary Classification (~80% Accuracy)
2. **[House Price Estimator](./scripts/house_prediction.py)** - Linear Regression (Predicting USD values)


### 📦 Versions Used
- Pandas: `2.x`
- Scikit-Learn: `1.x`
- Python: `3.10+`
- 
# Python Data Science Journey 🚀

This repo tracks my progress as I master the Python data stack.

## 🛠 Tools I'm Learning
- **Pandas:** Data manipulation
- **Matplotlib/Seaborn:** Visualization (EDA)
- **Scikit-Learn:** Machine Learning

## 📈 Progress
- [x] Create GitHub account
- [x] Initialize first repo
- [x] Complete first Pandas tutorial
- [x] Build a survival prediction model (Titanic)

## 🧠 Data Science Concepts Mastered

* **Supervised Learning:** Classification vs. Regression
* **Data Splitting:** Training vs. Testing sets (80/20 split)
* **Feature Selection:** Choosing numeric inputs for model accuracy
* **Model Evaluation:** Accuracy (Classification) and MAE (Regression)

## 🏡 Project 1: Titanic Analysis

- **Data Cleaning:** Using `.fillna()` to handle missing values in the Age column.
- **Aggregation:** Using `.groupby()` to compare survival rates across demographics.
- **Correlation:** Analyzing how features like `Fare` and `Pclass` relate to survival outcomes.
- **Feature Engineering:** Transforming categorical text (Sex) into numeric values (Gender).

- ---

## 🏡 Project 2: House Price Predictor
**Goal:** Predict the sale price of a house based on its features.
- **Type:** Linear Regression
- **Model:** Linear Regression (In Progress)
- **Features Used:** Overall Quality, Lot Area, Year Built, and Garage Capacity.
- **Current Status:** Data cleaned and split into training/testing sets.

 ### 🚀 Future Improvements
- [ ] Add more features like "Neighborhood" and "Condition".
- [x] Try a Random Forest Regressor to improve accuracy.
- [ ] Build a web interface using Streamlit.


## 🛠️ Internal Tools
- **[Roadmap Tracker](./utils/roadmap_tracker.py):** A custom Pandas script I built to track my learning progress and estimate project timelines using DataFrame filtering.
