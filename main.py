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

#Checker config
if not os.path.exists(os.path.join(current_directory,"requirements","config.py")):
    print("Configuration missing — fill in your details:")
    gateway_username = input("  Gateway username: ")
    gateway_password = input("  Gateway password: ")
    email_from       = input("  Email sender address: ")
    edubase_username = input("  Edubase username: ")
    edubase_password = input("  Edubase password: ")
    requ = (f'GATEWAY_URL      = "https://api.novaroma-homelab.uk"\n'
            f'GATEWAY_USERNAME = "{gateway_username}"\n'
            f'GATEWAY_PASSWORD = "{gateway_password}"\n'
            f'EMAIL_FROM       = "{email_from}"\n'
            f'EDUBASE_USERNAME = "{edubase_username}"\n'
            f'EDUBASE_PASSWORD = "{edubase_password}"\n')
    with open(os.path.join(current_directory,"requirements","config.py"),"x") as f:
        f.write(requ)
from requirements import config
from requirements.gateway import GatewayClient
from requirements.heartbeat import Heartbeat
import pyfiglet
import inquirer

# ── kill-switch heartbeat ───────────────────────────────────────────
# Disable "python-cli-tools" in /settings/software on the gateway to
# shut this CLI down remotely.
_gw = GatewayClient(config.GATEWAY_URL, config.GATEWAY_USERNAME, config.GATEWAY_PASSWORD)
_heartbeat = Heartbeat(_gw, kind="software", name="python-cli-tools")
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
        subprocess.run(["python","edubasedl.py","-u", config.EDUBASE_USERNAME, "-p", config.EDUBASE_PASSWORD], cwd="02_Edubase")
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