import requests
import pandas as pd

cities = {
    "Newcastle": (54.9783, -1.6178),
    "London": (51.5074, -0.1278),
    "Manchester": (53.4808, -2.2426),
    "Edinburgh": (55.9533, -3.1883)
}

all_data = []

for city, (lat, lon) in cities.items():

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max&forecast_days=7"

    response = requests.get(url)
    data = response.json()

    if "daily" not in data:
        print(f"Error for {city}:")
        print(data)
        continue

    dates = data["daily"]["time"]
    temps = data["daily"]["temperature_2m_max"]

    for date, temp in zip(dates, temps):
        all_data.append({
            "Date": date,
            "City": city,
            "MaxTemperature": temp
        })

df = pd.DataFrame(all_data)

df.to_csv("weather.csv", index=False)

print(df.head())
print("Multi-city weather file created!")










