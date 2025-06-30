# range()-Funktion

# Ausgabe des Containers mit den Zahlen von 1 bis 10
print(range(1, 11))

# Ausgabe des Container-Inhalts
print(list(range(1, 11)))

# Ausgabe der Zahlen von 1 bis 20, aber nur die geraden Zahlen
print(list(range(2, 21, 2)))

# Ausgabe der Zahlen von 7 bis 40, aber nur jede 5. Zahl
print(list(range(7, 41, 5)))

# Durchlaufen des Containers mit der for-Schleife
for zahl in range(7, 41, 5):
    print(zahl)

# Mit Hilfe der range-Funktion kann man eine for-Schleife simulieren, wie man sie beispielsweise aus
# Java her kennt.
for i in range(1, 11): # Java-Äquivalent: for(int i = 0; i <= 10; i++) {
    print(i)
    
# Wie würde nun eine for-Schleife aussehen, die in 2-er Schritten von 10 bis 0 abwärts zählen soll?
for i in range(10, -1, -2): # Java-Äquivalent: for(int i = 10; i >= 0; i-=2) {
    print(i)