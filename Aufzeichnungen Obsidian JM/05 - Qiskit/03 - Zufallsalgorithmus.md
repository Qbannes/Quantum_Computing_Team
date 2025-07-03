$$
|0\rangle \to \fbox{H} \to \fbox{Messung} \to \text{Zufallszahl}
$$
```
simulator = FakeAlmadenV2()
shots = 500

gesamt_counter0 = 0
gesamt_counter1 = 0

for i in range(0, 1000):
    job = simulator.run(qc, shots=shots)  # Nur zehn Schuss für ein Zufallsbit
    result = job.result()
    counts = result.get_counts()
    for bitstring, anzahl in counts.items():
        for bit in bitstring:
            if bit == '0':
                gesamt_counter0 += anzahl
            elif bit == '1':
                gesamt_counter1 += anzahl
```
500000 zufällige Bits werden erstellt und gezählt.
```
Beispiel Darstellung:

names = ["0", "1"]
counte = [gesamt_counter0, gesamt_counter1]
plt.bar(names, counte)
plt.show()
print(counte)
```
![[Pasted image 20250703123622.png]]
