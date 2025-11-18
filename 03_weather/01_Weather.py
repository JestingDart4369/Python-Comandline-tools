import argparse
from simple_chalk import chalk
import requests
import pyfiglet
from apikey import *
import time
from yaspin import yaspin
#Settings
Toggle_Coments = 0
units = "metric"

#Self configuration

#api_key_geo = "xxxxx"
#api_key_weather ="xxxxxx"

#Spinner
spinner = yaspin(text="Getting Weather Data",color="yellow")
spinner.start()

#Forcast
default_url_weather = "https://api.openweathermap.org"
Weather_icons_lib = {
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

#construct Geolocation api call
if Toggle_Coments == 1 :
    print("Constructing Geolocation Api Call")
parser = argparse.ArgumentParser(description='Check the weather for a certain Country/city')
parser.add_argument("Location", help="The Place to check")
args = parser.parse_args()
url_geo = f"https://api.geoapify.com/v1/geocode/search?text={args.Location}&apiKey={api_key_geo}"
headers = {
    "accept": "application/json",
    "accept-encoding": "deflate, gzip, br"
}

#makeing geo Api Call
if Toggle_Coments == 1 :
    print("Sending Geolocation Api Call")
response_geo = requests.get(url_geo, headers=headers)
if response_geo.status_code != 200:
    print(chalk.red("Error: Unable to retrive Coordinates information"))
    exit()

#Converting longitude and latitude
data_geo = response_geo.json()
longitude = data_geo["features"][0]["properties"]["lon"]
latitude = data_geo["features"][0]["properties"]["lat"]
if Toggle_Coments == 1 :
    print(longitude,latitude)

#Constructing whether api call
if Toggle_Coments == 1 :
    print("Constructing wheather api call")
url_wheather= f"{default_url_weather}/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key_weather}&units={units}"
headers = {
    "accept": "application/json",
    "accept-encoding": "deflate, gzip, br"
}
#Making Weather api call
if Toggle_Coments == 1 :
    print("Sending wheather api call")
response_wheater = requests.get(url_wheather, headers=headers)
if response_wheater.status_code != 200:
    print(chalk.red("Error: Unable to retrive weather information"))
    exit()
#parsing to json
data_weather = response_wheater.json()

#Converting to output"
icon = data_weather["weather"][0]["icon"]
weather_icon = Weather_icons_lib.get(icon, "")
discription = data_weather["weather"][0]["description"]
country = data_weather["sys"]["country"]
tempature = data_weather["main"]["temp"]
feels_like = data_weather["main"]["feels_like"]
wind_speed = data_weather["wind"]["speed"]
wind_gust = data_weather["wind"].get("gust", "N/A")
spinner.ok()
#Constructing the output
output = f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
output += f"{pyfiglet.figlet_format(args.Location)}"
output += f"({country}) Lat: {latitude} Lon: {longitude}\n\n"
output += f"{weather_icon}  {discription}\n"
output += f"Temperature: {tempature}°C\n"
output += f"Feels Like: {feels_like}°C\n"
output += f"Wind Speed: {wind_speed} km/h\n"
output += f"Wind Gust: {wind_gust} km/h"

#Printing the Output
print(output)

