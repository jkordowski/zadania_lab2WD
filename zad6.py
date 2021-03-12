a = input("Podaj liczbę całkowitą a: ")
a = int(a)
b = input("Podaj liczbę całkowitą b: ")
b = int(b)
c = input("Podaj liczbę całkowitą c: ")
c = int(c)

if (a > b):
    if(a > c):
        print("Największa liczba =", a)
    else:
        print("Największa liczba =", c)
if (a < b):
    if(b > c):
        print("Największa liczba =", b)
    else:
        print("Największa liczba =", c)