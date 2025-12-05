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

api_key_geo = apikey.api_key_geo
api_key_weather = apikey.api_key_weather
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


#Geoplocation

#Constructing Api Call
url_geo = f"https://api.geoapify.com/v1/geocode/search?text={Location}&apiKey={api_key_geo}"
headers = {
    "accept": "application/json",
    "accept-encoding": "deflate, gzip, br"
}

#Calling Geo Api
response_geo = requests.get(url_geo, headers=headers)
if response_geo.status_code != 200:
    print(chalk.red("Error: Unable to retrieve Coordinates information"))
    exit()


#Converting longitude and latitude
data_geo = response_geo.json()
longitude = data_geo["features"][0]["properties"]["lon"]
latitude = data_geo["features"][0]["properties"]["lat"]


#Weather

#Constructing Api Call
url_weather= f"{default_url_weather}/data/2.5/forecast/daily?lat={latitude}&lon={longitude}&cnd={days}&appid={api_key_weather}&units={units}"
headers = {
    "accept": "application/json",
    "accept-encoding": "deflate, gzip, br"
}

#Calling Weather Api
response_weather = requests.get(url_weather, headers=headers)
if response_weather.status_code != 200:
    print(chalk.red("Error: Unable to retrieve weather information"))
    exit()


#parsing to json
data_weather = response_weather.json()


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