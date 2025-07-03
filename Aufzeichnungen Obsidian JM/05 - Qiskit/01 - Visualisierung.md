![[7midpcuv.png]]

```
from qiskit import QuantumCircuit
from qiskit.circuit.library import HGate

hadamard_gate = HGate()

qc = QuantumCircuit(5, 5) # Qubist und klassische Bits initialisieren
qc.append(hadamard_gate, [0])
qc.append(hadamard_gate, [1]) # Hadamard-Gatter zum ersten und zweiten Qubit hinzufügen
qc.measure(
    range(5), range(5)
) # Alle Qubits messen, Ergebnisse in klassischen Bits speichern
qc.draw("mpl") # Visualisieren
```
Visualisierung des Quantencircuits
![[Pasted image 20250703093539.png]]

