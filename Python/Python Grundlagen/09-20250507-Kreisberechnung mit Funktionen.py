# Damit die Bibliothek math im folgenden Programm zur Verfügung steht, muss diese importiert werden
import math

# Berechnungsvorschriften mittels Funktionen
# Funktionen werden durch 'def' eingeleitet, danach folgt der Name, danach die Parameterliste.Soll eine
# Funktion fertig sein und das Ergebnis zurückliefern, so wird dies mit dem Return-Statement gemacht.
def umfang(r):
    return (2 * math.pi * r)
    

def flaeche(r):
    return math.pi * r**2
    
    
def durchmesser(r):
    return 2 * r


print('Programm zur Kreisberechunng')
print('Dieses Programm berechnet anhand eines eingegebenen Radius verschiedene Kreiskennzahlen')

# Eingabe
radius = float(input('\nBitte geben Sie einen Radius ein (Kommazahlen mit einem Punkt eingeben):'))

# Ausgabe
# Hier werden direkt in der Ausgabe die oben definierten Funktionen genutzt.
print('Für einen Kreis mit dem Radius "' + str(radius) + '" ergeben sich folgende Kennzahlen:')
print('Umfang: ' + str(umfang(radius)))
print('Fläche: ' + str(flaeche(radius)))
print('Durchmesser: ' + str(durchmesser(radius)))