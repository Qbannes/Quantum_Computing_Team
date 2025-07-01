"""
Verzweigung in Python mittels if
Bei Python sind Einrückungen essentiell! Hiermit werden zusammengehörige Blöcke definiert. Alle eingerückten
Zeilen die aufeinander folgen (ggf. auch mit Leerzeilen dazwischen) werden demselben Anweisungsblock
hinzugerechnet. Bei anderen Programmiersprachen wird hier häufig mit geschweiften Klammern gearbeitet {}
"""

wert = 5

if wert < 6:
    print('Der Wert ist kleiner als 6')
    print('Auch diese Zeile ist von der Bedingung betroffen')
print('Diese Zeile hingegen wird immer ausgegeben')

print('----------------')

wert = 6

if wert < 6:
    print('Der Wert ist kleiner als 6')
    print('Auch diese Zeile ist von der Bedingung betroffen')
print('Diese Zeile hingegen wird immer ausgegeben')

print('----------------')

# Die neuste Version von Python (Version 3) kann ebenfalls mit geschweiften Klammern umgehen.
# Allerdings ist diese Schreibweise für Python absolut unüblich
# Des Weiteren besteht die Einschränkung, dass nur eine Anweisungszeile in den Klammern stehen darf
wert = 6
if wert < 6: {
print('Der Wert ist kleiner als 6')
}
print('Diese Zeile hingegen wird immer ausgegeben')

print('----------------')
