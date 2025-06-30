def maximum(a, b):
    # Prüfung, ob die übergebenen Werte Ganzzahlen sind
    a = int(a)
    b = int(b)
    
    # Ergebnis vorfestlegen mit a
    result = a
    
    # Wenn b größer ist als a, dann wird b auf die Ergebnisvariable geschrieben
    if b > a:
        result = b
        
    # Ergebnis zurückgeben
    return result


# Ausprobieren der Funktion
a = 6
b = 7
print(maximum(a,b))