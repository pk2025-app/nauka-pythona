# === FUNKCJE - PODSTAWY PODSTAW ===

"""
SKŁADNIA FUNKCJI:
-----------------
def nazwa_funkcji(argument1, argument2):
    # kod funkcji
    return wynik



OPIS ELEMENTÓW:
---------------
- def - słowo kluczowe które tworzy funkcję
- nazwa_funkcji - dowolna nazwa (tak jak zmienna)
- (argumenty) - dane które funkcja otrzymuje (może być puste)
- : - dwukropek oznacza początek bloku funkcji
- return - zwraca wynik (opcjonalne - funkcja może nic nie zwracać)



PROSTE ZASADY:
--------------
1. Funkcję trzeba ZDEFINIOWAĆ zanim jej UŻYSZ
2. Funkcję WYWOŁUJEMY przez: nazwa_funkcji()
3. Argumenty to dane które podajemy funkcji
4. Return to wynik który funkcja zwraca



JAK DZIAŁA FUNKCJA KROK PO KROKU:
----------------------------------
1. Definicja                - tworzymy funkcję
2. Wywołanie                - używamy funkcji  
3. Argumenty                - funkcja dostaje dane
4. Wykonanie                - funkcja robi coś z danymi
5. Return                   - funkcja zwraca wynik



PRZYKŁADY WYWOŁANIA:
--------------------
funkcja()                   - bez argumentów
funkcja(5)                  - z jednym argumentem  
funkcja(5, 10)              - z dwoma argumentami
zmienna = funkcja(5, 10)    - zapisanie wyniku do zmiennej


CO MOŻE ZWRACAĆ FUNKCJA:
------------------------
- Liczby: return 5
- Tekst: return "Hello"
- True/False: return True
- Listy: return [1, 2, 3]
- Nic: (brak return) = None



NAJCZĘSTSZE BŁĘDY:
------------------
1. Brak dwukropka po definicji
2. Złe wcięcia w bloku funkcji
3. Wywołanie funkcji przed jej zdefiniowaniem
4. Za mało/za dużo argumentów



PARAMETRY POZYCYJNE I NAZWANE W FUNKCJACH
==========================================

    PARAMETRY POZYCYJNE (POSITIONAL):
        - Ważna KOLEJNOŚĆ argumentów
        - Muszą być podane w tej samej kolejności co w definicji funkcji
        - Szybsze do pisania, ale mniej czytelne

        Przykład:
            def przedstaw_sie(imie, wiek, miasto):
                print(f"{imie}, {wiek} lat, {miasto}")

        # Poprawne użycie pozycyjne:
            przedstaw_sie("Anna", 25, "Warszawa")

        # Niepoprawne (mieszają się dane):
            przedstaw_sie(25, "Anna", "Warszawa")  # ŹLE!


    PARAMETRY NAZWANE (KEYWORD):
        - Używamy NAZW parametrów przy wywołaniu
        - Nie ważna kolejność argumentów
        - Bardziej czytelne i bezpieczne

        Przykład:
            def przedstaw_sie(imie, wiek, miasto):
                print(f"{imie}, {wiek} lat, {miasto}")

        # Poprawne użycie nazwane (dowolna kolejność):
            przedstaw_sie(wiek=25, miasto="Warszawa", imie="Anna")
            przedstaw_sie(imie="Anna", wiek=25, miasto="Warszawa")


ZAKRES ZMIENNYCH (SCOPE)
========================
    Zmienne mogą istnieć w różnych zakresach (contextach):

    ZMIENNE LOKALNE:
        - Istnieją TYLKO wewnątrz funkcji
        - Nie są dostępne na zewnątrz
        - Każda funkcja ma swoje własne zmienne lokalne

        Przykład:
            def moja_funkcja():
                lokalna = "Jestem tylko w funkcji"
                print(lokalna)              # DZIAŁA

            moja_funkcja()
            print(lokalna)                  # BŁĄD! Zmienna nie istnieje poza funkcją

    ZMIENNE GLOBALNE:
        - Dostępne WSZĘDZIE w programie
        - Mogą być używane wewnątrz funkcji
        - Do MODYFIKACJI potrzebne słowo 'global'

        Przykład:
            globalna = "Jestem dostępna wszędzie"

        def moja_funkcja():
            print(globalna)                 # DZIAŁA - tylko odczyt

        def inna_funkcja():
            global globalna                 # Musimy powiedzieć że używamy globalnej
            globalna = "Nowa wartość"       # MODYFIKACJA

    SŁOWO KLUCZOWE 'global':
        - Używamy gdy chcemy MODYFIKOWAĆ zmienną globalną wewnątrz funkcji
        - Tylko do odczytu NIE wymaga 'global'
        - Bez 'global' tworzysz nową zmienną lokalną

        Przykład:
        licznik = 0

        def zwieksz():
            global licznik                  # Mówimy: modyfikuj globalną zmienną
            licznik += 1

        zwieksz()
        print(licznik)                      # 1

    WAŻNE ZASADY:
        1. Zawsze używaj parametrów nazwanych gdy funkcja ma wiele argumentów
        2. Unikaj modyfikowania zmiennych globalnych - to może powodować błędy
        3. Używaj zmiennych lokalnych gdy to możliwe
        4. Jeśli musisz modyfikować globalną, zawsze używaj 'global'
"""

