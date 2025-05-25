import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score

# Dummy Data Example (replace with actual dataset)
data = pd.DataFrame({
    'current_subs': [1000, 5000, 2000, 10000],
    'upload_freq': [4, 12, 6, 20],
    'age_months': [12, 24, 18, 36],
    'avg_vid_length': [10, 8, 12, 7],
    'niche': ['Tech', 'Vlogs', 'Education', 'Gaming'],
    'future_subs': [1500, 7000, 3000, 15000]  # target value
})

# One-hot encode the 'niche' column
encoded = pd.get_dummies(data['niche'], prefix='niche')
data = pd.concat([data.drop('niche', axis=1), encoded], axis=1)

# Features and target
X = data.drop('future_subs', axis=1)
y = data['future_subs']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Show coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", dict(zip(X.columns, model.coef_)))
