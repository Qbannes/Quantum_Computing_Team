# Formatieren in Python

# In Python gibt es sehr unterschiedliche Möglichkeiten Texte/Daten zu formatieren
# 1. %-Formatierung

name = "Max"
# %s ist ein Platzhalter für einen Wert, der nach dem %-Zeichen hinter
# dem Formatierungsstring angegeben wird
print("Hallo, %s!" % name)

# Auch Zahlen sind möglich
alter = 42
# %d steht für eine beliebige Ganzzahl
print("Hallo, %s! Du bist heute %d geworden." % (name, alter))

# Auch eine Auslagerung des Formatierungsstrings ist möglich
format = "Hallo, %s! Du bist heute %d geworden."
print(format % (name, alter))

# Darstellung einer Gleitkommazahl mit einem Prozentzeichen
lebenszeit=48.6
# %.1f bedeutet eine Gleitkommazahl mit einer Nachkommastelle
# %% ist die Darstellung des Prozentzeichens
print("Hallo, %s! Du bist heute %d geworden. Du hast bisher %.1f %% deines Lebens gelebt." % (name, alter, lebenszeit))

# Nachteil an der %-Formatierung ist, dass es schnell undurchsitig wird und man möglicherweise auch Variablen doppelt angeben muss

# --------------------------------------------------------

# 2. str.format()
# Etwas besser ist die format-Funktion, der String-Klasse

# Im Vergleich zur %-Formatierung werden bei der format-Funktion die Formatierungen in {} angegeben.
# Dies sorgt für eine bessere Übersichtlichkeit

name = "Max"
print("Hallo, {}!".format(name))

alter = 42
print("Hallo, {}! Du bist heute {} geworden.".format(name, alter))

# Die Variablen lassen sich auch genau adressieren
print("Hallo, {1}! Du bist heute {0} geworden.".format(alter, name))

# Auch Variablennamen können benutzt werden
print("Hallo, {name}! Du bist heute {alter} geworden.".format(alter=alter, name=name))

# Auch möglich ist die Angabe eines Dictionarys
person = {
    'name': 'Max',
    'alter': '42'
}
print("Hallo, {name}! Du bist heute {alter} geworden.".format(**person))


# Diesselben Formatierungsschreibweisen wie bei der %-Formatierung können auch bei der format-Funktion benuztzt werden

person = {
    'name': 'Max',
    'alter': 42,
    'lebenszeit': 48.6
}

print("Hallo, {name:s}! Du bist heute {alter:d} geworden. Du hast bisher {lebenszeit:.1f} % deines Lebens gelebt.".format(**person))

# Diesselbe Variable lässt sich auch mehrfach verwenden
zeit = 11
print("Uhrzeit {0}:{0}:{0}".format(zeit))

# --------------------------------------------------------

# 3. f-Strings
# Seit Python 3.6 stehen f-Strings zur Verfügung. Hiermit lassen sich Formatierungen noch einfacher darstellen,
# vor allem, wenn die Daten aus Variablen kommen

name = "Max"
print(f"Hallo, {name}!")

# Ob das f klein- oder großgeschrieben wird, ist unerheblich

alter = 42
print(F"Hallo, {name}! Du bist heute {alter} geworden.")

# Die f-Strings können auch rechnen
print(f"{4*5}")

# Funktionsaufrufe sind auch möglich
print(f"hallo {name.lower()}!")

def beispielfunktion():
    print("hm...")
    return "Test"

print(f"hallo {beispielfunktion()}!")

# --------------------------------------------------------

# f-Strings und Objekte
class Person:
    def __init__(self, vorname, alter):
        self.vorname = vorname
        self.alter = alter
    
    def __str__(self):
        return f"{self.vorname} ist {self.alter} Jahre alt."
    

neue_person = Person("Max", 21)
print(neue_person)

# --------------------------------------------------------

# f-Strings und längere Formatierungen

name = "Max"
alter = "42"
beruf = "Fachinformatiker"

nachricht = (
        f"Hallo {name}!\n"
        f"Jetzt bist du {alter} Jahre alt\n"
        f"Du bist {beruf}"
)

print(nachricht)

# --------------------------------------------------------

# Geschwindgkeitsvergleich zwischen %, format und f-String
import time

# %-Notation
start = time.time()
for i in range(0,10000000):
    name = "Max"
    alter = 42
    string = "%s ist %d Jahre alt" % (name, alter)
ende = time.time()

print(f"%-Notation:      {(ende-start)}s")

# format-Funktion
start = time.time()
for i in range(0,10000000):
    name = "Max"
    alter = 42
    string = "{} ist {} Jahre alt".format(name, alter)
ende = time.time()

print(f"format-Funktion: {(ende-start)}s")

# f-Strings
start = time.time()
for i in range(0,10000000):
    name = "Max"
    alter = 42
    string = f"{name} ist {alter} Jahre alt"
ende = time.time()

print(f"f-String:        {(ende-start)}s")

# --------------------------------------------------------

# Geschwindgkeitsvergleich zwischen %, format und f-String
import time

# %-Notation
start1 = time.time()
for i in range(0,10000):
    name = "Max"
    alter = 42
    print("%s ist %d Jahre alt" % (name, alter))
ende1 = time.time()

# format-Funktion
start2 = time.time()
for i in range(0,10000):
    name = "Max"
    alter = 42
    print("{} ist {} Jahre alt".format(name, alter))
ende2 = time.time()

# f-Strings
start3 = time.time()
for i in range(0,10000):
    name = "Max"
    alter = 42
    print(f"{name} ist {alter} Jahre alt")
ende3 = time.time()

print(f"%-Notation:      {(ende1-start1)}s")
print(f"format-Funktion: {(ende2-start2)}s")
print(f"f-String:        {(ende3-start3)}s")