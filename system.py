print("[SYSTEM] Weather Hunter Protocol Initiated.")

#city = input("Enter city name: ")
#print(f"Fetching weather for: {city}")

import requests
import os

fav_file = "favorite.txt"

if os.path.exists(fav_file):
    with open(fav_file, "r") as f:
        city = f.read().strip()
    print(f"[SYSTEM] Using saved city: {city}")
else:
    city = input("Enter city name: ")
    with open(fav_file, "w") as f:
        f.write(city)
    print(f"[SYSTEM] Saved '{city}' for next time.")

with open(".env") as f:
    API_KEY = f.read().strip().split("=")[1]
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f"Weather in {city}:{temp}°C, {desc}")
else:
    print("❌ Error: City not found or invalid API key")
