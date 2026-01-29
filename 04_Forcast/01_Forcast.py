#Requirements
from datetime import datetime
from simple_chalk import chalk
import requests
import pyfiglet
import sys
import os
from yaspin import yaspin

# Go to the project root folder
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# Now import from /requirements
from requirements import apikey
from requirements.gateway import GatewayClient

# Initialize gateway client
gateway = GatewayClient(
    base_url=apikey.GATEWAY_URL,
    username=apikey.GATEWAY_USERNAME,
    password=apikey.GATEWAY_PASSWORD
)
#Settings
Toggle_Comments = 0
units = "metric"
days = 7
i=1
#Forcast
#Start Program
print(pyfiglet.figlet_format("Weather-Forcast"))
Location = input("Enter the place to check\n")

#Spinner
spinner = yaspin(text="Getting Weather Data",color="yellow")
spinner.start()
#Code
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


#Geoplocation via gateway
try:
    data_geo = gateway.geocode(Location)
    longitude = data_geo["features"][0]["properties"]["lon"]
    latitude = data_geo["features"][0]["properties"]["lat"]
except Exception as e:
    spinner.fail(chalk.red(f"Error: Unable to retrieve coordinates: {e}"))
    exit()


#Weather forecast via gateway
try:
    data_weather = gateway.get_daily_forecast(latitude, longitude, days=days, units=units)
except Exception as e:
    spinner.fail(chalk.red(f"Error: Unable to retrieve weather forecast: {e}"))
    exit()


#Building Output

#formating to output
if Toggle_Comments == 1 :
    print("Building Output Main")
country = data_weather["city"]["country"]
output = f"{pyfiglet.figlet_format(Location)}"
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

#Printing Output
spinner.ok()
print(output)