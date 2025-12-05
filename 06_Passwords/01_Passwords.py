import inquirer
import pyfiglet
from simple_chalk.src.utils import whenTruthy
from cryptography.fernet import Fernet
import os
# Setup Checker
current_directory = os.getcwd()
if not os.path.exists(os.path.join(current_directory,"key.key")):
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


#Main Program
def load_key():
    file = open("key.key", "rb")
    key_load = file.read()
    file.close()
    return key_load


key = load_key()
fer = Fernet(key)


def add():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("02_Password_collection", "a") as f:
        f.write(fer.encrypt(username.encode()).decode()+"|"+fer.encrypt(password.encode()).decode()+"\n")
def read():
    with open("02_Password_collection", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print(f"{fer.decrypt(user.encode()).decode()}|{fer.decrypt(pwd.encode()).decode()}\n")
    whenTruthy(input("Press enter to continue... "))
while True:
    print(pyfiglet.figlet_format("Password-\nManager"))
    choice = inquirer.list_input(message=f'Password-Manager Menu', choices=["01|Add Password", "02|View Passwords","03|Exit"])
    if choice == "01|Add Password":
        add()
    if choice == "02|View Passwords":
        read()
    if choice == "03|Exit":
        break