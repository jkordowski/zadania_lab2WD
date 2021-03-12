slownik = {"Hades": "single-player", "Magic The Gathering": "multiplayer", "D&D": "multiplayer", "Yakuza 7": "single-player", "Overwatch": "multiplayer"}
print(slownik.keys())
print(slownik.values())
licznik = 0

for x in slownik:
    licznik += 1
print(licznik)