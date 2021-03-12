napis = input("Podaj zdanie: ")
licznik = 0
print(napis)

for x in napis:
    if(x == "a") | (x == "A"):
        licznik += 1

print(licznik)