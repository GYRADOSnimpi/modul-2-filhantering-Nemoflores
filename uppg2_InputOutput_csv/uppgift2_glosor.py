# Ditt namn
# Din klass
# Datum
# Glos-förhör: läs instruktioner i filen: glosor.md
# Fixa funktionerna som har kommentaren TODO!


import csv, random


def readCSV(path:str) -> dict:
    # TODO: Ska läsa csv-filen, gå igenom den och spara glosorna i en dictionary
    # glosor = {svenska: finska}, svenska = key, finska = value
    pass


def printGlosor(glosor:dict) -> str:
    for key in glosor:
        print(key.ljust(20) + glosor[key])


def doTest(glosor:dict) -> None:
    #TODO: en funktion för testet
    print("Välkommen till glosförhör, skriv 'exit' för tt avsluta när som helst")

    while True:
        question = random.choice(list(glosor.keys())) # Väljer ett random svenskt ord från gloslistan
        answer = input(f"{question}: ")
        pass


def main():
    filePath = "Programmering2-Module2-Template\uppg2_InputOutput_csv\glosor_SW_FIN.csv"
    glosor = readCSV(filePath)

    while True:
        #TODO: meny
        userInput = input("")
        if userInput == "1":
            printGlosor(glosor)
            pass
        elif userInput == "2":
            pass
        elif userInput == "3":
            pass

main()

# Klistra in din testutskrift nedan:
