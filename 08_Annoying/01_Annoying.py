import time
import ctypes
import pyfiglet
import inquirer
from pynput.mouse import Controller,Button
from pynput.keyboard import Key, Controller as Control
mouse = Controller()
keyboard = Control()
scale_factor = ctypes.windll.shcore.GetScaleFactorForDevice(0)/100
def question():
    person = input("who do you want to send the message to\n")
    message = input("What do you want to type\n")
    repetition = input("How many times do you want to type\n")
    number = input("Do you want it numbered\n")
    if number.lower() == "yes" :
        numbered = True
    else:
        numbered = False
    return [message,repetition,numbered, person]

def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def texting(message,repetitions,numbering,person):
    time.sleep(5)
    #select chat
    mouse.position = (406/scale_factor,170/scale_factor)
    time.sleep(2)
    mouse.press(Button.left)
    mouse.release(Button.left)
    keyboard.type(person)
    time.sleep(2)
    mouse.position = (437/scale_factor, 239/scale_factor)
    time.sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(1)
    #writes messages in a selected chat
    mouse.position = (985/scale_factor, 1095/scale_factor)
    mouse.press(Button.left)
    mouse.release(Button.left)
    i = 0
    while not i >= int(repetitions):
        i = i + 1
        if numbering == True:
            keyboard.type(
                message + " " + str(i))
            enter()
        else:
            keyboard.type(
                message)
            enter()
        time.sleep(0.25)

#main loop of the program
while True:
    print(pyfiglet.figlet_format("Annoying"))
    choice = inquirer.list_input(message=f'Annoying-Tools-Menu',
                                 choices=[
                                     "01|Spamming Whatsapp",
                                     "10|Exit"])
    if choice == "01|Spamming Whatsapp":
        if scale_factor == 1.5:
            quest = question()
            texting(quest[0], quest[1], quest[2],quest[3])
        else:
            print("Wrong Resolution exiting program")
            exit()
    if choice == "10|Exit":
        exit()