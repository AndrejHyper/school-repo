'''
Návštevníci jaskýň obdivujú ich výzdobu – kvaple. Zo stropu visia stalaktity (visiaky), z dna jaskyne vyrastajú zase stalagmity (stojáky). 
Niekedy sa spoja a vytvoria súvislý pilier (stalagnát).

Vytvorte program, ktorý pre vstupnú informáciu o jaskyni zistí, koľko je v nej visiakov a koľko stojákov. Prierez jaskyne budeme reprezentovať
tabuľkou, v ktorej 0 znamená vzduch a 1 horninu.

Na vstupe je v prvom riadku najprv jedno celé číslo – počet riadkov tabuľky, ktoré nasledujú. Oddeľovačom hodnôt v riadkoch tabuľky je čiarka.

Na výstupe najprv vypíšte počet visiakov, potom počet stojákov.

Oddeľovačom výstupných hodnôt je tiež čiarka.

Každá „jaskyňa” musí mať aspoň jeden riadok, počet stĺpcov môže byť rôzny. Na niektorých miestach jaskyne nie sú žiadne kvaple,
na niektorých miestach je visiak aj stoják, niekde sa zase možno spojili do súvislého piliera. Niektoré kvaple sú kratšie, iné dlhšie. 
V prvom príklade vstupu vidíme, že v tejto „jaskyni” sú 3 visiaky a 2 stojáky:

Vstup:
4
1,1,1,0,1,1,0
1,1,1,0,0,1,0
1,1,0,1,1,1,0
0,1,0,1,1,1,0
Výstup:
3,2


Vstup:
3
1,1,1,1
1,0,1,1
0,0,0,1
Výstup:
3,0


Vstup:
height =1
cave = [1,1,1,0,0]
Výstup:
0,0



Vstup ešte raz:

Výstup:
3,2
'''
height = 4
cave = [
    [1,1,1,0,1,1,0],
    [1,1,1,0,0,1,0],
    [1,1,0,1,1,1,0],
    [0,1,0,1,1,1,0]
]


def find_rocks(cave, height):
    stalagtite = 0
    stalagmite = 0
    for x in range(len(cave[0])):
        if cave[0][x] == 1:
            for y in range(height-1):
                if cave[y+1][x] == 0:
                    stalagtite += 1
                    break

    for x in range(len(cave[0])):
            if cave[-1][x] == 1:
                for y in range(height-1, 0, -1):
                    if cave[y][x] == 0:
                        stalagmite += 1
                        break
    
    return stalagtite, stalagmite

print(find_rocks(cave, height))
