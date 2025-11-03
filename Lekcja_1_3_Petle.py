"""
🎯 1.3 PĘTLE (FOR/WHILE)
    📝 PODSTAWOWA SKŁADNIA
        Pętla FOR - gdy wiesz ILE razy
        # Powtórz 5 razy
            for i in range(5):
                print(f"Powtórzenie nr {i}")
                
        Pętla WHILE - gdy wiesz KIEDY skończyć
        # Powtarzaj dopóki warunek jest True
            liczba = 0
            while liczba < 5:
                print(liczba)
                liczba += 1         # Zwiększ liczbę o 1
                
    🔧 PRZYDATNE FUNKCJE
            range(5)                # 0, 1, 2, 3, 4
            range(1, 6)             # 1, 2, 3, 4, 5  
            range(1, 10, 2)         # 1, 3, 5, 7, 9 (co 2)
    ⚡ INSTUKCJE STERUJĄCE
            break                   # Natychmiast przerwij pętlę
            continue                # Przejdź do następnej iteracji
"""

# ZADANIE 1: Odliczanie startowe

"""
Wejście: Liczba startowa
Wyjście: Odliczanie 3...2...1...START!

Efekt:
    === ODLICZANIE ===
    Podaj liczbę startową: 3
    3...
    2...
    1...
    START!

🎯 PODPOWIEDŹ:
    Użyj pętli for z range(liczba, 0, -1)
"""

print("1: Odliczanie startowe")
print()

start = int(input("Podaj liczbe startową: "))
print("Odliczam do startu:")

for i in range (start, 0, -1):
    print(f"{i}...")

print("Start!")

# ZADANIE 2: Sumator liczb

"""
Wejście: 5 liczb od użytkownika
Wyjście: Suma wszystkich liczb

Efekt:
    === SUMATOR LICZB ===
    Podaj liczbę 1: 5
    Podaj liczbę 2: 3
    Podaj liczbę 3: 2
    Podaj liczbę 4: 8
    Podaj liczbę 5: 1
    Suma: 19
    
🎯 PODPOWIEDŹ:
    Użyj pętli for i in range(5) i dodawaj do zmiennej suma
"""

print()
print("2: Sumator liczb")
print()

suma = 0

for i in range (1, 6):
    liczba = int(input(f"Wprowadź liczbę nr {i}... "))
    suma += liczba

print()
print(f"Wynik dodawania wszystkich liczb to: {suma}.")

# ZADANIE 3: Gra w zgadywanie

"""
Wejście: Liczby aż użytkownik zgadnie (wylosowana: 7)
Wyjście: Informacje "za mało/za dużo/trafiłeś!"

Efekt:
    === GRA W ZGADYWANIE ===
    Zgadnij liczbę: 5
    Za mało!
    Zgadnij liczbę: 10
    Za dużo!
    Zgadnij liczbę: 7
    Trafiłeś! Liczba prób: 3

🎯 PODPOWIEDŹ:
    Użyj pętli while True i break gdy trafi
"""

print()
print("3: Gra w zgadywanie")
print()

liczba = int(input("Wprowadz liczbę: "))
szukana = 6
proby = 1

while liczba != szukana:
    if szukana - liczba > 0:
        liczba = int(input("Liczba za mala... spróbuj ponownie... "))
    elif szukana - liczba < 0:
        liczba = int(input("Liczba za duża... spróbuj ponownie... "))
    proby = proby + 1
            
print(f"Brawo! Zgadles liczbe :) bylo to {szukana}. Ilość prób: {proby}")

# ZADANIE 4: Generator tabliczki mnożenia

"""
Wejście: Liczba (np. 5)
Wyjście: Tabliczka mnożenia 1-10

Efekt:
    === TABLICZKA MNOŻENIA ===
    Podaj liczbę: 5
    5 x 1 = 5
    5 x 2 = 10
    ...
    5 x 10 = 50
    
🎯 PODPOWIEDŹ:
    Użyj pętli for i in range(1, 11)
"""

print()
print("4: Generator tabliczki mnożenia")
print()

liczba = int(input("Podaj liczbe: "))

for i in range (1, 11):
    print(f"{liczba} x {i} = {liczba * i}")

# ZADANIE 5: Bankomat - wypłata

"""
Wejście: Kwota do wypłaty
Wyjście: Nominały 100, 50, 20, 10 zł

Efekt:
    === SYMULATOR BANKOMATU ===
    Podaj kwotę do wypłaty: 380
    Wypłacone nominały:
    100 zł x 3
    50 zł x 1
    20 zł x 1
    10 zł x 1

🎯 PODPOWIEDŹ:
    Użyj pętli while kwota > 0 i sprawdzaj nominały od największych
"""

print()
print("5: Bankomat - wypłata")
print()

kwota = int(input("Podaj kwotę do wyplaty: "))
kwota2 = kwota
print("Wyplacam...")

setki = 0
piecdziesiatki = 0
dwudziestki = 0
dziesiatki = 0
piatki = 0
dwojki = 0
zlotowki = 0

while kwota != 0:
    if kwota >= 100:
        kwota = kwota - 100
        setki = setki + 1
        continue
    elif kwota >= 50:
        kwota = kwota - 50
        piecdziesiatki = piecdziesiatki + 1
        continue
    elif kwota >= 20:
        kwota = kwota - 20
        dwudziestki = dwudziestki + 1
        continue
    elif kwota >= 10:
        kwota = kwota - 10
        dziesiatki = dziesiatki + 1
        continue
    elif kwota >= 5:
        kwota = kwota - 5
        piatki = piatki + 1
        continue
    elif kwota >= 2:
        kwota = kwota - 2
        dwojki = dwojki + 1
        continue
    else:
        kwota = kwota - 1
        zlotowki = zlotowki + 1
        
print(f"{kwota2} PLN zostalo wyplacone w nominalach:")
print(f"100zl : {setki}")
print(f"50zl : {piecdziesiatki}")
print(f"20zl : {dwudziestki}")
print(f"10zl : {dziesiatki}")
print(f"5zl : {piatki}")
print(f"2zl : {dwojki}")
print(f"1zl : {zlotowki}")