"""
Wejście: 10 liczb od użytkownika
Wyjście: Unikalne liczby

Efekt:
    === UNIKALNE LICZBY ===
    Podaj liczbę 1: 5
    Podaj liczbę 2: 3
    [...]
    Podaj liczbę 10: 5
    Unikalne liczby: {2, 3, 5, 7, 8}

🎯 PODPOWIEDŹ:
    Zbierz liczby do listy, potem konwertuj na set
"""

print()
print("3: Unikalne liczby")
print()

print("Wprowadź 10 liczb:")

for i in range (1, 11):
    liczby = set(input(f"{i}: "))

print()
print("Unikalne liczby: ")
for liczba in liczby:
    print(liczba)