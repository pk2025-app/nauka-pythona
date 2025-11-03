# range(start, stop, krok) - generuje sekwencję liczb
#   start - od której liczby zaczynamy (domyślnie 0)
#   stop - do której liczby (nie włącznie)
#   krok - co ile liczb (domyślnie 1)

# type(zmienna) - zwraca typ zmiennej
#   zmienna - zmienna do sprawdzenia typu

# round(liczba, miejsca) - zaokrągla liczbę
#   liczba - liczba do zaokrąglenia
#   miejsca - do ilu miejsc po przecinku (domyślnie 0)

print("1. Odliczanie od 10 do 1: ")
print("")

for i in range(10, 0, -1):
    print(i)

print("")
print("2. Sprawdź typy 4 różnych zmiennych: ")
print("")

liczba = 10
poPrzecinku = 4.23
napis = "Prosty napis"
test = False

print(f"Typ zmiennej [{liczba}] to {type(liczba)}")
print(f"Typ zmiennej [{poPrzecinku}] to {type(poPrzecinku)}")
print(f"Typ zmiennej [{napis}] to {type(napis)}")
print(f"Typ zmiennej [{test}] to {type(test)}")

print("")
print("3. Zaokrąglij π do 3 miejsc po przecinku: ")
print("")

pi = 3.1415926535
print(f"Liczba PI ({pi}) skrócona do 3 miejsc po przecinku: {round(pi, 3)}")