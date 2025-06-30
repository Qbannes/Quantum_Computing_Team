# Rekursion

# Um eine Rekursion zu definieren ist es notwenidig den jeweiligen Algorithmus in einer Funktion unterzubringen
def rekursiv():
    print('Ich stürze ab')
    rekursiv() # Die Funktion rekursiv() ruft sich nun selbst wieder auf
    
# Um den Prozess in Gang zu bringen wird einmalig die Funktion rekursiv() aufgerufen
#rekursiv()


# Ausgeben der Zahlen von 1 bis 10 mittels einer Rekursion
def zaehlen1(n):
    # Abbruchbedingung: Sollte n größer oder gleich 10 sein, so wird die Aktuelle Funktion beendet
    if n > 10:
        return
    print(n)
    n += 1
    zaehlen1(n)
    
# Aufruf der Funktion mit der Zahl 1:
zaehlen1(1)


# Durch umstellen der Reihenfolge von Ausgabe und Rekursionsaufruf lässt sich die Zahlenreihe umdrehen
# Ausgeben der Zahlen von 10 bis 2 mittels einer Rekursion
def zaehlen2(n):
    # Abbruchbedingung: Sollte n größer oder gleich 10 sein, so wird die Aktuelle Funktion beendet
    if n >= 10:
        return
    n += 1
    zaehlen2(n)
    print(n)
    
# Aufruf der Funktion mit der Zahl 1:
zaehlen2(1)