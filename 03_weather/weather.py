import argparse
from simple_chalk import chalk
import requests
import pyfiglet

api_key = "xdM1sxyeGbyfC3XOlTR5ASYplv6TjDVI"
Base_URl = "https://api.tomorrow.io/v4"


#construct api url with query parameter
parser = argparse.ArgumentParser(description='Check the weather for a certain Country/city')
parser.add_argument("Location", help="The Place to check")
args = parser.parse_args()
url = f"https://api.tomorrow.io/v4/weather/realtime?location={args.Location}&apikey=xdM1sxyeGbyfC3XOlTR5ASYplv6TjDVI"
headers = {
    "accept": "application/json",
    "accept-encoding": "deflate, gzip, br"
}


#make Api request
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(chalk.red("Error: Unable to retrive weather information"))
    exit()
#parsing the JSON response form api and extract weather information


data = response.json()
# get information from api response
temperature = data["data"]["values"]["temperature"]
feels_like = data["data"]["values"]["temperatureApparent"]
altitude = data["data"]["values"]["altimeterSetting"]
#Construct output
output = f""
output += pyfiglet.figlet_format(args.Location)
output += f"Altitude: {altitude}"
output += f"Tempature: {temperature}c°"

print(output)