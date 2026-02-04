import os
import subprocess
import sys

#Setup Checker
current_directory = os.getcwd()

#Checker Packages

def run(cmd, **kwargs):
    subprocess.call(cmd,stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL, **kwargs)



req_file = os.path.join(current_directory, "requirements.txt")
if os.path.exists(req_file):
    print("Installing required packages globally...")
    run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], cwd=current_directory)
    run([sys.executable, "-m", "pip", "install", "-r", req_file], cwd=current_directory)
    print("All required packages are installed.\n")
else:
    print("No requirements.txt found — skipping package installation.\n")
    quit()

#Checker api keys
if not os.path.exists(os.path.join(current_directory,"requirements","apikey.py")):
    print("ApiKeys Missing")
    apikey_mail = input("Enter Mail Bearer token from Resend: ")
    email = input("Enter Email Address to send Mail from Resend: ")
    api_key_geo = input("Enter Geolocation API Key from Geoapify: ")
    api_key_weather = input("Enter Weather API Key: from OpenWeatherMap: ")
    edubase_username = input("Enter Edubase Username: ")
    edubase_password = input("Enter Edubase Password: ")
    gateway_username = input("Enter API Gateway Username: ")
    gateway_password = input("Enter API Gateway Password: ")
    requ = (f"apikey_mail = '{apikey_mail}'\n"
            f"email= '{email}'\n"
            f"api_key_geo = '{api_key_geo}'\n"
            f"api_key_weather = '{api_key_weather}'\n"
            f"edubase_username = '{edubase_username}'\n"
            f"edubase_password = '{edubase_password}'\n"
            f"GATEWAY_USERNAME = '{gateway_username}'\n"
            f"GATEWAY_PASSWORD = '{gateway_password}'")
    with open(os.path.join(current_directory,"requirements","apikey.py"),"x") as i:
        i.write(requ)
from requirements import apikey
from requirements.heartbeat import Heartbeat
import pyfiglet
import inquirer

# ── kill-switch heartbeat ───────────────────────────────────────────
# Disable "python-cli-tools" in /settings/software on the gateway to
# shut this CLI down remotely.
_heartbeat = Heartbeat("python-cli-tools", apikey.GATEWAY_USERNAME, apikey.GATEWAY_PASSWORD)
_heartbeat.start()


#Program
while True:

    if _heartbeat.killed.is_set():
        print("Shutting down — disabled on gateway.")
        exit()

    #Building Menu
    print(pyfiglet.figlet_format("Main-Menu"))
    choice = inquirer.list_input(message="Menu", choices=[
        "01|Sort Downloads Folder",
        "02|Edubase-Downloader",
        "03|Weather-Info",
        "04|Weather-Forcast",
        "05|Mailing",
        "06|Password-Manager",
        "07|Banking",
        "08|Annoying",
        "10|Exit"])

    #trigger For programs

    if choice == "01|Sort Downloads Folder":

        subprocess.run(["python","01_Main.py"], cwd="00_DownloadSorting")

    if choice == "02|Edubase-Downloader":
        subprocess.run(["python","edubasedl.py","-u", apikey.edubase_username, "-p", apikey.edubase_password], cwd="02_Edubase")
        input("Press ENTER to return to the menu...")

    if choice == "03|Weather-Info":
        subprocess.run(["python","01_weather.py"] ,cwd="03_weather")
        input("Press ENTER to return to the menu...")

    if choice == "04|Weather-Forcast":
        subprocess.run(["python","01_Forcast.py"] ,cwd="04_Forcast")
        input("Press ENTER to return to the menu...")

    if choice == "05|Mailing":
        subprocess.run(["python", "01_SendMail.py"], cwd="05_Mailing")
        input("Press ENTER to return to the menu...")

    if choice == "06|Password-Manager":

        subprocess.run(["python","01_Passwords.py"], cwd="06_Passwords")

    if choice == "07|Banking":
        subprocess.run(["python","01_Banking.py"], cwd="07_Banking")

    if choice == "08|Annoying":
        subprocess.run(["python", "01_Annoying.py"], cwd="08_Annoying")

    if choice == "10|Exit":
        print(f"Bye bye👋")
        exit()