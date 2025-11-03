"""
OBSŁUGA BŁĘDÓW W PYTHONIE - WPROWADZENIE
=========================================

CO TO JEST OBSŁUGA BŁĘDÓW?
---------------------------
Mechanizm który pozwala programowi "przeżyć" błędy zamiast się crashować.
Gdy coś pójdzie nie tak, program może wyświetlić ładny komunikat i kontynuować działanie.

PODSTAWOWA SKŁADNIA TRY/EXCEPT:
-------------------------------
try:
    # kod który może spowodować błąd
    ryzykowna_operacja()
except TypBledu:
    # co zrobić gdy błąd wystąpi
    print("Coś poszło nie tak!")

NAJCZĘSTSZE TYPY BŁĘDÓW:
-----------------------
- ValueError - zła wartość (np. int("abc"))
- TypeError - zły typ danych (np. "5" + 2)  
- ZeroDivisionError - dzielenie przez zero
- FileNotFoundError - plik nie istnieje
- IndexError - zły indeks w liście
- KeyError - zły klucz w słowniku

BLOKI OPCJONALNE:
-----------------
- except - łapie konkretny typ błędu
- else - wykonuje się gdy NIE ma błędu
- finally - wykonuje się ZAWSZE (nawet przy błędzie)

NAJPOPULARNIEJSZE BŁĘDY W PYTHONIE - SKRÓCONA WERSJA
=====================================================

ValueError        - zła wartość (int("abc"))
TypeError         - zły typ danych ("5" + 2)
ZeroDivisionError - dzielenie przez zero (10 / 0)
IndexError        - zły indeks listy ([1,2,3][5])
KeyError          - zły klucz słownika ({"a":1}["b"])
FileNotFoundError - plik nie istnieje (open("brak.txt"))
AttributeError    - zła metoda/atrybut ("hello".append())
NameError         - niezdefiniowana zmienna (print(nieistnieje))
ImportError       - zły import (import nieistnieje)
KeyboardInterrupt - użytkownik przerwał (Ctrl+C)
"""

# ZADANIE 1: Błędna konwersja liczby

"""
Wejście: Tekst od użytkownika
Wyjście: Liczba lub komunikat błędu

Efekt:
    === KONWERSJA LICZBY ===
    Podaj liczbę: abc
    Błąd: To nie jest poprawna liczba!

🎯 PODPOWIEDŹ:
    Użyj try/except ValueError przy int(input())
"""

print("1: Błędna konwersja liczby")
print()

try :
    liczba = int(input("Wprowadź liczbę: "))
    print(f"Wprowadzona liczba: {liczba}")
except ValueError:
    print("Podales bledna liczbę.")

# ZADANIE 2: Dzielenie z zabezpieczeniem

"""
Wejście: Dwie liczby od użytkownika
Wyjście: Wynik dzielenia lub komunikat błędu

Efekt:
    === DZIELENIE ===
    Podaj liczbę A: 10
    Podaj liczbę B: 0
    Błąd: Nie można dzielić przez zero!

🎯 PODPOWIEDŹ:
    Użyj except ZeroDivisionError
"""

print()
print("2: Dzielenie z zabezpieczeniem")
print()

try:
    liczbaA = int(input("Wprowadź pierwszą liczbę: "))
    liczbaB = int(input("Wprowadź drugą liczbę: "))
    print(f"{liczbaA} / {liczbaB} = {liczbaA/liczbaB}")
except ZeroDivisionError:
    print("Nie dziel przez 0!")

# ZADANIE 3: Bezpieczny dostęp do listy

"""
Wejście: Lista i indeks od użytkownika
Wyjście: Element lub komunikat błędu

Efekt:
    === DOSTĘP DO LISTY ===
    Lista: [10, 20, 30]
    Podaj indeks: 5
    Błąd: Indeks poza zakresem!

🎯 PODPOWIEDŹ:
    Użyj except IndexError
"""

print()
print("3: Bezpieczny dostęp do listy")
print()

lista = [10, 20, 30]

linia = int(input("Wprowadź którą pozycje na liście chcesz sprawdzić: "))

try:
    print(f"Na pozycji {linia} jest wartość: {lista[linia+1]}")
except IndexError:
    print("Index poza zakresem.")

# ZADANIE 4: Obsługa wielu błędów

"""
Wejście: Operacja na pliku
Wyjście: Wynik lub odpowiedni komunikat błędu

Efekt:
    === OBSŁUGA PLIKU ===
    Podaj nazwę pliku: nieistniejacy.txt
    Błąd: Plik nie istnieje!

🎯 PODPOWIEDŹ:
    Użyj wielu except dla różnych błędów
"""

print()
print("4: Obsługa wielu błędów")
print()

nazwa_pliku = input("Podaj nazwę pliku: ")

try:
    with open(nazwa_pliku, "r") as plik:
            print(plik.read())
except FileNotFoundError:
    print("Plik nie istnieje!")
except PermissionError:
    print("Brak dostępu do pliku!")

# ZADANIE 5: Finally - sprzątanie

"""
Wejście: Operacja która może się nie udać
Wyjście: Komunikat że sprzątanie zostało wykonane

Efekt:
    === FINALLY ===
    Operacja się nie udała, ale sprzątanie wykonane!

🎯 PODPOWIEDŹ:
    Użyj bloku finally który wykonuje się zawsze
"""

print()
print("5: Finally - sprzątanie")
print()

try:
    for i in range(0, 5):
        slowo = input(f"{i}: ")
        krotek.add(slowo)
    
    print()
    print("Wypisuje krotka: ")
    print(krotek)
except:
    print("Krotki są niemodyfikalne!")
finally:
    print("Ten kod wykona sie zawsze!")