import sys as system
system.stdout.write("Podaj liczbe całkowitą a: ")
a = system.stdin.readline()
a = int(a)
system.stdout.write("Podaj liczbe całkowitą b: ")
b = system.stdin.readline()
b = int(b)
system.stdout.write("Podaj liczbe całkowitą c: ")
c = system.stdin.readline()
c = int(c)
wynik = (a ** b)+c
wynik = str(wynik)
system.stdout.write(wynik)


