import pandas as pd
import numpy as np

# 1. Simulate global climate anomalies dataset
np.random.seed(10)
years = list(range(2000, 2026))
temperature_anomalies = np.random.uniform(0.4, 1.2, size=len(years))

df = pd.DataFrame({
    "Year": years,
    "Global_Anomaly_Celsius": np.round(temperature_anomalies, 2)
})

# 2. Compute key analytical baseline metrics
average_anomaly = df["Global_Anomaly_Celsius"].mean()
max_anomaly_year = df.loc[df["Global_Anomaly_Celsius"].idxmax(), "Year"]

print("--- Climate Analytics Brief ---")
print(f"Dataset tracked records across {len(df)} calendar years.")
print(f"Mean Global Temperature Anomaly: {average_anomaly:.2f} C")
print(f"Peak global anomaly recorded in the year: {max_anomaly_year}")

# 3. Save raw output dataset
df.to_csv("climate_data.csv", index=False)
