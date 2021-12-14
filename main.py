import os
from grafika import *
from slova import *
from random import *

kontrol = []
zivoty = 7
hra_bezi = True
seed(42)
slovo = choice(hadana_slova)
tajenka = len(slovo) * ["_"]
print(slovo)
oznameni= ''
stav=''
# 1. Smyčka pro celou hru, hlídání životů
while hra_bezi and zivoty > 0:
    os.system('cls')
    print(f"Tajenka je: {''.join(tajenka)}")
    print(obesenec[ 7 - zivoty])
    print(oznameni)


# 2. Hádání slova/písmena - input()
    hadej = input("Hádej jednotlivá písmena, či zadej celé slovo: ")

# 3. Vyhodnocení výsledku hry

    #pokud je slovo správně
    if hadej == slovo:
        print("Uhádl jsi celé slovo!")
        hra_bezi = False


    elif hadej in kontrol and hadej in slovo:
        oznameni = 'Písmeno je již obsaženo!'

    elif hadej in kontrol and hadej not in slovo:
        oznameni = 'Pismeno neni a znovu si jej zadal'
        zivoty -= 1

    #pokud uhodne 1 písmeno
    elif len(hadej) == 1 and hadej in slovo and hadej != slovo:
        kontrol.append(hadej)
        #print("Uhodl jsi 1 písmeno, pokračuj dál.")
        oznameni = 'Uhodl jsi 1 písmeno, pokračuj dál.'
        for i, pismeno in enumerate(slovo):
            if pismeno == hadej:
                tajenka[i] = hadej
        if '_' not in tajenka:
            hra_bezi = False



    else:
        kontrol.append(hadej)
        zivoty -= 1
        print("Chyba")

else:

    if hra_bezi == False:
        print(f"Tajenka: '{slovo}', gratuluji k uhodnutí slova!")

    if zivoty == 0:

        print("Vyčerpal jsi pokusy. Konec hry.")
        print(obesenec.get(7))
        exit()



# TODO: Úklid výpisu v konzoli - os.system("cls")

# TODO: Vykreslení figurky
