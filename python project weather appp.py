import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather?q=Delhi,ind&APPID=cd33d394766ecddd07d6bfae531b8358"
api_key = 'cd33d394766ecddd07d6bfae531b8358'

weather_params = {
    "lat": 28.704060,
    "lon": 77.102493,
    "appid": api_key,
    "cnt": 4,
}

# Making the API request
response = requests.get(OWM_Endpoint, params=weather_params)

# Checking if the request was successful
if response.status_code == 200:
    weather_data = response.json()
    print(weather_data)

    # Checking if it will rain
    will_rain = False
    for hour_data in weather_data.get("list", []):
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True
            break

    if will_rain:
        print("It's going to rain today, don't forget to bring an umbrella with you.")
    else:
        print("No rain expected in the next 4 hours.")
else:
    print(f"Failed to retrieve weather data. Status code: {response.status_code}")
