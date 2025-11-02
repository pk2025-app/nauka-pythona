"""
2.1 LISTY - wprowadzenie
    Czym jest lista?
        # To jak pudełko na wiele wartości
        lista_zakupow = ["chleb", "mleko", "jajka"]
        liczby = [1, 2, 3, 4, 5]
        mieszana = ["tekst", 42, 3.14, True]
        
    Podstawowe operacje:
        # Tworzenie
            lista = [1, 2, 3]

        # Dodawanie
            lista.append(4)             # [1, 2, 3, 4]
            lista.insert(1, 1.5)        # [1, 1.5, 2, 3, 4]

        # Usuwanie
            lista.remove(1.5)           # [1, 2, 3, 4]
            element = lista.pop()       # [1, 2, 3], element = 4

        # Dostęp
            print(lista[0])             # 1 (pierwszy element)
            print(lista[-1])            # 3 (ostatni element)
"""

# ZADANIE 1: Lista zakupów

"""
Wejście: 5 produktów od użytkownika
Wyjście: Lista wszystkich produktów

Efekt:
    === LISTA ZAKUPÓW ===
    Dodaj produkt 1: chleb
    Dodaj produkt 2: mleko
    Dodaj produkt 3: jajka
    Dodaj produkt 4: masło
    Dodaj produkt 5: ser

    Twoja lista zakupów:
    1. chleb
    2. mleko
    3. jajka
    4. masło
    5. ser

🎯 PODPOWIEDŹ:
    Użyj pętli for z append() do dodawania do listy
"""

print("1: Lista zakupów")
print()

lista = []

for i in range (1, 6):
    lista.append(input(f"Wprowadz produkt nr. {i}: "))
    
print("\nTwoja lista zakupów:")
print("1.", lista[0])
print("2.", lista[1]) 
print("3.", lista[2])
print("4.", lista[3])
print("5.", lista[4])

# ZADANIE 2: Suma listy

"""
Wejście: 5 liczb od użytkownika
Wyjście: Suma i średnia liczb

Efekt:
    === SUMA I ŚREDNIA ===
    Podaj liczbę 1: 10
    Podaj liczbę 2: 20
    Podaj liczbę 3: 30
    Podaj liczbę 4: 40
    Podaj liczbę 5: 50

    Suma: 150
    Średnia: 30.0

🎯 PODPOWIEDŹ:
    Użyj sum(lista) i len(lista)
"""

print()
print("2: Suma listy")
print()

lista = []

for i in range (1, 6):
    liczba = int(input(f"Wprowadź liczbę nr: {i}: "))
    lista.append(liczba)

print(f"Suma: {sum(lista)}")
print(f"Średnia: {sum(lista) / len(lista)}")

# ZADANIE 3: Wyszukiwarka w liście

"""
Wejście: Lista imion + szukane imię
Wyjście: Czy imię jest na liście i na której pozycji

Efekt:
    === WYSZUKIWARKA IMION ===
    Lista: ['Anna', 'Jan', 'Maria', 'Piotr']
    Podaj imię do znalezienia: Maria
    Imię Maria znajduje się na pozycji 3

🎯 PODPOWIEDŹ:
    Użyj in do sprawdzenia czy element jest w liście i index() do znalezienia pozycji
"""

print()
print("3: Wyszukiwarka w liście")
print()

imie = ['Jagoda', 'Maria', 'Angelika', 'Paulina', 'Roksana', 'Monika', 'Agnieszka', 'Joanna', 'Katarzyna', 'Jadwiga']

imieSzukane = input("Podaj imie do znalezienia: ").capitalize()

if imieSzukane in imie:
    pozycja = imie.index(imieSzukane)
    print(f"Imie {imieSzukane} znajduje się na {pozycja + 1} miejscu.")
else:
    print(f"Imie {imieSzukane} nie znajduje się na liście.")

# ZADANIE 4: Sortowanie ocen

"""
Wejście: 6 ocen szkolnych
Wyjście: Posortowana lista ocen (rosnąco i malejąco)

Efekt:
    === SORTOWANIE OCEN ===
    Podaj ocenę 1: 4
    Podaj ocenę 2: 5
    Podaj ocenę 3: 3
    Podaj ocenę 4: 6
    Podaj ocenę 5: 4
    Podaj ocenę 6: 5

    Oceny rosnąco: [3, 4, 4, 5, 5, 6]
    Oceny malejąco: [6, 5, 5, 4, 4, 3]

🎯 PODPOWIEDŹ:
    Użyj sort() i sort(reverse=True)
"""

print()
print("4: Sortowanie ocen")
print()

print("Podaj 5 ocen: ")
oceny = []

for i in range (1, 6):
    ocena = int(input(f"{i}: "))
    oceny.append(ocena)


print()
print("Posortowane: ")

oceny.sort()
for i, ocenka in enumerate(oceny, 1):
    print(f"{i}: {ocenka}")
    
print()
print("Posortowane: (revers)")

oceny.sort(reverse=True)
for i, ocenka in enumerate(oceny, 1):
    print(f"{i}: {ocenka}")

# ZADANIE 5: Filtrowanie liczb

"""
Wejście: 8 liczb od użytkownika
Wyjście: Liczby parzyste i nieparzyste w osobnych listach

Efekt:
    === FILTROWANIE LICZB ===
    Podaj liczbę 1: 7
    Podaj liczbę 2: 2
    Podaj liczbę 3: 5
    Podaj liczbę 4: 8
    Podaj liczbę 5: 1
    Podaj liczbę 6: 4
    Podaj liczbę 7: 3
    Podaj liczbę 8: 6

    Liczby parzyste: [2, 4, 6, 8]
    Liczby nieparzyste: [1, 3, 5, 7]

🎯 PODPOWIEDŹ:
    Użyj % 2 == 0 do sprawdzenia parzystości i warunkowego dodawania do list
"""

print()
print("5: Filtrowanie liczb")
print()

print("Wprowadź 8 liczb: ")

liczby = []
parzyste = []
nieparzyste = []

for i in range (1, 9):
    liczba = int(input(f"{i}: "))
    liczby.append(liczba)

for i, liczba in enumerate(liczby, 1):
    if(liczba % 2 == 0):
        parzyste.append(liczba)
    else:
        nieparzyste.append(liczba)

print()

print("Wypisuje jedynie parzyste liczby:")
for i, parzysta in enumerate(parzyste, 1):
    print(f"{i}: {parzysta}")

print()

print("Wypisuje jedynie nieparzyste liczby:")
for i, nieparzysta in enumerate(nieparzyste, 1):
    print(f"{i}: {nieparzysta}")