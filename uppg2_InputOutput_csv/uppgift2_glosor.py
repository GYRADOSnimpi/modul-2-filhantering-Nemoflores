# Gergoose
# TEI23A
# 2026-05-15
# Glos-förhör: läs instruktioner i filen: glosor.md
# Fixa funktionerna som har kommentaren TODO!


import csv 
import random 
import os


def readCSV(path: str) -> dict: 
    glosor = {}


    if not os.path.exists(path):
        path = path.replace("glosor_SW_FIN.csv", "glosor_SW_FIN-csv")

        try: 
            with open(path, "r", encoding="uft-8") as file: 
                reader = csv.reader.file
                next(reader)
                for row in reader: 
                    if len(row) == 2:
                        glosor[row[0].strip()] = row[1].strip()
        except FileNotFoundError: 
            print(f"Filen inte: {path}")

            return glosor 
        
    def printGlosor (glosor: dict) -> None: 
        if not glosor:
            print("Inga glosor laddade.")
            return
        
        print("Glosförhör, skriv exit för att avsluta")

        points = 0 
        wrong_answers = []

        while True: 
            question = random.choice(list(glosor.keys()))
            answer = input(f"{questions}:").strip()

            if answer.lower() == "exit": 
                break 


            if answer.lower() == glosor[question].lower():
                points += 1 
            else: 
                print(f"{answer} är fel, -1 poäng")
                points -= 1
                if question not in wrong_answers: 
                    wrong_answers.append(question) 
        wrong_str = "".join([word + ", " for word in wrong_asnwers])
        print(f"Provet avklarat, dina poäng: {points}, fel svar: {wrong_str}")
    def main():
        filePath = "uppg2_InputOutput_csv/glosor_SW_FIN.csv"
        glosor = readCSV(filePath)

        while True: 
            print("Det ulitimata glosförhöret")
            print("1. Lista")
            print("2. Kör provet")
            print("3. Avlsuta")

            if userInput == "1":
                printGlosor(glosor)
            elif userInput == "2":
                doTest(glosor)
            elif userInput == "3":
                print("Avlutar")
                break 

    main()                   
