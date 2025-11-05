"""
KLASY I OBIEKTY W PYTHONIE - KOMPLETNY PRZEWODNIK
=================================================

PO CO W OGÓLE KLASY? - ŻYCIOWY PRZYKŁAD
----------------------------------------

BEZ KLAS (bałagan):
gracz1_imie = "Jan"
gracz1_zdrowie = 100
gracz1_poziom = 1

gracz2_imie = "Anna" 
gracz2_zdrowie = 120
gracz2_poziom = 2

def atakuj_gracza(gracz_imie, gracz_zdrowie, obrazenia):
    nowe_zdrowie = gracz_zdrowie - obrazenia
    return nowe_zdrowie

Z KLASAMI (porządek):
class Gracz:
    def __init__(self, imie, zdrowie=100):
        self.imie = imie
        self.zdrowie = zdrowie
    
    def atakuj(self, obrazenia):
        self.zdrowie -= obrazenia

gracz1 = Gracz("Jan")
gracz2 = Gracz("Anna", 120)
gracz1.atakuj(20)

CO JEST CZYM? - PROSTE WYJAŚNIENIE
-----------------------------------

KLASA = FORMARZ DO WYPEŁNIENIA
------------------------------
Klasa to SZABLON, FORMULARZ, PROJEKT
- Określa JAKIE DANE przechowuje (imię, zdrowie)
- Określa CO MOŻNA ROBIĆ (atakuj, leczenie)
- To tylko PLAN - sam nie przechowuje danych

PRZYKŁAD: 
- Klasa "DowódOsobisty" - ma pola: imię, nazwisko, pesel
- Klasa "Samochód" - ma: marka, kolor, paliwo

OBIEKT = WYPEŁNIONY FORMARZ
---------------------------
Obiekt to KONKRETNA RZECZ utworzona z klasy
- Ma KONKRETNE wartości (imię="Jan", zdrowie=80)
- To PRAWDZIWA RZECZ która istnieje w programie
- Z jednej klasy można stworzyć wiele obiektów

PRZYKŁAD:
- Obiekt "moj_dowód" - imię="Jan", nazwisko="Kowalski"
- Obiekt "moje_auto" - marka="Toyota", kolor="czerwony"

METODA = CO OBIEKT UMIE ROBIĆ
-----------------------------
Metoda to FUNKCJA należąca do obiektu
- Operuje na danych TEGO KONKRETNEGO obiektu
- Ma dostęp do self - czyli "siebie samego"

PRZYKŁAD:
- Samochód.uruchom_silnik() - uruchamia TEN samochód
- Gracz.atakuj() - atakuje TEGO gracza

CZEMU NIE MOŻNA ZREZYGNOWAĆ Z KTÓREGOŚ?
---------------------------------------

BEZ KLASY: 
- Brak szablonu, każdy obiekt tworzony "na piechotę"
- Trudno utrzymać porządek gdy obiektów jest dużo

BEZ OBIEKTU:
- Klasa sama nic nie robi - to tylko papierowy formularz
- Bez obiektów program nie ma żadnych danych

BEZ METOD:
- Obiekty byłyby tylko "głupimi" paczkami danych
- Logika rozrzucona po całym programie

PODSTAWOWA SKŁADNIA W PRAKTYCE:
-------------------------------
class Gracz:                    # FORMULARZ Gracz
    def __init__(self, imie):   # Wypełnianie formularza
        self.imie = imie        # Pole "imie" = podana wartość
        self.zdrowie = 100      # Pole "zdrowie" = zawsze 100
    
    def przedstaw_sie(self):    # Co umie gracz
        return f"Jestem {self.imie}"  # self = TEN gracz

# UŻYCIE:
gracz1 = Gracz("Jan")          # Wypełniamy formularz - tworzymy OBIEKT
print(gracz1.przedstaw_sie())  # Wywołujemy METODĘ na OBIEKCIE

DZIEDZICZENIE - RODZIC I DZIECKO:
---------------------------------
class Zwierze:                  # RODZIC - ogólne zwierzę
    def __init__(self, imie):
        self.imie = imie
    
    def dzwiek(self):
        return "Jakiś dźwięk"

class Pies(Zwierze):            # DZIECKO - specyficzne zwierzę
    def __init__(self, imie, rasa):
        super().__init__(imie)  # Najpierw wypełnij formularz rodzica
        self.rasa = rasa        # Potem dodaj swoje pola
    
    def dzwiek(self):           # Nadpisanie metody rodzica
        return "Hau hau!"

# UŻYCIE:
azor = Pies("Azor", "owczarek")
print(azor.imie)    # Dziedziczone od Zwierze: "Azor"
print(azor.rasa)    # Własne: "owczarek"  
print(azor.dzwiek()) # Nadpisane: "Hau hau!"

PRACA Z LISTAMI W KLASACH:
--------------------------
class Koszyk:
    def __init__(self):
        self.produkty = []      # Pusta lista jako pole
    
    def dodaj(self, nazwa, cena):
        self.produkty.append((nazwa, cena))  # Dodaj do listy
    
    def suma(self):
        return sum(cena for _, cena in self.produkty)  # Przejdź przez listę

WALIDACJA - SPRAWDZANIE WARUNKÓW:
--------------------------------
class KontoBankowe:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def wyplata(self, kwota):
        if kwota <= self.saldo:     # SPRAWDŹ warunek
            self.saldo -= kwota     # Jeśli OK - wykonaj
            return True
        else:
            print("Brak środków!")  # Jeśli nie - komunikat
            return False

SKŁADNIA TECHNICZNA - PODSUMOWANIE:
===================================

TWORZENIE KLASY:
---------------
class {NazwaKlasy}:
    def __init__(self, {parametry}):
        self.{atrybut1} = {wartość1}
        self.{atrybut2} = {wartość2}

TWORZENIE METODY:
-----------------
def {nazwa_metody}(self, {parametry}):
    {użyj self.atrybut1}
    return {wynik}

DZIEDZICZENIE:
--------------
class {Dziecko}({Rodzic}):
    def __init__(self, {parametry}):
        super().__init__({parametry_rodzica})
        self.{nowy_atrybut} = {wartość}

TWORZENIE OBIEKTU:
------------------
{obiekt} = {Klasa}({argumenty})

WYWOŁANIE METODY:
-----------------
{obiekt}.{metoda}({argumenty})

DOSTĘP DO ATRYBUTU:
-------------------
{obiekt}.{atrybut}
"""

