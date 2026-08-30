import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Load data
df = pd.read_csv('data/flight_delay_dataset.csv')

# Check for missing values
print(df.isna().sum())

# Features / target
x = df.drop(['departure_delay_minutes'], axis=1)
y = df['departure_delay_minutes']

# Train/test split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)

# Train model
lr = LinearRegression()
lr.fit(x_train, y_train)

# Evaluate
predict_y1 = lr.predict(x_test)
print("R2 score:", r2_score(y_test, predict_y1))
print("MSE:", mean_squared_error(y_test, predict_y1))

# Save model
joblib.dump(lr, 'models/flight_delay_model.pkl')
print("Model saved as models/flight_delay_model.pkl")
