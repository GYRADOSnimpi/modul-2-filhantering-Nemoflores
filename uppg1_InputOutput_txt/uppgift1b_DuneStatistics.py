# Gergoose
# TEI23A
# 05/15/2026

# Statistik
# Skriv ett program som räknar antal bokstäver i filen DuneSummaryCH1.txt
#Template nedan:

statistics = {}
alfabet = "abcdefghijklmnopqrstuvwxyz"
filePath = "uppg1_InputOutput_txt/DuneSummaryCH1.txt"

# statistik["a"] = 0, lagra 0 med a som nyckel i dictionary
for letter in alfabet:
    statistics[letter] = 0


# TODO: DIN KOD HÄR

try: 
    with open(filePath, "r", encoding="utf-8") as file: 

        text = file.read().lower()

        for chart in text: 
            if chat in statistics: 
                statistics[chat] += 1

except FileNotFoundError: 
    print(f"Filen hittades inte")