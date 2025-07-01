# Zufallszahlen generieren

# Importieren des random-Moduls - Dies muss immer geschehen,
# damit im folgenden die Funktionen des random-Moduls verwendet werden können
import random

# Zufallszahl im Bereich von 0 bis kleiner als 1 generieren
i = random.random()
print(i)

# Zufallszahl in einem Bereich zwischen 5 und 50 generieren
# Achtung! Die Endzahl ist NICHT im Bereich der Zufallszahlen
i = random.randrange(5, 51)
print(i)

# Bei der Funktion randint sind die Grenzen inklusive
i = random.randint(5,7) # identisch zu random.randrange(5,8)
print(i)

# Dokumentation: https://docs.python.org/3/library/random.html