# import requests
# import pandas as pd
# import time

# # Replace with your WAQI API token
# API_TOKEN = "6ac550e437d98d75957d3a37e85d8274e6a4e604"

# # Function to fetch air quality data for a specific city
# def fetch_air_quality(city):
#     base_url = f"https://api.waqi.info/feed/{city}/?token={API_TOKEN}"
#     response = requests.get(base_url)
#     if response.status_code == 200:
#         data = response.json()
#         if data.get("status") == "ok":
#             return {
#                 "city": city,
#                 "aqi": data["data"].get("aqi"),
#                 "pm25": data["data"]["iaqi"].get("pm25", {}).get("v"),
#                 "pm10": data["data"]["iaqi"].get("pm10", {}).get("v"),
#                 "no2": data["data"]["iaqi"].get("no2", {}).get("v"),
#                 "so2": data["data"]["iaqi"].get("so2", {}).get("v"),
#                 "co": data["data"]["iaqi"].get("co", {}).get("v"),
#                 "ozone": data["data"]["iaqi"].get("o3", {}).get("v"),
#                 "time": data["data"].get("time", {}).get("s"),
#             }
#     return None

# # Function to fetch data for multiple cities
# def fetch_multiple_cities(cities):
#     results = []
#     for city in cities:
#         print(f"Fetching data for {city}...")
#         data = fetch_air_quality(city)
#         if data:
#             results.append(data)
#         time.sleep(1)  # Respect API rate limits
#     return pd.DataFrame(results)

# # Example usage
# if __name__ == "__main__":
#     cities = ["Delhi", "Los Angeles", "Beijing", "London"]
#     data = fetch_multiple_cities(cities)
#     data.to_csv("data/real_time_air_quality.csv", index=False)
#     print("Data saved to 'data/real_time_air_quality.csv'.")


import requests
import pandas as pd

API_TOKEN = "6ac550e437d98d75957d3a37e85d8274e6a4e604"

def fetch_city_data(city):
    url = f"https://api.waqi.info/feed/{city}/?token={API_TOKEN}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'ok':
            aqi_data = {
                "city": [data['data']['city']['name']],
                "aqi": [data['data']['aqi']],
                "pm25": [data['data']['iaqi']['pm25']['v'] if 'pm25' in data['data']['iaqi'] else None],
                "pm10": [data['data']['iaqi']['pm10']['v'] if 'pm10' in data['data']['iaqi'] else None],
                "co": [data['data']['iaqi']['co']['v'] if 'co' in data['data']['iaqi'] else None],
                "so2": [data['data']['iaqi']['so2']['v'] if 'so2' in data['data']['iaqi'] else None],
                "no2": [data['data']['iaqi']['no2']['v'] if 'no2' in data['data']['iaqi'] else None],
                "datetime": [data['data']['time']['s']],
            }
            return pd.DataFrame(aqi_data)
    return None

