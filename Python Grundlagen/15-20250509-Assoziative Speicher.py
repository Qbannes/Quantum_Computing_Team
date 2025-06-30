# Assoziative Arrays / Dictionarys

# Definition eines dictionarys
dict1 = {
    "Zebra" : "Zebraallee 99, Zebrastadt",
    "Mustermann" : "Musterstr 47, Musterhausen",
    "Müller" : "Müllerweg 1, Müllerdorf"    
}

# Ausgabe
print(dict1)

print("\n------------\n")

# Zugriff auf ein bestimmtes Element
print(dict1["Zebra"])
print(dict1.get("Zebra"))

print("\n------------\n")

#Ein neues Element hinzufügen
dict1["Affe"] = "Affengasse 5, Affingen"
print(dict1)

print("\n------------\n")

# Nochmaliger Versuch dasselbe Element mit anderen Werten hinzuzufügen
dict1["Affe"] = "Affengasse 9, Affingen"
print(dict1)
# --> Es ist nicht möglich bei assoziativen Speichern einen doppelten Schlüssel zu haben

print("\n------------\n")

# Abfragen der Länge
print(len(dict1))

print("\n------------\n")

# Liste der Schlüssel
print(dict1.keys())
print(list(dict1.keys()))

print("\n------------\n")

# Liste der Werte
print(dict1.values())
print(list(dict1.values()))

print("\n------------\n")

# Liste der Schlüssel-Wert-Paare
print(dict1.items())
print(list(dict1.items()))

print("\n------------\n")

# Die Datentypen der Werte von Dictionaries müssen nicht übereinstimmen
dict2 = {
    "farbe" : "rot",
    "zahl" : 42,
    "wahrheitswert" : True,
    "Gleitkomma" : 47.11
}

print(dict2)

# Ansicht der Datentypen
for key in dict2:
    print(key + ' - ' + str(type(dict2.get(key))))
    
print("\n------------\n")

# Auch unterschiedliche Datentypen bei den Schlüsseln sind möglich
dict2[863.624] = "Dezimalzahl"
print(dict2)

print("\n------------\n")

# Löschen von Elementen
dict2.pop(863.624)
print(dict2)

# Löschen von nicht vorhandenen Elementen führt zu Laufzeitfehlern -> KeyError
# dict2.pop(863.624)

print("\n------------\n")

# Abfragen, ob ein Element existiert
if "farbe" in dict2:
    print("farbe vorhanden")
else:
    print("farbe nicht vorhanden")

print("\n------------\n")

# Löschen, bzw. ignorieren, wenn der Schlüssel nicht vorhanden ist
if 863.624 in dict2:
    dict2.pop(863.624)
    
print("\n------------\n")

# Dictionaries kopieren
dict3 = dict2.copy()
dict4 = dict(dict2)
print("dict2: " + str(dict2))
print("dict3: " + str(dict3))
print("dict4: " + str(dict4))

print()

# Werte verändern
dict2["farbe"] = 'blau'
dict3["farbe"] = 'lila'
dict4["farbe"] = 'grün'
print("dict2: " + str(dict2))
print("dict3: " + str(dict3))
print("dict4: " + str(dict4))

print("\n------------\n")

# Verschachtelte Dictionaries
familie = {
    "vater" : {
        "name" : "Max",
        "geburtsjahr" : 1950
    },
    "mutter" : {
        "name" : "Maxine",
        "geburtsjahr" : 1951
    },
    "kinder" : {
        "kind1" : {
            "name" : "Mäxchen",
            "geburtsjahr" : 1980
        },
        "kind2" : {
            "name" : "Mätzchen",
            "geburtsjahr" : 1981
        }
    }
}
print(familie)
print("Schlüssel: " + str(list(familie.keys())))
print("Schlüssel der Kinder: " + str(list(familie.get("kinder").keys())))
