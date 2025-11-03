"""
1.1 PODSTAWY SKŁADNI PYTHON

    📝 ZMIENNE I TYPY DANYCH
    
        imie = "Anna"                               # str - tekst
        wiek = 25                                   # int - liczba całkowita  
        wzrost = 1.75                               # float - liczba dziesiętna
        czy_student = True                          # bool - True/False
        
    🔢 OPERATORY
    
        # Arytmetyczne
    
            5 + 3                                   # 8 - dodawanie
            10 / 3                                  # 3.333 - dzielenie
            2 ** 3                                  # 8 - potęgowanie

        # Porównania
    
            5 == 5                                  # True - równe
            5 != 3                                  # True - różne
            5 > 3                                   # True - większe

        # Logiczne
    
            True and False                          # False
            True or False                           # True
            not True                                # False
    
    💬 KOMENTARZE
    
        # Komentarz jednolinijkowy

            \"""
                Komentarz
                wielolinijkowy
            \"""

            imie = "Jan"  # Komentarz obok kodu
    
    ⌨️ WEJŚCIE/WYJŚCIE
    
        # Wyświetlanie
    
            print("Hello World!")
            print(f"Witaj {imie}!")                 # f-string

        # Pobieranie danych
    
            imie = input("Podaj imię: ")
            wiek = int(input("Podaj wiek: "))       # tekst na liczbę

"""

# Kalkulator

print("1. Kalkulator:")
waga = float(input("Podaj ile kg. ważysz: "))
wzrost = float(input("Wprowadź jaki masz zwrost (w metrach): "))

bmi = waga/wzrost**2
print(f"Twoje BMI to {bmi:.2f}")


# Konwerter temperatur

print("")
print("2. Konwerter temperatur:")
temperatura = float(input("Wprowadź temperature w °C: "))

farenhait = (temperatura * 9 / 5) + 32
print(f"{temperatura:.2f}°C = {farenhait:.2f}°F")


# Pole prostokąta

print("")
print("3. Pole prostokąta:")
dlugosc = int(input("Wprowadź dlugość boku: "))
szerokosc = int(input("Wprowadź szerokość boku: "))

pole = dlugosc * szerokosc
print(f"Pole prostokąta to: {pole}")


# Konwerter walut

print("")
print("4. Konwerter walut:")

kwota = float(input("Podaj kwotę: "))

euro = kwota / 4.5
print(f"{kwota} PLN = {euro:.2f} EUR")


# Średnia ocen

print("")
print("5. Średnia ocen:")

ocA = int(input("Wprowadź 1 ocene: "))
ocB = int(input("Wprowadź 2 ocene: "))
ocC = int(input("Wprowadź 3 ocene: "))

srednia = (ocA + ocB + ocC) / 3
print(f"Średnia ocen {ocA}, {ocB}, {ocC} to {srednia:.1f}")