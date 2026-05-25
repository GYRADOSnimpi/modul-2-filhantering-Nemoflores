# Gergoose
# TEI23A 
# 2026-05-15

# Läs från en .txt fil
# Skriv ett program som läser in från PythonPoem.txt och printar ut alla dess rader.
# Din kod nedan.

filePath = "uppg1_InputOutput_txt/PythonPoem.txt"


print("The poems")

try: 
    with open(filePath, "r", encoding='utf-8') as file: 
        for line in file:
            print(line.strip())

except FileNotFoundError: 
    print(f"Fel: Filen hittades inte på sökvägen: {filePath}")
except Exception as e: 
    print(f"Ett önväntat fel uppstod: {e}")

print("Klart")