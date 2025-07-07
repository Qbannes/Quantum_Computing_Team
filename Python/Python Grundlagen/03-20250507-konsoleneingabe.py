"""
Dieses Programm fragt den Benutzer nach einer Eingabe auf der Konsole. Dabei wird zunächst der Text
'Bitte geben Sie etwas ein und bestätigen mit der "Enter"-Taste' ausgegeben. Danach hat der Benutzer
nun die Möglichkeit selbst etwas auf der Konsole einzugeben und dieses dem Programm mitzuteilen. Die
eingegebenen Zeichen werden dann in der Variable mit dem Namen 'variable' zwischengespeichert. In der
letzten Zeile wird die Variable an die Funktion 'print' übergeben und somit der vom Benutzer zur
Laufzeit des Programms eingegebenen Text wieder ausgegeben.
"""

variable = input('Bitte geben Sie etwas ein und bestätigen mit der "Enter"-Taste: ')

print('Folgendes haben Sie eingegeben:')
print(variable)