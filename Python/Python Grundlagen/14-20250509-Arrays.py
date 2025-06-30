# Array

"""
Bei einem Array (zu deutsch auch Feld genannt) handelt es sich um einen Container für mehrere Elemente
desselben Datentyps.
Beispiel Einkaufsliste: In einer Einkaufsliste kann es beliebig viele Elemente des Datentyps text/string geben
"""
einkaufsliste = [
        "Brötchen",
        "Joghurt",
        "Eier",
        "Milch"
    ]
    
# Ausgeben eines Arrays
print(einkaufsliste)

print('--------------------')

# Länge eines Arrays abfragen
print(len(einkaufsliste))

print('--------------------')

# Gezielt ein bestimmtes Element ansprechen
# ACHTUNG! Es wird normalerweise bei der Zahl 0 angefangen zu zählen. Aber nicht bei allen
# Programmiersprachen ist dies so. SQL fängt beispielsweise mit der 1 an zu zählen.
print(einkaufsliste[1])

# Zugriff auf das Element 4 - dieses liegt ausserhalb unserer einkaufsliste
# Das Ergebnis ist ein Laufzeitfehler: "IndexError: list index out of range"
# Ein solcher zugriffsfehler lässt das Programm abstürzen!
# print(einkaufsliste[4])

print('--------------------')

# Nachträglich einer Liste weitere Werte hinzufügen (nicht alle Programmiersprachen unterstützen dies)
einkaufsliste.append("Butter")
print(einkaufsliste)
print(len(einkaufsliste))

print('--------------------')

# Nachträglich Elemente entfernen. Der Index der darauf folgenden Elemente wird angepasst.
einkaufsliste.remove("Eier")
print(einkaufsliste)
print(len(einkaufsliste))

# Wird versucht ein Element zu entfernen, welches nicht in der Liste vorhanden ist, so gibt es einen
# ValueError und das Programm stürzt ab.
# einkaufsliste.remove("Eier")

print('--------------------')

# Ersetzen eines bestimmten Elementes
einkaufsliste[1] = "Quark"
print(einkaufsliste)

print('--------------------')

# Sortieren einer Liste
einkaufsliste.sort()
print(einkaufsliste)

print('--------------------')

# Umdrehen der Reihenfolge. Wenn zuvor keine Sortierung gemacht wurde, dann erreicht man hiermit auch keine
# Absteigende Sortierung, da reverse selbst nicht sortiert, sondern eben nur die Reihenfolge umdreht.
einkaufsliste.reverse()
print(einkaufsliste)

print('--------------------')

# Index eines Elementes herausfinden
print(einkaufsliste.index("Butter"))

# Wird versucht den Index eines Elementes zu suchen, welches nicht in der Liste vorhanden ist, so gibt es einen
# ValueError und das Programm stürzt ab.
# print(einkaufsliste.index("Eier"))

print('--------------------')

# Um zu überprüfen, ob ein Element in der Liste vorhanden ist kann man den Operator "in" benutzen
print("Butter" in einkaufsliste)
print("Eier" in einkaufsliste)

# Daraus ergibt sich, wenn man ein Element löschen möchte, aber nicht weiß ob es vorhanden ist, sollte
# man zunächst prüfen, ob das entsprechende Element vorhanden ist
if "Eier" in einkaufsliste:
    einkaufsliste.remove("Eier")
    
print('--------------------')

# Eine Liste zu einer Liste hinzufügen. Die 2. Liste befindet sich dann am Ende der ersten Liste
einkaufsliste2 = ["Joghurt", "Schinken"]
einkaufsliste.extend(einkaufsliste2)
print(einkaufsliste)
print(len(einkaufsliste))

print('--------------------')

# Referenzkopie auf eine Liste
einkaufsliste2 = einkaufsliste
print("Liste1: " + str(einkaufsliste))
print("Liste2: " + str(einkaufsliste2))

# Einen Wert in der ersten Liste verändern
einkaufsliste[3] = "Brot"
print("Liste1: " + str(einkaufsliste))
print("Liste2: " + str(einkaufsliste2))

# ACHTUNG!! Hierbei wurde KEINE Kopie erstellt, sondern BEIDE Variablen zeigen auf diesselbe Liste.
# Wird über eine der beiden Variablen die Liste verändert, so kann man die veränderte Liste auch über
# die andere Variable erreichen

print('--------------------')

# Kopie einer Liste erstellen
einkaufsliste2 = einkaufsliste.copy()
print("Liste1: " + str(einkaufsliste))
print("Liste2: " + str(einkaufsliste2))

# Einen Wert in der ersten Liste verändern
einkaufsliste[3] = "Brötchen"
print("Liste1: " + str(einkaufsliste))
print("Liste2: " + str(einkaufsliste2))

# Bei diesem Beispiel wurde nun eine echte Kopie angelegt, daher unterscheiden sich die beiden Listen am Ende

print('--------------------')

# Liste vollständig leeren
einkaufsliste2.clear()
print(einkaufsliste2)

print('--------------------')

# Durchgehen einer Liste mittels einer for-Schleife
for nahrungsmittel in einkaufsliste:
    print(nahrungsmittel + " - Index in Liste: " + str(einkaufsliste.index(nahrungsmittel)))