# =============================================================================
# ZADANIE 1: Podstawowa klasa - Gracz RPG
# =============================================================================

"""
Wejście: Brak
Wyjście: Obiekt klasy Gracz z metodami

Efekt:
    Gracz: Jan, poziom: 1, zdrowie: 100
    Gracz przedstawia się i otrzymuje obrażenia

🎯 WYMAGANIA:
    Stwórz klasę Gracz z:
    - atrybutami: imie, poziom=1, zdrowie=100
    - metodą przedstaw_sie() zwracającą string z danymi
    - metodą otrzymaj_obrazenia(ile) zmniejszającą zdrowie

📝 PRZYKŁAD UŻYCIA:
    gracz1 = Gracz("Jan")
    print(gracz1.przedstaw_sie())
    gracz1.otrzymaj_obrazenia(20)
"""

print()
print("1: Podstawowa klasa - Gracz RPG")
print()



# =============================================================================
# ZADANIE 2: Klasa z obliczeniami - Prostokat
# =============================================================================

"""
Wejście: Długości boków
Wyjście: Obiekt umiejący obliczać pole i obwód

Efekt:
    Prostokąt 5x3 ma pole: 15 i obwód: 16

🎯 WYMAGANIA:
    Stwórz klasę Prostokat z:
    - atrybutami: bok_a, bok_b
    - metodą pole() zwracającą pole prostokąta
    - metodą obwod() zwracającą obwód

📝 PRZYKŁAD UŻYCIA:
    prostokat = Prostokat(5, 3)
    print(f"Pole: {prostokat.pole()}")
    print(f"Obwód: {prostokat.obwod()}")
"""

print()
print("2: Klasa z obliczeniami - Prostokat")
print()



# =============================================================================
# ZADANIE 3: Klasa z walidacją - KontoBankowe
# =============================================================================

"""
Wejście: Saldo początkowe
Wyjście: Obiekt kontrolujący operacje bankowe

Efekt:
    Konto z saldem: 1000
    Wplata: 500, Wyplata: 200, Próba wyplaty: 2000 -> Błąd

🎯 WYMAGANIA:
    Stwórz klasę KontoBankowe z:
    - atrybutem: saldo
    - metodą wplata(kwota) zwiększającą saldo
    - metodą wyplata(kwota) zmniejszającą saldo (tylko jeśli wystarczy środków)
    - metodą sprawdz_saldo() zwracającą saldo

📝 PRZYKŁAD UŻYCIA:
    konto = KontoBankowe(1000)
    konto.wplata(500)
    konto.wyplata(200)
    konto.wyplata(2000)  # Powinno się nie udać
"""

print()
print("3: Klasa z walidacją - KontoBankowe")
print()



# =============================================================================
# ZADANIE 4: Klasa z listą - KoszykZakupowy
# =============================================================================

"""
Wejście: Produkty i ceny
Wyjście: Obiekt zarządzający listą zakupów

Efekt:
    Koszyk zawiera: ['chleb', 'mleko']
    Łączna wartość: 8.5
    Po usunięciu: ['mleko'], wartość: 3.5

🎯 WYMAGANIA:
    Stwórz klasę KoszykZakupowy z:
    - atrybutem: produkty (początkowo pusta lista)
    - metodą dodaj_produkt(nazwa, cena) dodającą krotkę (nazwa, cena)
    - metodą usun_produkt(nazwa) usuwającą produkt
    - metodą suma() zwracającą łączną wartość koszyka

📝 PRZYKŁAD UŻYCIA:
    koszyk = KoszykZakupowy()
    koszyk.dodaj_produkt("chleb", 5.0)
    koszyk.dodaj_produkt("mleko", 3.5)
    koszyk.usun_produkt("chleb")
"""

print()
print("4: Klasa z listą - KoszykZakupowy")
print()



# =============================================================================
# ZADANIE 5: Klasa dziedziczenie - PostacSpecjalna
# =============================================================================

"""
Wejście: Specjalne umiejętności
Wyjście: Rozszerzona klasa Gracz z dodatkowymi możliwościami

Efekt:
    Mag: Gandalf, poziom: 5, mana: 100
    Rzuca czar: Kul ognia!

🎯 WYMAGANIA:
    Stwórz klasę Mag dziedziczącą po klasie Gracz (z Zadania 1) z:
    - dodatkowym atrybutem: mana=100
    - metodą rzuc_czar(nazwa) zwracającą string z nazwą czaru
    - nadpisaną metodą przedstaw_sie() pokazującą także manę

📝 PRZYKŁAD UŻYCIA:
    mag = Mag("Gandalf", 5)
    print(mag.przedstaw_sie())
    print(mag.rzuc_czar("Kula ognia"))
"""

print()
print("5: Klasa dziedziczenie - PostacSpecjalna")
print()