# ZADANIE 1: Prosta funkcja powitania

"""
Wejście: Brak
Wyjście: Tekst powitania

Efekt:
    === POWITANIE ===
    Witaj świecie!

🎯 PODPOWIEDŹ:
    Stwórz funkcję bez argumentów która printuje "Witaj świecie!"
    Funkcja nie zwraca wartości (brak return), tylko wyświetla tekst
"""

print()
print("1: Prosta funkcja powitania")
print()

def hello():
    
    """Wyświetla powitanie świata"""
    print("Witaj świecie")
    
hello()

# ZADANIE 2: Funkcja z jednym argumentem

"""
Wejście: Imię użytkownika
Wyjście: Spersonalizowane powitanie

Efekt:
    === POWITANIE ===
    Podaj swoje imię: Anna
    Witaj Anna!

🎯 PODPOWIEDŹ:
    Stwórz funkcję z jednym argumentem 'imie'
    Użyj f-string: f"Witaj {imie}!"
"""

print()
print("2: Funkcja z jednym argumentem")
print()

def powitaj(imie):
    
    """Wyświetla powitanie z imieniem"""
    print(f"Witaj {imie}")
    
powitaj(input("Podaj swoje imie: "))

# ZADANIE 3: Funkcja zwracająca wynik

"""
Wejście: Dwie liczby
Wyjście: Wynik dodawania

Efekt:
    === DODAWANIE ===
    Wynik: 5 + 3 = 8

🎯 PODPOWIEDŹ:
    Stwórz funkcję z dwoma argumentami
    Użyj return aby zwrócić wynik dodawania
    Zapisz wynik do zmiennej: wynik = dodaj(5, 3)
"""

print()
print("3: Funkcja zwracająca wynik")
print()

def dodaj(a, b):
    return a + b

print("Podaj 2 liczby: ")
a = int(input("A: "))
b = int(input("B: "))

print()
print(f"Wynik: {a} + {b} = {dodaj(a,b)}")

# ZADANIE 4: Funkcja z warunkiem

"""
Wejście: Wiek użytkownika
Wyjście: Informacja o pełnoletności

Efekt:
    === SPRAWDZANIE WIEKU ===
    Podaj swój wiek: 16
    Jesteś niepełnoletni

🎯 PODPOWIEDŹ:
    Stwórz funkcję która zwraca True/False
    Użyj if wiek >= 18: return True else: return False
"""

print()
print("4: Funkcja z warunkiem")
print()

def sprawdzCzyPelnoletni(wiek):
    if(wiek < 18):
        print(f"Jesteś niepelnoletni.. wróć za {18 - wiek} lat")
    else:
        print("Brawo! Jesteś pelnoletni :) Możesz wejść.")
    
sprawdzCzyPelnoletni(int(input("Podaj swój wiek... ")))

# ZADANIE 5: Funkcja z wartością domyślną

"""
Wejście: Imię i opcjonalny tekst powitania
Wyjście: Spersonalizowane powitanie

Efekt:
    === POWITANIE ===
    Witaj Anna!
    Cześć Jan!

🎯 PODPOWIEDŹ:
    Stwórz funkcję z dwoma argumentami, drugi z wartością domyślną
    def powitanie(imie, tekst="Witaj"):
"""

print()
print("5: Funkcja z wartością domyślną")
print()

def powitaj(imie, tekst = "Witaj"):
    print(f"{tekst} {imie}")
    
print("Wprowadź 2 dane, imie oraz opcjonalny tekst powitalny.")
imie = input("Imie: ")
wiadomosc = input("Tekst powitalny: ")

print(f"Ilosc znakow: {len(wiadomosc)}")

if(len(wiadomosc) == 0):
    powitaj(imie)    
else:
    powitaj(imie, wiadomosc)

# ZADANIE 6: Funkcja konwertująca

"""
Wejście: Temperatura w Celsiuszach
Wyjście: Temperatura w Fahrenheitach

Efekt:
    === KONWERTER TEMPERATURY ===
    Podaj temperaturę w °C: 20
    20°C = 68°F

🎯 PODPOWIEDŹ:
    Wzór: F = C × 9/5 + 32
    Funkcja powinna zwracać wynik
"""

print()
print("6: Funkcja konwertująca")
print()

def fahrenheity(celcjusze):
    return celcjusze * 9 / 5 + 32

celcjusze = float(input("Podaj temperature w °C - "))

print(f"{celcjusze}°C = {fahrenheity(celcjusze)}°F")