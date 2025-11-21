import subprocess
import pyfiglet
from Edubase_Login import *
import inquirer
exit_Button = False
choice = 0


#Program
while not exit_Button:

    #Building Menu
    choice = inquirer.list_input(message=f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{pyfiglet.figlet_format('Menu')}\n\n', choices=[
        "01|Infos",
        "02|Edubase-Downloader",
        "03|Weather-Info",
        "04|Weather-Forcast",
        "05|Mailing",
        "06|Passwords",
        "07|Banking",
        "08|Quiz",
        "10|Exit"])

    #trigger For programs
    if choice == "02|Edubase-Downloader":
        subprocess.run(["python","edubasedl.py","-u",edubase_username,"-p",edubase_password] ,cwd="02_Edubase")
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

    if choice == "08|Quiz":
        subprocess.run(["python","main.py"], cwd="08_Quiz/Program")

    if choice == "10|Exit":
        exit_Button = True
print(f"Bye bye👋")