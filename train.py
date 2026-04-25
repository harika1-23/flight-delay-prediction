import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv("flight_data_2024.csv", low_memory=False)

# Select columns
cols = [
    "dep_delay",
    "carrier_delay",
    "weather_delay",
    "nas_delay",
    "security_delay",
    "late_aircraft_delay",
    "taxi_out",
    "air_time",
    "distance",
    "arr_delay"
]

df = df[cols]

# 🔥 Convert all to numeric (VERY IMPORTANT)
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 🔥 Remove NaN values
df = df.dropna()

# Features & target
X = df.drop("arr_delay", axis=1)
y = df["arr_delay"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained successfully after FULL CLEANING ✅")