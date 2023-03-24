print("Cześć! Witam w quizie Historia Polski!")
playing = input("Czy chcesz sprawdzić swoją wiedzę? ")
print(playing)

if playing != "Tak":
        quit()
print("Do dzieła!")
print("Pierwsze pytanie!")
pytanie =input (" 1. W którym roku odbył się Chrzest Polski?")
if pytanie == "966":
        print("Brawo!")
else:
        print("Błąd, spróbuj jeszcze raz")