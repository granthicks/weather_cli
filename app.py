from api_key import api_key
import requests

city_name = input("Enter city name: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial")

weather_json = weather_data.json()

descrip = weather_json['weather'][0]['main']
temp = weather_json['main']['temp']

print(f"The weather in {city_name} is {descrip} with a temperature of {temp}F.")