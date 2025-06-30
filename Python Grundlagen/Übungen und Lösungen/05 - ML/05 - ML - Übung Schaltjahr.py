# ML - Übung Schaltjahr

# Aufgabenteil 1
def istSchaltjahr(jahr):
    # Prüfung auf int-Wert
    jahr = int(jahr)
    
    # Prüfung auf Schaltjahr
    # 1. Möglichkeit - Sie funktioniert zwar, aber elegant ist etwas anderes
    """
    if jahr % 4 == 0:
        if jahr % 100 == 0:
            if jahr % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    """
    
    # 2. Möglichkeit - Ausnutzung des Umstandes, dass eine Prüfung selbst schon ein boolean ist
    return (jahr % 400 == 0) or (jahr % 4 == 0 and jahr % 100 != 0)
    
    
# Testen der Funktion 'istSchaltjahr'
def testen():
    print('1900 - erwartet: False -> ' + str(istSchaltjahr(1900)))
    print('1904 - erwartet: True -> ' + str(istSchaltjahr(1904)))
    print('2000 - erwartet: True -> ' + str(istSchaltjahr(2000)))
    print('2022 - erwartet: False -> ' + str(istSchaltjahr(2022)))
    

# testen()


# Aufgabenteil 2
def aufgabe2():
    print('Dies ist ein Programm zur Schaltjahresabfrage')
    jahr = input('Bitte geben Sie eine Jahreszahl ein: ')
    
    print('Ist das Jahr ' + jahr + ' ein Schaltjahr? ' + str(istSchaltjahr(jahr)))


# aufgabe2()


# Aufgabenteil 3
def aufgabe3():
    while True:
        aufgabe2()
        print('\n---------------------\n')
        
        
# aufgabe3()


# Aufgabenteil 4
def aufgabe4():
    while True:
        print('Dies ist ein Programm zur Schaltjahresabfrage')
        jahr = input('Bitte geben Sie eine Jahreszahl ein: ')
    
        if jahr == 'exit':
            break    
        
        print('Ist das Jahr ' + jahr + ' ein Schaltjahr? ' + str(istSchaltjahr(jahr)))
        print('\n---------------------\n')
    

aufgabe4()