lista = []
licznik = 0
while licznik != 10:
    x = input("Podaj liczbę: ")
    if (int(x) % 2 == 0):
        lista.append(x)
    licznik += 1
else:
    print(lista)