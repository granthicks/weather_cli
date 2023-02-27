import sys
from api_key import api_key
import requests

def get_location_name():
    """Obtains name of location to look up weather info"""
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        city_name = input("Enter city name: ")
        return city_name

def get_json_data(location, api_key=api_key):
    """Looks up weather information for the city and returns json data"""
    status = False
    tries = 0

    while not status:
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial")

        if weather_data.status_code != 200 and tries < 3:
            print(f"Unable to find weather information for {location}.")
            tries += 1
            location = input("Enter a city name: ")
        elif tries == 3:
            print("Try again later.")
            quit()
        else:
            status = True

    return (location, weather_data.json())

def weather_report(city_name, weather_json):
    """Prepares the weather report printout string"""
    descrip = weather_json['weather'][0]['main']
    temp = round(weather_json['main']['temp'])
    return f"The weather in {city_name} is {descrip} with a temperature of {temp}°F."


def run():
    location_name = get_location_name()

    # Gets location name again in case argv was passed and was unfindable
    # Otherwise report includes the undindable name
    location_name, weather_data = get_json_data(location_name)

    report = weather_report(location_name, weather_data)

    print(report)


if __name__ == '__main__':
    run()