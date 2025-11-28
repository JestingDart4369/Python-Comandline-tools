import argparse
from datetime import datetime
from simple_chalk import chalk
import requests
import pyfiglet
import sys
import os

# Go to the project root folder
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# Now import from /requirements
from requirements import apikeys

api_key_geo = apikeys.api_key_geo
api_key_weather = apikeys.api_key_weather
#Settings
Toggle_Comments = 0
units = "metric"
days = 7
i=1
#Forcast
default_url_weather = "https://api.openweathermap.org"
weather_icons_lib = {
    #Day icons
    "01d": "☀️",
    "02d": "⛅",
    "03d": "☁️",
    "04d": "☁️☁️",
    "09d": "🌧️",
    "10d": "🌦️",
    "11d": "🌩️",
    "13d": "🌨️",
    "50d": "🌫️",
    #Night Icons
    "01n": "🌙",
    "02n": "🌙☁️",
    "03n": "☁️",
    "04n": "☁️☁️",
    "09n": "🌧️",
    "10n": "🌙🌧️",
    "11n": "🌩️",
    "13n": "🌨️",
    "50n": "🌫️",

}

#Constructing Geolocation api call
if Toggle_Comments == 1 :
    print("Constructing Geolocation Api Call")
parser = argparse.ArgumentParser(description='Check the weather for a certain Country/city')
parser.add_argument("Location", help="The Place to check")
args = parser.parse_args()
url_geo = f"https://api.geoapify.com/v1/geocode/search?text={args.Location}&apiKey={api_key_geo}"
headers = {
    "accept": "application/json",
    "accept-encoding": "deflate, gzip, br"
}

#Making Api Call geo
if Toggle_Comments == 1 :
    print("Sending Geolocation Api Call")
response_geo = requests.get(url_geo, headers=headers)
if response_geo.status_code != 200:
    print(chalk.red("Error: Unable to retrieve Coordinates information"))
    exit()

#Converting longitude and latitude
data_geo = response_geo.json()
longitude = data_geo["features"][0]["properties"]["lon"]
latitude = data_geo["features"][0]["properties"]["lat"]
if Toggle_Comments == 1 :
    print(longitude,latitude)

#Constructing Weather forcast api call
if Toggle_Comments == 1 :
    print("Constructing weather api call")
url_weather= f"{default_url_weather}/data/2.5/forecast/daily?lat={latitude}&lon={longitude}&cnd={days}&appid={api_key_weather}&units={units}"
headers = {
    "accept": "application/json",
    "accept-encoding": "deflate, gzip, br"
}
#Making Weather api call
if Toggle_Comments == 1 :
    print("Sending weather api call")
response_weather = requests.get(url_weather, headers=headers)
if response_weather.status_code != 200:
    print(chalk.red("Error: Unable to retrieve weather information"))
    exit()

#parsing to json
data_weather = response_weather.json()

#formating to output
if Toggle_Comments == 1 :
    print("Building Output Main")
country = data_weather["city"]["country"]
output = f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
output += f"{pyfiglet.figlet_format(args.Location)}"
output += f"({country}) Lat: {latitude} Lon: {longitude}\n\n"


#adding forcast for each day
while i < days:
    if Toggle_Comments == 1:
        print(f"Building Forcast day {i-1}")
    #Loop for forcast days
    i = i+1
    icon = data_weather["list"][i-1]["weather"][0]["icon"]
    weather_icon = weather_icons_lib.get(icon, "")
    description = data_weather["list"][i - 1]["weather"][0]["description"]
    temperature = data_weather["list"][i - 1]["temp"]["day"]
    feels_like = data_weather["list"][i-1]["feels_like"]["day"]
    wind_speed = data_weather["list"][i-1]["speed"]
    wind_gust = data_weather["list"][i-1].get("gust", "N/A")
    unix_time = data_weather["list"][i-1]["dt"]
    #constructing output
    date = datetime.fromtimestamp(unix_time).strftime('%d-%m-%Y')
    output += f"{weather_icon}  | {description} | {date}\n"
    output += f"Temperature: {temperature}°C\n"
    output += f"Feels Like: {feels_like}°C\n"
    output += f"Wind Speed: {wind_speed} km/h\n"
    output += f"Wind Gust: {wind_gust} km/h\n\n"

print(output)