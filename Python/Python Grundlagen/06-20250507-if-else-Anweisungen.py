# if-else-Anweisung

# Wenn nun neben der Prüfung und dem DANN-Ergebnis auch noch der Teil WENN NICHT benötigt wird, so muss die
# if-Anweisung um einen else-Teil erweitert werden.

y = 5

if y == 4:
    print('y ist vier')
else:
    print('y ist nicht vier')
    
    
# Nun kann es aber auch sein, dass man mehrere Prüfungen vornehmen möchte. Dies lässt sich mit der if-elif-else-Syntax machen
y = 5

if y == 4:
    print('y ist vier')
elif y == 5:
    print('y ist fünf')
else:
    print('y ist weder vier noch fünf')
    
print('-----------------')

y = 3

if y == 4:
    print('y ist vier')
elif y == 5:
    print('y ist fünf')
else:
    print('y ist weder vier noch fünf')
    
# Folgende Fehler treten gerade am Anfang häufig auf:
# 1. Die Einrückungen werden falsch gesetzt. Diese sind allerdings für Python zwingend korrekt einzuhalten
# 2. statt elif wird elseif geschrieben
# 3. statt einem Vergleich mit == wird eine Zuweisung mit = versucht
# 4. Der Doppelpunkt am Ende einer Prüfungszeile fehlt
# 5. Es wurde nicht auf Groß-/Kleinschreibung geachtet. Python ist allerdings Case-Sensitive!