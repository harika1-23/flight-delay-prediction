import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("vite-project/public/flight_data_2024.csv")

features = [
    "dep_delay",
    "carrier_delay",
    "weather_delay",
    "nas_delay",
    "security_delay",
    "late_aircraft_delay"
]

df[features] = df[features].fillna(0)
df["arr_delay"] = df["arr_delay"].fillna(0)

X = df[features]
y = df["arr_delay"]

model = LinearRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model created")