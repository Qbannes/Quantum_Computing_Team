print('5+3') # '5+3' wird als Text interpretiert und auch genau so ausgegeben

print(5+3)   # In dieser Zeile wird zunächst die Berechnung 5+3 ausgeführt und dann das Ergebnis 8 ausgegeben

# In den folgenden zwei Zeilen wird die Berechnung in einer Variablen 'summe' zwischengespeichert und dann ausgegeben
print('------------------')
summe = 5+4
print(summe)

# Im folgenden werden zwei Ganzzahlen in Variablen gespeichert, dann die Summe gebildet und zuletzt ausgegeben
print('------------------')
zahl1 = 4
zahl2 = 6
summe = zahl1 + zahl2
print(summe)

# Nun sollen die Zahlen von der Konsoleneingabe stammen. Der Benutzer gibt also auf der Konsole, die alle Zeichen
# als Text interpretiert ein und diese Werte werden nun in die Variablen 'zahl1' und 'zahl2' gespeichert.
# Eine Summe lässt sich von den beiden Texten nun aber nicht bilden - sehr wohl aber eine Verkettung.
# Daher steht in der Variablen 'summe' nun der Text aus 'zahl1' vor dem Text aus 'zahl2'. Der so verbundene
# Text wird dann mittels der print-Funktion ausgegeben.
print('------------------')
zahl1 = input("Zahl1:")
zahl2 = input("Zahl2:")
summe = zahl1 + zahl2
print(summe)

# Damit nun die Zahlen die der Benutzer eingibt als Zahlen interpretiert werden muss ein sogennanter
# Typecast stattfinden. Dies passiert für unsere Ganzzahlen mit dem Befehl 'int'.
print('------------------')
zahl1 = int(input("Zahl1:"))
zahl2 = int(input("Zahl2:"))
summe = zahl1 + zahl2
print(summe)