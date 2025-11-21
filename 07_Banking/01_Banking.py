import csv
import os
import inquirer
import pyfiglet
kontoauszug_file = ""
def kontoauszug_laden():
    #Loads a Kontoauszug
    #Cantonal Bank Csv
        #buchung        |0
        #valuta         |1
        #Buchungstext   |2
        #belastung      |3
        #Gutschrift     |4
        #saldo          |5
    base_dir = "./02_Bankauszüge"
    gesamt_ausgaben = 0.0
    kontoauszug = inquirer.list_input(
        "Bitte wählen Sie ein Kontoauszug aus:",
        choices=os.listdir(base_dir))
    global kontoauszug_file
    kontoauszug_file = f"{base_dir}/{kontoauszug}"

def kontoauszug_money_spent():
    #calculates all money spent
    cost = 0.0
    with open(kontoauszug_file,"r") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        next(csv_reader)
        for line in csv_reader:
            line[3] = line[3].replace("'", "")
            try:
                cost += float(line[3])
            except ValueError:
                cost += float(0)
    return cost

def kontoauszug_money_received():
    #calculates all money Received to bank conto
    received = 0.0
    with open(kontoauszug_file,"r") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        next(csv_reader)
        for line in csv_reader:
            line[4] = line[4].replace("'", "")
            try:
                received += float(line[4])
            except ValueError:
                received += float(0)
    return received
def bankkontoauszug():
    kontoauszug_laden()
    spent_money = kontoauszug_money_spent()
    received = kontoauszug_money_received()
    current_konto_summ = received - spent_money
    print(pyfiglet.figlet_format('Kontoauszug'))
    print("\n")
    with open(kontoauszug_file,"r") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        next(csv_reader)
        for line in csv_reader:
            print(line)
    print(f"\nAusgegeben| {spent_money} Bekommen| {received}\n"
               f"Kontosumme| {current_konto_summ}\n")

while True:
    function_choice = inquirer.list_input(message="Finanzen Menu",
                                          choices=[
                                     "01|Bankkontoauszug",
                                     "10|Exit"])
    if function_choice == "01|Bankkontoauszug":
        bankkontoauszug()
        input("\nPress ENTER to return to the menu...")

    if function_choice == "10|Exit":
        break
