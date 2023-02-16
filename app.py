import sys
from api_key import api_key
import requests

try:
    city_name = sys.argv[1]
except IndexError:
    city_name = input("Enter city name: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial")

if weather_data.status_code != 200:
    print(f"Unable to find weather information for {city_name}.")
else:
    weather_json = weather_data.json()

    descrip = weather_json['weather'][0]['main']
    temp = round(weather_json['main']['temp'])

    print(f"The weather in {city_name} is {descrip} with a temperature of {temp}°F.")