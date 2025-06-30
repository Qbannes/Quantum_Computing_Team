# for-Schleife
# Die for-Schleife in Python wird dazu genutzt um eine Iteration über eine Sequenz von Objekten durchzuführen

# Definition eines Arrays (Einer Liste von Elementen)
sprachen = ['Deutsch', 'Englisch', 'Französisch', 'Spanisch', 'Schwedisch']

# for-Schleife, um den Container 'sprachen' einmal vollständig durchzugehen
for sprache in sprachen:
    print(sprache)
    
print('------------')

# Auch die for-Schleife kann einen else-Zweig besitzen
for sprache in sprachen:
    print(sprache)
else:                   # Der else-Zweig wird ausgeführt, wenn die Schleife den Container vollständig durchlaufen hat
    print('Keine weiteren Sprachen gefunden - Ausführung fertig')
    
    
print('------------')

# Bei einem Abbruch der Schleife, wird der else-Zweig nicht ausgeführt
for sprache in sprachen:
    if sprache == 'Französisch':
        break
    print(sprache)
else:                   # Der else-Zweig wird ausgeführt, wenn die Schleife den Container vollständig durchlaufen hat
    print('Fertig')
