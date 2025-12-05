import os
import subprocess
import pyfiglet
current_directory = os.getcwd()
if not os.path.exists(os.path.join(current_directory,"requirements","apikeys.py")):
    print("ApiKeys Missing")
    apikey_mail = input("Enter Mail Bearer token from Resend: ")
    email = input("Enter Email Address to send Mail from Resend: ")
    api_key_geo = input("Enter Geolocation API Key from Geoapify: ")
    api_key_weather = input("Enter Weather API Key: from OpenWeatherMap: ")
    edubase_username = input("Enter Edubase Username: ")
    edubase_password = input("Enter Edubase Password: ")
    requ = (f"apikey_mail = '{apikey_mail}'\n"
            f"email= '{email}'\n"
            f"api_key_geo = '{api_key_geo}'\n"
            f"api_key_weather = '{api_key_weather}'\n"
            f"edubase_username = '{edubase_username}'\n"
            f"edubase_password = '{edubase_password}'")
    with open(os.path.join(current_directory,"requirements","apikeys.py"),"x") as i:
        i.write(requ)
from requirements import apikeys
import inquirer
exit_Button = False
choice = 0


#Program
while not exit_Button:

    #Building Menu
    choice = inquirer.list_input(message=f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{pyfiglet.figlet_format('Menu')}\n\n', choices=[
        "01|Sort Downloads Folder",
        "02|Edubase-Downloader",
        "03|Weather-Info",
        "04|Weather-Forcast",
        "05|Mailing",
        "06|Passwords",
        "07|Banking",
        "10|Exit"])

    #trigger For programs

    if choice == "01|Sort Downloads Folder":
        subprocess.run(["python","01_DownloadSorter.py"], cwd="00_DownloadSorting")

    if choice == "02|Edubase-Downloader":
        subprocess.run(["python","edubasedl.py","-u", apikeys.edubase_username, "-p", apikeys.edubase_password], cwd="02_Edubase")
        input("\nPress ENTER to return to the menu...")

    if choice == "03|Weather-Info":
        place= input("Enter the place to check: ")
        subprocess.run(["python","01_weather.py",place] ,cwd="03_weather")
        input("\nPress ENTER to return to the menu...")

    if choice == "04|Weather-Forcast":
        place= input("Enter the place to check: ")
        subprocess.run(["python","01_Forcast.py",place] ,cwd="04_Forcast")
        input("\nPress ENTER to return to the menu...")

    if choice == "05|Mailing":
        subprocess.run(["python", "01_SendMail.py"], cwd="05_Mailing")
        input("\nPress ENTER to return to the menu...")

    if choice == "06|Passwords":
        subprocess.run(["python","01_Passwords.py"], cwd="06_Passwords")

    if choice == "07|Banking":
        subprocess.run(["python","01_Banking.py"], cwd="07_Banking")

    if choice == "10|Exit":
        exit_Button = True
print(f"Bye bye👋")