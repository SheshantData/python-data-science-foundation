import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


# Load the data
df = pd.read_csv('data/Housing.csv')

print("--- House Data Loaded ---")
print(df.head())

# X = Features (The things that influence price)
# y = Target (The actual price)
X = df[['OverallQual', 'LotArea', 'YearBuilt', 'GarageCars']]
y = df['SalePrice']

print("\nFeatures selected for the model.")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training on {len(X_train)} houses.")

# Initialize the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("Model training complete.")
