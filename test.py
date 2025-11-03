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
import os

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