```
from qiskit.circuit.library import HGate
from qiskit import QuantumCircuit
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService

# Quantencircuit erstellen
hadamard_gate = HGate()
circuit = QuantumCircuit(1)
circuit.append(hadamard_gate, [0])
circuit.measure_all()

# Festlegen des Simulators/Quantencomputers
backend = ...
 
# Convert to an ISA circuit
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(circuit)

# Anfrage schicken
job = backend.run(isa_circuit, shots = 100000, memory = True)

result = job.result()
memory = result.get_memory()
```
Das Quantencircuit mit einem Qubit berechnet mithilfe des Hadamard-Gatter und dank der Superposition einen echten 50/50 Zufall. [[01 - Hadamard-Gatter]]
ISA-Circuit: Angepasster Circuit, der auf der ausgewählten Hardware besser läuft. Wird automatisch generiert mit generate_preset_pass_manager.
!!! Memory gibt es bei neueren Versionen nicht mehr. Da muss man selbst die Werte aus result() übersetzen.