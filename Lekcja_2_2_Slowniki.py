"""
📚 OMÓWIENIE SŁOWNIKÓW (DICTIONARY)
Czym jest słownik?
    To struktura klucz: wartość - jak prawdziwy słownik:
        Klucz = słowo (np. "kot")
        Wartość = definicja (np. "zwierzę domowe")

# === SŁOWNIKI (DICTIONARY) ===

    # TWORZENIE
        {}                                          # pusty słownik
        {"klucz": "wartość"}                        # słownik z jednym elementem
        {"klucz1": wartość1, "klucz2": wartość2}    # słownik z wieloma elementami

    # DODAWANIE/MODYFIKACJA
        slownik["klucz"] = wartość                  # dodaje lub zmienia wartość

    # USUWANIE  
        del slownik["klucz"]                        # usuwa klucz i wartość

    # ODWOŁYWANIE SIĘ
        slownik["klucz"]                            # pobiera wartość (błąd jeśli brak klucza)
        slownik.get("klucz", domyślna)              # bezpieczne pobieranie

    # INFORMACJE
        "klucz" in slownik                          # sprawdza czy klucz istnieje
        len(slownik)                                # liczba elementów

    # ITEROWANIE
        for klucz in slownik:                       # iteruje po kluczach
        for wartosc in slownik.values():            # iteruje po wartościach  
        for klucz, wartosc in slownik.items():      # iteruje po parach

    # METODY
        slownik.keys()                              # lista kluczy
        slownik.values()                            # lista wartości
        slownik.items()                             # lista par (klucz, wartość)
        slownik.pop("klucz")                        # usuwa i zwraca wartość
        slownik.clear()                             # czyści słownik
"""

# ZADANIE 1: Słownik uczniów

"""
Wejście: Brak (użyj gotowego słownika)
Wyjście: Lista uczniów i ich ocen

Efekt:
    === SŁOWNIK UCZNIÓW ===
    Anna: 5
    Jan: 4
    Maria: 5
    Piotr: 3

🎯 PODPOWIEDŹ:
    Stwórz słownik {imie: ocena} i użyj pętli for po items()
"""

print("1: Słownik uczniów")
print()

oceny = {"Janek": 5, "Emilka": 3, "Dawid": 2, "Robert": 2, "Roksana": 5}

for imie, ocena in oceny.items():
    print(f"{imie}: {ocena}")

# ZADANIE 2: Książka telefoniczna

"""
Wejście: 3 pary (imię, telefon) od użytkownika
Wyjście: Cała książka telefoniczna

Efekt:
    === KSIĄŻKA TELEFONICZNA ===
    Podaj imię: Anna
    Podaj telefon: 123-456-789
    [...]
    Twoje kontakty:
    Anna: 123-456-789
    Jan: 987-654-321
    Maria: 555-123-456

🎯 PODPOWIEDŹ:
    Użyj pętli do dodawania do słownika, potem wyświetl items()
"""

print()
print("2: Książka telefoniczna")
print()

print("Wprowadz imię oraz numer telefony:")
telefoniczna = {}

for i in range (1, 4):
    imie = input(f"Imie[{i}]: ")
    numer = input(f"Numer teledonu[{i}]: ")
    telefoniczna[imie] = numer
    
print()

print("Twoje kontakty: ")

for i, (imie, numer) in enumerate(telefoniczna.items(), 1):
    print(f"{i}: {imie} - {numer}")

# ZADANIE 3: Wyszukiwarka w słowniku

"""
Wejście: Słownik produktów i szukany produkt
Wyjście: Cena produktu lub informacja o braku

Efekt:
    === WYSZUKIWARKA CEN ===
    Słownik: {'chleb': 3.50, 'mleko': 2.80, 'jajka': 8.00}
    Podaj produkt: mleko
    Cena mleko: 2.80 zł

🎯 PODPOWIEDŹ:
    Użyj get() z wartością domyślną dla bezpiecznego wyszukiwania
"""

print()
print("3: Wyszukiwarka w słowniku")
print()

cennik = {'chleb': 3.50, 'mleko': 2.80, 'jajka': 8.00}
szukane = "jajka"

print("Szukam produktu...")

print(f"Produkt: {szukane} - {cennik.get(szukane, "Brak produktu w bazie.")}")

# ZADANIE 4: Aktualizacja magazynu

"""
Wejście: Słownik magazynu i operacje (dodaj/usuw)
Wyjście: Zaktualizowany stan magazynu

Efekt:
    === MAGAZYN ===
    Stan: {'jabłka': 10, 'banany': 5, 'pomarańcze': 8}
    Co chcesz zrobić? (dodaj/usun): dodaj
    Podaj produkt: gruszki
    Podaj ilość: 7
    Nowy stan: {'jabłka': 10, 'banany': 5, 'pomarańcze': 8, 'gruszki': 7}

🎯 PODPOWIEDŹ:
    Użyj input() do wyboru operacji i modyfikuj słownik
"""

print()
print("4: Aktualizacja magazynu")
print()

stan = {'jabłka': 10, 'banany': 5, 'pomarańcze': 8}
wybor = ""

while(wybor != "dodaj" and wybor != "usun"):
    wybor = input("Co chcesz zrobić? (dodaj/usun): ").lower()
    print()
    
    if(wybor != "dodaj" and wybor != "usun"):
        print("Bledna komenda...")
        print("Powtorz...")
        print()

if(wybor == "dodaj"):
    produkt = input("Nazwa produktu: ")
    ilosc = int(input("Stan magazynowy: "))
    stan[produkt] = ilosc

if(wybor == "usun"):
    for nazwa in stan:
        print(nazwa)
    produkt = ""
    
    while(stan.get(produkt, 0) == 0):
        produkt = input("Wybierz nazwę produktu: ")
        if(stan.get(produkt, 0) == 0):
            print("Nie ma takigo produktu!")
            print()
    
    approve = input(f"Czy napewno chcesz usunąć [{produkt}]? [y/n] ").lower()
    if(approve != "y" and approve != "n"):
        print("Bledna komenda, produkt nie zostal usuniety.")
    elif(approve == "n"):
        print(f"Usunięcie produktu [{produkt}] zostalo anulowane.")
    else:
        del stan[produkt]
    
print()
print("Aktualny stan magazynowy: ")

for i, (nazwa, sztuki) in enumerate(stan.items(), 1):
    print(f"{i}: {nazwa} - {sztuki}")

print()

# ZADANIE 5: Statystyki słownika

"""
Wejście: Słownik z ocenami
Wyjście: Statystyki ocen

Efekt:
    === STATYSTYKI OCEN ===
    Oceny: {'matematyka': 5, 'fizyka': 4, 'chemia': 3, 'biologia': 5}
    Najlepsza ocena: 5
    Najsłabsza ocena: 3
    Średnia: 4.25

🎯 PODPOWIEDŹ:
    Użyj max(), min(), sum() i len() na values()
"""

print()
print("5: Statystyki słownika")
