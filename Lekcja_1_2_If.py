"""
Będziemy się uczyć:

    - Jak program podejmuje decyzje
    - Sprawdzanie warunków (if)
    - Alternatywne ścieżki (elif/else)  
    - Porównywanie wartości
    - Logiczne łączenie warunków

Przykład:

    wiek = int(input("Ile masz lat? "))
    if wiek >= 18:
        print("Jesteś pełnoletni!")
    else:
        print("Jesteś niepełnoletni!")

--------------------------------------

1.2 INSTRUKCJE WARUNKOWE (if/elif/else)

    📝 PODSTAWOWA SKŁADNIA
    
    Prosty if:
    
        wiek = 20
        if wiek >= 18:
            print("Jesteś pełnoletni!")
            
    if/else:
    
        wiek = 15
        if wiek >= 18:
            print("Jesteś pełnoletni!")
        else:
            print("Jesteś niepełnoletni!")
            
    if/elif/else:
    
        ocena = 4
        if ocena == 6:
            print("Celujący!")
        elif ocena == 5:
            print("Bardzo dobry!")
        elif ocena == 4:
            print("Dobry!")
        else:
            print("Inna ocena!")
        
    🔍 OPERATORY PORÓWNANIA
    
        ==      # równe
        !=      # różne
        >       # większe
        <       # mniejsze
        >=      # większe lub równe
        <=      # mniejsze lub równe
        
    🎯 OPERATORY LOGICZNE
    
        and     # i (oba warunki muszą być True)
        or      # lub (jeden warunek musi być True)
        not     # nie (odwraca wartość)

"""


# ZADANIE 1: Symulator rzutu kostką
"""
Wejście: Wynik rzutu kostką (1-6)
Wyjście: Opis wyniku

Efekt:
=== RZUT KOSTKĄ ===
Wynik rzutu: 6
WYGRAŁEŚ! Trafiłeś szóstkę!

🎯 PODPOWIEDŹ:
Dla 1: "Pech, jedynka!"
Dla 6: "WYGRAŁEŚ! Trafiłeś szóstkę!"
Dla innych: "Standardowy rzut: [liczba]"
"""

print("1; Symulator rzutu kostką")
print()

wynikRzutu = int(input("Rzuć kostką (1-6): "))

if wynikRzutu == 1: print("Brawo! Wyrzucileś jedynkę!")
elif wynikRzutu == 2: print("Brawo! Wyrzucileś dwójkę!")
elif wynikRzutu == 3: print("Brawo! Wyrzucileś trójkę!")
elif wynikRzutu == 4: print("Brawo! Wyrzucileś czwórkę!")
elif wynikRzutu == 5: print("Brawo! Wyrzucileś piątkę!")
else: print("Brawo! Wyrzucileś szustkę!")

# ZADANIE 2: Detektor pogodowy
"""
Wejście: Temperatura
Wyjście: Zalecenie ubioru

Efekt:
=== DETEKTOR POGODOWY ===
Podaj temperaturę: -5
ZALECENIE: Załóż kurtkę zimową i czapkę!

🎯 PODPOWIEDŹ:
poniżej 0: kurtka zimowa + czapka
0-15: lekka kurtka
16-25: bluza
powyżej 25: T-shirt
"""

print()
print("2. Detektor pogodowy")
print()

temperatura = float(input("Jaka jest temperatura na zewnątrz? "))

if temperatura < 0: print("kurtka zimowa + czapka")
elif temperatura <= 15: print("lekka kurtka")
elif temperatura <= 25: print("bluza")
else: print("T-shirt")

# ZADANIE 3: System poziomów gry
"""
Wejście: Punkty doświadczenia
Wyjście: Aktualny poziom gracza

Efekt:
=== SYSTEM POZIOMÓW ===
Podaj liczbę punktów: 350
Twój poziom: Ekspert

🎯 PODPOWIEDŹ:
0-99: Nowicjusz
100-249: Adept
250-499: Ekspert
500+: Mistrz
"""

print()
print("3. System poziomów gry")
print()

xp = int(input("Podaj liczbę punktów: "))

if xp < 0: print("Nie możesz mieć punktów na minusie!")
elif 100 > xp: print("Nowicjusz")
elif 250 > xp: print("Adept")
elif 500 > xp: print("Ekspert")
else: print("Mistrz")

# ZADANIE 4: Kalkulator dostawy
"""
Wejście: Waga paczki
Wyjście: Koszt dostawy

Efekt:
=== KOSZTY DOSTAWY ===
Podaj wagę paczki [kg]: 3.5
Koszt dostawy: 25.00 zł

🎯 PODPOWIEDŹ:
do 2 kg: 15 zł
2-5 kg: 25 zł
5-10 kg: 40 zł
powyżej 10 kg: "Za ciężka paczka"
"""

print()
print("4. Kalkulator dostawy")
print()

waga = float(input("Podaj wagę paczki [kg]: "))

if waga < 2: print("Koszt dostawy: 15zl")
elif waga >= 2 and 5 > waga: print("Koszt dostawy: 25zl")
elif waga >= 5 and 10 > waga: print("Koszt dostawy: 40zl")
else: print("powyżej 10 kg: \"Za ciężka paczka\"")

# ZADANIE 5: Generator horoskopu
"""
Wejście: Znak zodiaku
Wyjście: Losowa wróżba

Efekt:
=== GENERATOR HOROSKOPU ===
Podaj swój znak zodiaku: Lew
HOROSKOP: Czeka Cię niespodziewany zwrot wydarzeń!

🎯 PODPOWIEDŹ:
Dla 3-4 wybranych znaków daj różne wróżby, dla reszty: "Standardowy dzień"
"""

print()
print("5. Generator horoskopu")
print()

zodiak = input("Podaj swój znak zodiaku: ")

if zodiak.lower() == "baran": print("Dziś spotkasz interesującą osobę!")
elif zodiak.lower() == "lew": print("Czeka Cię niespodziewany zwrot wydarzeń!")
elif zodiak.lower() == "skorpion": print("Uważaj na fałszywe obietnice.")
elif zodiak.lower() == "wodnik": print("Stary problem wreszcie się rozwiąże.")
else: print("Standardowy dzień")