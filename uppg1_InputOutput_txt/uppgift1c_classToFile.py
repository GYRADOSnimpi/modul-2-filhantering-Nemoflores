# Gergoose
# TEI23A
# 05/15/2026


class Character: # klass med olika objekt med attributen name, house och planet. 
    def __init__(self, name: str, house: str, planet: str) -> None: # 
        self.name = name
        self.house = house 
        self.planet = planet

    def __str__(self) -> str:
        return f"Character: {self.name}, House:{self.house} Planet: {self.planet}"


    def writeFile(info) -> None: 
        filePath = "uppg1_InputOutput_txt/SavedCharacter.txt"

        try: 
            with open(filePath, "a", encoding="utf-8") as file:
                file.write(str(info) + "\n")

            print("Informationen har sparats")

        except Exception as e:
            print(f"Ett fel uppstod: {e}")

    def main():
        character_object = Character("Paul Atreides", "House Atreides", "Caladan")

        WriteToFile(character_object)


    main()

    
                      