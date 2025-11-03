"""
SLICING I LIST COMPREHENSIONS W LISTACH

    SLICING (WYCINANIE FRAGMENTÓW LIST)

        Slicing to wycinanie fragmentów listy używając składni: lista[start:stop:step]

        SKŁADNIA:
        
            lista[start]                # pojedynczy element na pozycji start
            lista[start:stop]           # elementy od start do stop-1
            lista[start:stop:step]      # elementy od start do stop-1 co step
            lista[:stop]                # od początku do stop-1  
            lista[start:]               # od start do końca
            lista[::step]               # cała lista co step
            lista[::-1]                 # odwrócona lista

        PRZYKŁADY:
        
            lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

            print(lista[2:5])               # [2, 3, 4]                         - od indeksu 2 do 4
            print(lista[:5])                # [0, 1, 2, 3, 4]                   - pierwsze 5 elementów
            print(lista[5:])                # [5, 6, 7, 8, 9]                   - od indeksu 5 do końca
            print(lista[::2])               # [0, 2, 4, 6, 8]                   - co drugi element
            print(lista[::-1])              # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]    - odwrócona lista
            print(lista[-3:])               # [7, 8, 9]                         - ostatnie 3 elementy
            print(lista[:-3])               # [0, 1, 2, 3, 4, 5, 6]             - wszystko oprócz ostatnich 3

LIST COMPREHENSIONS (WYRAŻENIA LISTOWE)

    To zwięzły sposób tworzenia list w jednej linijce używając pętli for i warunków.

    SKŁADNIA:
        [wyrażenie for element in sekwencja]                                # podstawowa
        [wyrażenie for element in sekwencja if warunek]                     # z filtrowaniem
        [wyrażenie if warunek else wyrażenie2 for element in sekwencja]     # z warunkiem

    PRZYKŁADY:
    
        # Tworzenie listy kwadratów liczb
            kwadraty = [x**2 for x in range(1, 6)]
            print(kwadraty)  # [1, 4, 9, 16, 25]

        # Tylko parzyste liczby
            parzyste = [x for x in range(10) if x % 2 == 0]
            print(parzyste)  # [0, 2, 4, 6, 8]

        # Zamiana na duże litery
            imiona = ["anna", "jan", "maria"]
            duze_litery = [imie.upper() for imie in imiona]
            print(duze_litery)  # ["ANNA", "JAN", "MARIA"]

        # Z warunkiem if/else
            liczby = [1, 2, 3, 4, 5]
            parzystosc = ["parzysta" if x % 2 == 0 else "nieparzysta" for x in liczby]
            print(parzystosc)  # ["nieparzysta", "parzysta", "nieparzysta", "parzysta", "nieparzysta"]

        # Pętla zagnieżdżona
            kombinacje = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
            print(kombinacje)  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

ZALETY LIST COMPREHENSIONS:

    - Krótszy i czytelniejszy kod
    - Szybsze wykonanie niż tradycyjna pętla for
    - Łatwiejsze do zrozumienia dla prostych transformacji

KIEDY NIE UŻYWAĆ:
    
    - Gdy logika jest zbyt skomplikowana
    - Gdy potrzebujesz wielu warunków if/else
    - Gdy kod staje się nieczytelny
"""

# ZADANIE 1: Podstawy slicingu

"""
Wejście: Lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Wyjście: Różne fragmenty listy

Efekt:
    Pierwsze 3: [0, 1, 2]
    Ostatnie 3: [7, 8, 9]
    Co drugi: [0, 2, 4, 6, 8]
    Odwrócona: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

🎯 PODPOWIEDŹ:
    Użyj slicing: [:3], [-3:], [::2], [::-1]
"""

print()
print("1: Podstawy slicingu")
print()

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print()
print("Wypisuje liste: ")

print(f"1 trzy wartości listy: {lista[:3]}")
print(f"2 trzy ostatnie wartości listy: {lista[-3:]}")
print(f"Co drugi argument: {lista[::2]}")
print(f"Odwrócona: {lista[::-1]}")

# ZADANIE 2: Slicing tekstu

"""
Wejście: Zdanie "Python jest super!"
Wyjście: Fragmenty tekstu

Efekt:
    Pierwsze 6 znaków: Python
    Ostatnie 6 znaków: super!
    Co trzeci znak: Ph  s

🎯 PODPOWIEDŹ:
    Tekst to też sekwencja - działa slicing!
"""

print()
print("2: Slicing tekstu")
print()

string = "Python jest super!"

print(f"Zdanie: \"{string}\"")
print()
print("Wypisuje zdanie:")
print(f"Pierwsze 6 znaków: {string[0:6]}")
print(f"Ostatnie 6 znaków: {string[-6:]}")
print(f"Co trzeci znak: {string[::3]}")

# ZADANIE 3: List comprehension - kwadraty

"""
Wejście: Zakres 1-10
Wyjście: Lista kwadratów

Efekt:
    Kwadraty: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

🎯 PODPOWIEDŹ:
    [x**2 for x in range(1, 11)]
"""

print()
print("3: List comprehension - kwadraty")
print()

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lista: {lista}")
print()

print("Potegowanie listy: ")
print()

lista = [x**2 for x in range(1,11)]
print(lista)

# ZADANIE 4: List comprehension - filtrowanie

"""
Wejście: Lista liczb [12, 5, 8, 17, 3, 9, 21, 6]
Wyjście: Tylko liczby większe niż 10

Efekt:
    Liczby > 10: [12, 17, 21]

🎯 PODPOWIEDŹ:
    [x for x in lista if x > 10]
"""

print()
print("4: List comprehension - filtrowanie")
print()

liczby = [12, 5, 8, 17, 3, 9, 21, 6]

lista2 = [x for x in liczby if x > 10]
print(lista2)

# ZADANIE 5: List comprehension - transformacja

"""
Wejście: Lista temperatur w °C [0, 20, 30, -10, 15]
Wyjście: Lista temperatur w °F

Efekt:
    Temperatury w °F: [32.0, 68.0, 86.0, 14.0, 59.0]

🎯 PODPOWIEDŹ:
    F = C * 9/5 + 32
    [c * 9/5 + 32 for c in temperatury]
"""

print()
print("5: List comprehension - transformacja")
print()

c = [0, 20, 30, -10, 15]
print(f"°C = {c}")

f = [x * 9 / 5 + 32 for x in c]
print(f"°F = {f}")