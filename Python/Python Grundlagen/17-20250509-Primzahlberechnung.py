import math

# Algorithmus zur Primzahlberechnung
# Hier: Divisionsansatz

def ist_primzahl(n):
    # Es wird davon ausgegangen, dass die übergebene Zahl eine Primzahl ist
    prim = True
    
    # Alle Zahlen, die kleiner als 2 sind, sind keine Primzahlen
    if n < 2:
        prim = False

    # Die übergebene Zahl wird durch alle Zahlen geteilt, die kleiner oder gleich der Quadratwurzel der Zahl selbst sind. Bei der 2 wird angefangen
    k = 2
    
    while prim and k <= math.sqrt(n):
        # Sollte die übergebene Zahl durch den aktuellen Teiler teilbar sein, so kann es sich
        # nicht um eine Primzahl handeln und der Algorithmus ist beendet
        if n % k == 0:
            prim = False
        
        k += 1
        
    return prim


    
zahlen = {-1: False,
           0: False,
           1: False,
           2: True,
           3: True,
           4: False,
           5: True,
           6: False,
           7: True,
           8: False,
           9: False,
           10: False,
           11: True
           }

for zahl in zahlen:
    print(str(zahl) + " erwartet '" + str(zahlen[zahl]) + "': " + str(ist_primzahl(zahl)))
