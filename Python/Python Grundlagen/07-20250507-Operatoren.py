# Operatoren

"""
Vergleichsoperatoren

    ==      Prüfung ob linke und rechte Seite gleich sind
    !=      Prüfung ob linke und rechte Seite ungleich sind
    <       Prüfung ob linke Seite kleiner als die rechte Seite ist
    <=      Prüfung ob linke Seite kleiner oder gleich der rechte Seite ist
    >       Prüfung ob linke Seite größer als die rechte Seite ist
    >=      Prüfung ob linke Seite größer oder gleich der rechte Seite ist
"""
print('Vergleichsoperatoren')
print('Ist 5 gleich 3? ' + str(5==3))
print('Ist 5 ungleich 3? ' + str(5!=3))
print('Ist 5 kleiner als 3? ' + str(5<3))
print('Ist 5 kleiner oder gleich 3? ' + str(5<=3))
print('Ist 5 größer als 3? ' + str(5>3))
print('Ist 5 größer oder gleich 3? ' + str(5>=3))

"""
Arithmetische Operatoren

    +       Addition
    -       Subtraktion
    *       Multiplikation
    **      Exponentation
    /       Division
    //      Ganzzahldivision
    %       Modulo / Restzahldivision
"""
print('\nArithmetische Operatoren')
print('5 + 3 = ' + str(5+3))
print('5 - 3 = ' + str(5-3))
print('5 * 3 = ' + str(5*3))
print('5 hoch 3 = ' + str(5**3))
print('5 / 3 = ' + str(5/3))
print('Ganzzahldivision mit 5 / 3 = ' + str(5//3))
print('5 % 3 = ' + str(5%3))

"""
Logische Operatoren

    and     UND-Verknüpfung
    or      ODER-Verknüpfung
    not     Negation
"""
print('\nLogische Operatoren')
print((4==5) and (1==1))
print((4==5) or (1==1))
print(not (1==1))

"""
Zuweisungsoperator und zusammengesetzte Operatoren

    =       Zuweisung                       - Der linken Seite wird der Wert der rechten Seite zugewiesen
    +=      Addition und Zuweisung          - Der linken Seite wird die Summe aus linker und rechter Seite zugewiesen
    -=      Subtraktion und Zuweisung       - Der linken Seite wird die Differenz aus linker und rechter Seite zugewiesen
    *=      Multiplikation und Zuweisung    - Der linken Seite wird das Produkt aus linker und rechter Seite zugewiesen
    /=      Division und Zuweisung          - Der linken Seite wird der Quotient aus linker und rechter Seite zugewiesen
    %=      Modulo und Zuweisung            - Der linken Seite wird das Ergebnis der Restzahldivision aus linker und rechter Seite zugewiesen
    **=     Exponentiation und Zuweisung    - Der linken Seite wird die Potenz aus linker und rechter Seite zugewiesen
    //=     Ganzzahldivision und Zuweisung  - Der linken Seite wird das Ergebnis der Ganzzahldivision aus linker und rechter Seite zugewiesen
"""
print('\nZuweisungsoperator und zusammengesetzte Operatoren')
x = 5
x += 3;
print('Erwartet 8: ' + str(x))
x -= 3;
print('Erwartet 5: ' + str(x))
x *= 3;
print('Erwartet 15: ' + str(x))
x /= 3;
print('Erwartet 5.0: ' + str(x))
x **= 3;
print('Erwartet 125.0: ' + str(x))
x //= 3;
print('Erwartet 41.0: ' + str(x))
x %= 3;
print('Erwartet 2.0: ' + str(x))

# Hinweis: Ab dem Zeitpunkt der Division wird mit Gleitkommewerten weitergerechnet.