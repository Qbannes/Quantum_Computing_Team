# Schleifen

# Schleifen werden genutzt, um Code wiederholt auszuführen

# while-Schleife
# Beispiel 1: In diesem Beispiel werden die Zahlen 1 bis 10 ausgegeben
i = 1

while i <= 10:
    print(i)
    i += 1
    
print('\n---------------')

# Beispiel 2: Der Benutzer wird immer wieder nach einer Jahreszahl gefragt, bis er 'exit' eingibt
while True: # Definition einer Endlosschleife
    benutzereingabe = input('\nBitte geben Sie eine Jahreszahl ein: ')
    
    if benutzereingabe == 'exit':
        break   # Hiermit wird die Schleife abgebrochen, wenn der Benutzer das Wort 'exit' eingegeben hat

    print('Sie haben folgende Jahreszahl eingegeben: ' + benutzereingabe)
    
# Diese Zeile wird erst ausgegeben, wenn die Schleife verlassen wurde 
print('Das Programm wird nun beendet.')

print('\n---------------\n')

# Beispiel 3: else-Zweig der while-Schleife

i = 1

while i <= 10:
    print(i)
    i+=1
else:
    print('i ist nicht mehr kleiner oder gleich 10')
    
print('\n---------------\n')

"""
Der else-Zweig der while-Schleife wird nur ausgeführt, wenn die Schleifenbedingung nicht mehr erfüllt ist.
Wird die Schleife aus anderen Gründen beendet, so wird der else-Zweig nicht ausgeführt.
"""

i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 5:
        break
else:
    print('i ist nicht mehr kleiner oder gleich 10')  # Diese Zeile wird nun nicht mehr ausgegeben, da die Schleife nicht über eine unwahre Bedingung beendet wurde, sondern über einen Abbruch

print('\n---------------\n')

# Beispiel 4: Ausgabe aller geraden Zahlen bis 10
i = 1

while i <= 10:
    i += 1
    
    # Wenn es sich um eine ungerade Zahl handelt, dann soll beim Schleifenkopf fortgefahren werden.
    # Die Ausgabe wird also übersprungen
    if i % 2 != 0:
        continue
    
    print(i)


"""
Schleifensteuerungsbefehle

Mit 'break' lässt sich eine Schleife abbrechen.
Mit 'continue' wird sofort zum Schleifenkopf gewechselt und die Schleifenbedingung erneut überprüft.
Hierbei ist zu beachten, dass man nicht aus Versehen eine Endlosschleife generiert, weil der continue
Befehl ausgeführt wurde VOR der Veränderung des Schleifenzählers.
"""