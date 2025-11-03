"""
OBSŁUGA PLIKÓW W PYTHONIE - MATERIAŁY
======================================

    PODSTAWOWE OPERACJE NA PLIKACH:
    -------------------------------

        1. OTWIERANIE PLIKU:
            with open("nazwa_pliku.txt", "tryb") as zmienna:
                # operacje na pliku

        2. TRYBY OTWIERANIA:
            "r"                     - read (odczyt) - domyślny
            "w"                     - write (zapis) - tworzy nowy lub nadpisuje istniejący
            "a"                     - append (dopisywanie) - dopisuje na końcu istniejącego
            "x"                     - create (tworzenie) - tworzy nowy, błąd jeśli istnieje
            "r+"                    - read and write (odczyt i zapis)

        3. METODY ODCZYTU:
            plik.read()             - czyta cały plik jako string
            plik.readline()         - czyta jedną linię
            plik.readlines()        - czyta wszystkie linie jako listę
            for linia in plik:      - iteruje po liniach

        4. METODY ZAPISU:
            plik.write("tekst")     - zapisuje tekst
            plik.writelines(lista)  - zapisuje listę stringów

        5. AUTOMATYCZNE ZAMYKANIE:
            Blok 'with' automatycznie zamyka plik, nawet jeśli wystąpi błąd

    PRZYKŁADY:
    ----------

        # Przykład 1: Odczyt całego pliku
            with open("dane.txt", "r") as plik:
                zawartosc = plik.read()
                print(zawartosc)

        # Przykład 2: Odczyt linia po linii
            with open("dane.txt", "r") as plik:
                for linia in plik:
                    print(linia.strip())  # strip() usuwa znaki nowej linii

        # Przykład 3: Zapis do pliku
            with open("wynik.txt", "w") as plik:
                plik.write("Hello World!\n")
                plik.write("To jest druga linia\n")

        # Przykład 4: Dopisywanie do pliku
            with open("log.txt", "a") as plik:
                plik.write("Nowy wpis w logu\n")

        # Przykład 5: Praca z listą linii
            with open("dane.txt", "r") as plik:
                linie = plik.readlines()
                print(f"Plik ma {len(linie)} linii")

        WAŻNE UWAGI:
        -----------
            - Zawsze używaj 'with' - gwarantuje poprawne zamknięcie pliku
            - Pliki tekstowe domyślnie używają kodowania UTF-8
            - W Windows mogą być problemy z znakami nowej linii (\r\n vs \n)
            - Przy zapisie w trybie "w" stara zawartość pliku jest tracona
"""

# ZADANIE 1: Zapis do pliku

"""
Wejście: Tekst od użytkownika
Wyjście: Nowy plik z tekstem

Efekt:
    === ZAPIS DO PLIKU ===
    Podaj tekst do zapisania: Hello World!
    Tekst zapisany do pliku!

🎯 PODPOWIEDŹ:
    Użyj with open("nazwa.txt", "w") as plik: i plik.write(tekst)
"""

import os

print("1: Zapis do pliku")
print()

text = """Litwo! Ojczyzno moja! ty jesteś jak zdrowie.

Ile cię trzeba cenić, ten tylko się dowie,

Kto cię stracił. Dziś piękność twą w całej ozdobie

Widzę i opisuję, bo tęsknię po tobie.

 

Panno Święta, co Jasnej bronisz Częstochowy

I w Ostrej świecisz Bramie! Ty, co gród zamkowy

Nowogródzki ochraniasz z jego wiernym ludem!

Jak mnie dziecko do zdrowia powróciłaś cudem

(Gdy od płaczącej matki pod Twoję opiekę

Ofiarowany, martwą podniosłem powiekę

I zaraz mogłem pieszo do Twych świątyń progu

Iść za wrócone życie podziękować Bogu),

Tak nas powrócisz cudem na Ojczyzny łono.

Tymczasem przenoś moję duszę utęsknioną

Do tych pagórków leśnych, do tych łąk zielonych,

Szeroko nad błękitnym Niemnem rozciągnionych;

Do tych pól malowanych zbożem rozmaitem,

Wyzłacanych pszenicą, posrebrzanych żytem;

Gdzie bursztynowy świerzop, gryka jak śnieg biała,

Gdzie panieńskim rumieńcem dzięcielina pała,

A wszystko przepasane, jakby wstęgą, miedzą

Zieloną, na niej z rzadka ciche grusze siedzą."""

if(os.path.exists("plik_testowy.txt")):
    print("Plik już istnieje!")
else:
    with open("plik_testowy.txt", "w") as plik:
        plik.write(text)
        print("Plik (plik_testowy.txt) zostal utworzony.")

# ZADANIE 2: Odczyt pliku

"""
Wejście: Plik tekstowy
Wyjście: Zawartość pliku

Efekt:
    === ODCZYT PLIKU ===
    Zawartość pliku:
    [treść pliku]

🎯 PODPOWIEDŹ:
    Użyj with open("nazwa.txt", "r") as plik: i plik.read()
"""

print()
print("2: Odczyt pliku")
print()

if(os.path.exists("plik_testowy.txt")):
    with open("plik_testowy.txt", "r") as plik:
        tresc = plik.read()
        print(tresc)
else:
    print("Plik nie istnieje!")

# ZADANIE 3: Dopisywanie do pliku

"""
Wejście: Tekst od użytkownika
Wyjście: Tekst dopisany do istniejącego pliku

Efekt:
    === DOPISYWANIE DO PLIKU ===
    Podaj tekst do dopisania: Nowa linijka
    Tekst dopisany do pliku!

🎯 PODPOWIEDŹ:
    Użyj trybu "a" (append) zamiast "w"
"""

print()
print("3: Dopisywanie do pliku")
print()

if(os.path.exists("plik_testowy.txt")):
    with open("plik_testowy.txt", "a") as plik:
        text = "Adam Mickiewicz: Pan Tadeusz (Inwokacja)"
        plik.write("\n\n")
        plik.write(text)
else:
    print("Plik nie istnieje!")

# ZADANIE 4: Liczenie linii w pliku

"""
Wejście: Plik tekstowy
Wyjście: Liczba linii w pliku

Efekt:
    === LICZENIE LINII ===
    Plik ma 5 linii

🎯 PODPOWIEDŹ:
    Użyj readlines() i len()
"""

print()
print("4: Liczenie linii w pliku")
print()

ileLini = 0

if(os.path.exists("plik_testowy.txt")):
    with open("plik_testowy.txt", "r") as plik:
        for linia in plik:
            ileLini += 1
else:
    print("Plik nie istnieje")
    
print(f"Calkowita liczba lini: {ileLini}")

# ZADANIE 5: Kopiowanie pliku

"""
Wejście: Plik źródłowy
Wyjście: Kopia pliku

Efekt:
    === KOPIOWANIE PLIKU ===
    Plik został skopiowany!

🎯 PODPOWIEDŹ:
    Odczytaj jeden plik i zapisz do drugiego
"""

print()
print("5: Kopiowanie pliku")
print()

if(os.path.exists("plik_testowy.txt")):
    with open("plik_testowy.txt", "r") as plik:
        caly_plik = plik.readlines()
        print(caly_plik)
    
    with open("kopia_plik_testowy.txt", "w") as plik:
        plik.writelines(caly_plik)
else:
    print("Plik nie istnieje!")