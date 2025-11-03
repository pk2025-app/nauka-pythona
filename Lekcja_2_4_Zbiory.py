# === ZBIORY (SET) - PROSTE WYJAŚNIENIE ===

"""
Co to jest zbiór?
    To jak TORBA z rzeczami, gdzie:
    - Nie może być dwóch takich samych rzeczy (automatycznie usuwa duplikaty)
    - Kolejność nie ma znaczenia (rzeczy są pomieszane w torbie)
    - Możesz dodawać i wyjmować rzeczy

📦 PRZYKŁADY TWORZENIA ZBIORÓW:

    # Zbiór z liczbami - nawiasy klamrowe {}
        zbior_liczb = {1, 2, 3, 4, 5}

    # Zbiór z tekstami  
        zbior_imion = {"Anna", "Jan", "Maria"}

    # Zbiór z listy - konwersja listy na zbiór
        lista = [1, 2, 2, 3, 3, 3]              # lista z duplikatami
        zbior = set(lista)                      # {1, 2, 3} - duplikaty zniknęły!

    # Pusty zbiór (uwaga: {} to słownik, nie zbiór!)
        pusty_zbior = set()

🧩 CO MOŻESZ ROBIĆ ZE ZBIORAMI?

    # DODAWANIE elementu do zbioru
        zbior = {1, 2, 3}
        zbior.add(4)                            # zbior = {1, 2, 3, 4}
        zbior.add(2)                            # nic się nie dzieje, bo 2 już jest

    # USUWANIE elementu ze zbioru
        zbior.remove(3)                         # zbior = {1, 2, 4}

    # SPRAWDZANIE czy element jest w zbiorze
        if 2 in zbior:
            print("2 jest w zbiorze!")

    # ILOŚĆ elementów w zbiorze
        print(len(zbior))                       # pokaże 3

🔢 OPERACJE MATEMATYCZNE NA ZBIORACH:
    Działają tak jak w matematyce!

    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}

    # SUMA (wszystkie elementy z A i B)
        suma = A | B                            # {1, 2, 3, 4, 5, 6}

    # CZĘŚĆ WSPÓLNA (elementy w A i B)
        czesc_wspolna = A & B                   # {3, 4}

    # RÓŻNICA (elementy w A, ale nie w B)
        roznica = A - B                         # {1, 2}

    # RÓŻNICA SYMETRYCZNA (elementy w A lub B, ale nie w obu)
        roz_sym = A ^ B                         # {1, 2, 5, 6}

💡 KIEDY UŻYWAĆ ZBIORÓW W PRAKTYCE?

    # Gdy chcesz usunąć duplikaty z listy
        lista_z_duplikatami = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        lista_bez_duplikatow = list(set(lista_z_duplikatami))
        wynik: [1, 2, 3, 4] (kolejność może być inna)

    # Gdy chcesz szybko sprawdzić czy coś istnieje
        (zbiory są szybsze niż listy do wyszukiwania)

    # Gdy pracujesz z unikalnymi wartościami
        (np. unikalni użytkownicy, unikalne tagi)

⚠️ WAŻNE RÓŻNICE:
    - Zbiór: {1, 2, 3} - nie ma duplikatów, nieuporządkowany
    - Lista: [1, 2, 3] - mogą być duplikaty, uporządkowana
    - Krotka: (1, 2, 3) - niezmienna, uporządkowana
    - Słownik: {1: "a", 2: "b"} - pary klucz:wartość
"""

# ZADANIE 1: Unikalne słowa

"""
Wejście: Zdanie od użytkownika
Wyjście: Unikalne słowa ze zdania

Efekt:
    === UNIKALNE SŁOWA ===
    Podaj zdanie: ala ma kota i ala ma psa
    Unikalne słowa: {'ala', 'ma', 'kota', 'i', 'psa'}

🎯 PODPOWIEDŹ:
    Użyj set(text.split())
"""

print("1: Unikalne słowa")
print()

text = input("Wprowadź swoje zdanie: ")

zbior_imiona = set(text.split())

print()
print("Przetwarzam zdanie...")
print()

for i, slowo in enumerate(zbior_imiona, 1):
    print(f"{i}: {slowo}")

# ZADANIE 2: Wspólne znajome

"""
Wejście: Znajomi dwóch osób (dwie listy)
Wyjście: Wspólni znajomi

Efekt:
    === WSPÓLNI ZNAJOMI ===
    Znajomi Anny: ['Jan', 'Maria', 'Piotr', 'Kasia']
    Znajomi Marka: ['Maria', 'Tomasz', 'Kasia', 'Adam']
    Wspólni znajomi: {'Maria', 'Kasia'}

🎯 PODPOWIEDŹ:
    Użyj set(lista1) & set(lista2)
"""

print()
print("2: Wspólne znajome")
print()

znajomiEwy = ["Adam", "Ola", "Michał", "Monika"]
znajomiBasi = ["Marcel", "Robert", "Monika", "Ola"]

wspolniZnajomi = set(znajomiEwy) & set(znajomiBasi)

print()
print("Wspólni znajomi to:")
for znajomy in wspolniZnajomi:
    print(znajomy)

# ZADANIE 3: Unikalne liczby

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



# ZADANIE 4: Operacje na zbiorach

"""
Wejście: Dwa zbiory liczb
Wyjście: Wyniki operacji matematycznych

Efekt:
    === OPERACJE NA ZBIORACH ===
    Zbiór A: {1, 2, 3, 4}
    Zbiór B: {3, 4, 5, 6}
    Suma: {1, 2, 3, 4, 5, 6}
    Część wspólna: {3, 4}
    Różnica A-B: {1, 2}

🎯 PODPOWIEDŹ:
    Użyj | (suma), & (część wspólna), - (różnica)
"""

print()
print("4: Operacje na zbiorach")
print()



# ZADANIE 5: Filtrowanie duplikatów

"""
Wejście: Lista z duplikatami
Wyjście: Lista bez duplikatów

Efekt:
    === USUWANIE DUPLIKATÓW ===
    Lista z duplikatami: [1, 2, 2, 3, 4, 4, 4, 5]
    Lista bez duplikatów: [1, 2, 3, 4, 5]

🎯 PODPOWIEDŹ:
    Użyj list(set(lista_z_duplikatami))
"""

print()
print("5: Filtrowanie duplikatów")
print()

