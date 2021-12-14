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

#Smyčka pro celou hru, hlídání životů
while hra_bezi and zivoty > 0:
    os.system('cls')
    print(f"Tajenka je: {''.join(tajenka)}")
    print(obesenec[ 7 - zivoty])
    print(oznameni)



    hadej = input("Hádej jednotlivá písmena, či zadej celé slovo: ")



    #pokud je slovo správně
    if hadej == slovo:
        print("Uhádl jsi celé slovo!")
        hra_bezi = False

    #pokud zadáš písmeno, které si již zadal a je součástí tajenky
    elif hadej in kontrol and hadej in slovo:
        oznameni = 'Písmeno je již obsaženo!'

    #pokud zadáš písmeno, které si již zadal a není součástí tajenky
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


    #pokud si zadal špatné písmeno
    else:
        kontrol.append(hadej)
        zivoty -= 1
        print("Chyba")

else:
    #pokud si uhodl správné slovo, cyklus je ukončen a přesměrován na tuhle podmínku
    if hra_bezi == False:
        print(f"Tajenka: '{slovo}', gratuluji k uhodnutí slova!")

    # pokud vyčerpáš všechny pokusy
    if zivoty == 0:
        print("Vyčerpal jsi pokusy. Konec hry.")
        print(obesenec.get(7))
        exit()