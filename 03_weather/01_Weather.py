import argparse
from simple_chalk import chalk
import requests
import pyfiglet
import sys
import os

# Go to the project root folder
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# Now import from /requirements
from requirements import apikey
from requirements.gateway import GatewayClient
from yaspin import yaspin

# Initialize gateway client
gateway = GatewayClient(
    base_url=apikey.GATEWAY_URL,
    username=apikey.GATEWAY_USERNAME,
    password=apikey.GATEWAY_PASSWORD
)
#Settings
Toggle_Comments = 0
units = "metric"
#Start Program
print(pyfiglet.figlet_format("Weather-Info"))
Location = input("Enter the place to check\n")
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

#Making Geocoding API call via gateway
if Toggle_Comments == 1:
    print("Sending Geocoding API call via gateway")
try:
    data_geo = gateway.geocode(Location)
    longitude = data_geo["features"][0]["properties"]["lon"]
    latitude = data_geo["features"][0]["properties"]["lat"]
    if Toggle_Comments == 1:
        print(longitude, latitude)
except Exception as e:
    spinner.fail(chalk.red(f"Error: Unable to retrieve coordinates: {e}"))
    exit()

#Making Weather API call via gateway
if Toggle_Comments == 1:
    print("Sending weather API call via gateway")
try:
    # Use the gateway's convenience method for weather
    data_weather = gateway.get_weather(Location, units=units)
except Exception as e:
    spinner.fail(chalk.red(f"Error: Unable to retrieve weather information: {e}"))
    exit()


#Converting to output
icon = data_weather["weather"][0]["icon"]
weather_icon = Weather_icons_lib.get(icon, "")
description = data_weather["weather"][0]["description"]
country = data_weather["sys"]["country"]
temperature = data_weather["main"]["temp"]
feels_like = data_weather["main"]["feels_like"]
wind_speed = data_weather["wind"]["speed"]
wind_gust = data_weather["wind"].get("gust", "N/A")
spinner.ok()


#Constructing the output
output = f"{pyfiglet.figlet_format(Location)}"
output += f"({country}) Lat: {latitude} Lon: {longitude}\n\n"
output += f"{weather_icon}  {description}\n"
output += f"Temperature: {temperature}°C\n"
output += f"Feels Like: {feels_like}°C\n"
output += f"Wind Speed: {wind_speed} km/h\n"
output += f"Wind Gust: {wind_gust} km/h"

#Printing the Output
print(output)

