import math

try:
    x = input("Podaj liczbę: ")
    print(math.sqrt(int(x)))

except ValueError:
    print("Negative.")