# Damit die Bibliothek math im folgenden Programm zur Verfügung steht, muss diese importiert werden
import math

print('Programm zur Kreisberechunng')
print('Dieses Programm berechnet anhand eines eingegebenen Radius verschiedene Kreiskennzahlen')

# Eingabe
radius = float(input('\nBitte geben Sie einen Radius ein (Kommazahlen mit einem Punkt eingeben):'))

# Berechnung
umfang = 2 * math.pi * radius
flaeche = math.pi * radius**2
durchmesser = 2 * radius

# Ausgabe
print('Für einen Kreis mit dem Radius "' + str(radius) + '" ergeben sich folgende Kennzahlen:')
print('Umfang: ' + str(umfang))
print('Fläche: ' + str(flaeche))
print('Durchmesser: ' + str(durchmesser))