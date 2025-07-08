```
# Verwendbare Werte
samples = result['results'][0]['data']['c']['samples']
samples_int = [int(s, 16) for s in samples]
print(samples_int)
```
Verwandelt die Ergebniss aus result = job.result() in lesbare (ha) Binärzahlen.

```
def csvBits(samples_int): 
    # Umwandeln in eine Liste von Listen
    memory_rows = [[bit] for bit in samples_int]
    with open("speicherpfad/dateiname.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(memory_rows)
```
Die Liste der Binärzahlen wird in eine CSV-Datei umgewandelt.

Gleiches passiert auch folgend, aber in Bytes und Dezimalzahlen:
```
#BYTES: 
def csvBytes(samples_int):
    bytes_list = [memory[i:i+8] for i in range(0, len(samples_int), 8)]
    with open("speicherpfad/dateiname.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(bytes_list)

#DEZIMALZAHLEN:
def csvDezimal(samples_int):
    # Mit Nullen auffüllen, damit die Länge durch 8 teilbar ist
    if len(memory) % 8 != 0:
        memory += ['0'] * (8 - len(memory) % 8)
    
    # In 8er-Gruppen (Bytes) unterteilen
    bytes_list = [samples_int[i:i+8] for i in range(0, len(samples_int), 8)]
    
    # Bytes zu Dezimalzahlen umwandeln
    decimal_values = [int(''.join(byte), 2) for byte in bytes_list]
    
    # In CSV schreiben
    with open("speicherpfad/dateiname.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for value in decimal_values:
            writer.writerow([value])  # Eine Dezimalzahl pro Zeile

```