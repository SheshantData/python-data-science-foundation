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

# Make predictions on the test set
predictions = model.predict(X_test)

# Calculate error
error = mean_absolute_error(y_test, predictions)

print(f"\n--- Model Results ---")
print(f"On average, our model is off by: ${error:,.2f}")

# Manual Test: Quality 8, 10000 sqft, Built 2005, 2-car garage
sample_house = [[8, 10000, 2005, 2]]
predicted_price = model.predict(sample_house)
print(f"Predicted price for sample house: ${predicted_price[0]:,.2f}")

# Add this above your manual prediction
def get_safe_prediction(data):
    if all(isinstance(i, (int, float)) for i in data[0]):
        return model.predict(data)
    else:
        return "Error: All inputs must be numbers."

# Use it
print(f"Validated Prediction: ${get_safe_prediction(new_house)[0]:,.2f}")
