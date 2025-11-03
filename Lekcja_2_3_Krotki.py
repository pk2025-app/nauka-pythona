# === KROTKI (TUPLE) - WPROWADZENIE ===

"""
Krotki to struktury danych podobne do list, ale NIEMODYFIKOWALNE.
Główna różnica: listy można zmieniać, krotek NIE można zmieniać.

📝 PODSTAWOWA SKŁADNIA:
    krotka = (element1, element2, element3)
    krotka = element1, element2, element3  # nawiasy opcjonalne

🎯 KLUCZOWE RÓŻNICE vs LISTY:
    LISTA: [1, 2, 3] - MOŻNA zmieniać
    KROTKA: (1, 2, 3) - NIE MOŻNA zmieniać

🔧 PODSTAWOWE OPERACJE:
    - Dostęp: krotka[indeks] ✅ (tak samo jak lista)
    - Długość: len(krotka) ✅  
    - Sprawdzanie: element in krotka ✅
    - Indeksowanie: krotka[0], krotka[-1] ✅

❌ CZEGO NIE MOŻNA ROBIĆ:
    - krotka[0] = nowa_wartość ❌
    - krotka.append(element) ❌
    - krotka.remove(element) ❌

💡 KIEDY UŻYWAĆ KROTEK:
    - Gdy dane nie powinny się zmieniać
    - Jako klucze w słownikach
    - Do zwracania wielu wartości z funkcji
    - Gdy potrzebujesz stałej sekwencji danych
    
# Tworzenie
    krotka = (1, 2, 3)
    krotka = 1, 2, 3      # nawiasy optionalne
    pusta = ()

# Dostęp (tak samo jak lista)
    print(krotka[0])      # 1
    print(krotka[-1])     # 3

# Ale NIE możesz:
    krotka[0] = 10        # BŁĄD! Nie można zmieniać
    krotka.append(4)      # BŁĄD! Nie można dodawać
"""

# ZADANIE 1: Współrzędne punktu

"""
Wejście: Brak (użyj gotowej krotki)
Wyjście: Współrzędne x i y

Efekt:
    === WSPÓŁRZĘDNE ===
    Punkt: (5, 3)
    Współrzędna x: 5
    Współrzędna y: 3

🎯 PODPOWIEDŹ:
    Użyj krotki punkt = (5, 3) i indeksowania punkt[0], punkt[1]
"""

print()
print("1: Współrzędne punktu")
print()

wspolrzedne = (5, 3)
x, y = wspolrzedne

print(f"Wspólrzędne: x = {x}, y = {y}")

# ZADANIE 2: Rozpakowywanie krotki

"""
Wejście: Krotka z danymi pracownika
Wyjście: Imię, nazwisko, stanowisko osobno

Efekt:
    === DANE PRACOWNIKA ===
    Pracownik: ('Anna', 'Kowalska', 'programistka')
    Imię: Anna
    Nazwisko: Kowalska
    Stanowisko: programistka

🎯 PODPOWIEDŹ:
    Użyj imie, nazwisko, stanowisko = pracownik
"""

print()
print("2: Rozpakowywanie krotki")
print()

dane = ("Andrzej", "Więckowski", "Magazynier")

imie, nazwisko, stanowisko = dane

print("Dane pracownika:")
print(f"Imie: {imie}")
print(f"Nazwisko: {nazwisko}")
print(f"Stanowisko: {stanowisko}")

# ZADANIE 3: Krotka jako klucz słownika

"""
Wejście: Słownik z krotkami jako kluczami
Wyjście: Wartości dla podanych współrzędnych

Efekt:
    === SŁOWNIK WSPÓŁRZĘDNYCH ===
    Wartość dla (1, 2): A
    Wartość dla (3, 4): B

🎯 PODPOWIEDŹ:
    Stwórz słownik slownik = {(1,2): 'A', (3,4): 'B'}
"""

print()
print("3: Krotka jako klucz słownika")
print()

wspolrzedne = {(1,2): "A", (3,4): "B", (5,6): "C"}

for klucz, wartosc in wspolrzedne.items():
    print(f"Wspólrzedne: {klucz} = {wartosc}")

# ZADANIE 4: Konwersja lista ↔ krotka

"""
Wejście: Lista liczb
Wyjście: Krotka z tych liczb

Efekt:
    === KONWERSJA ===
    Lista: [1, 2, 3, 4, 5]
    Krotka: (1, 2, 3, 4, 5)

🎯 PODPOWIEDŹ:
    Użyj tuple(lista) i list(krotka)
"""

print()
print("4: Konwersja lista ↔ krotka")
print()

lista = [1, 2, 3, 4, 5]

krotka = tuple(lista)

print(f"Lista: {lista}")
print(f"Krotka: {krotka}")
print(f"Typ listy: {type(lista)}")
print(f"Typ krotki: {type(krotka)}")

# ZADANIE 5: Wyszukiwanie w krotce

"""
Wejście: Krotka imion i szukane imię
Wyjście: Czy imię jest w krotce

Efekt:
    === WYSZUKIWANIE W KROTCE ===
    Krotka: ('Anna', 'Jan', 'Maria', 'Piotr')
    Szukane: Maria
    Maria znajduje się w krotce

🎯 PODPOWIEDŹ:
    Użyj in tak samo jak w listach
"""

print()
print("5: Wyszukiwanie w krotce")
print()

imiona = ("Adam", "Paweł", "Rafał", "Katarzyna", "Weronika", "Monika", "Jagoda")

szukaneImie = "Eliza"

if szukaneImie in imiona:
    print(f"Imie {szukaneImie} znajduje się w krotce.")
else:
    print(f"Imie {szukaneImie} nie znajduje się w krotce.")