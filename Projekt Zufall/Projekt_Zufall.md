# Projekt: Zufall


## Einführung

Zufaälle spielen eine zentrale Rolle in der Informatik, von Simulationen über Kryptografie bis hin zu Algorithmen des Maschinellen Lernens. Allerdings ist nicht jeder Zufall Gleich. Da wären die **klassischen Zufallsalgorithmen** die sogenannten PRNG (Pseudo Random Number Generator). Sie erzeugen nur scheinbar zufällige Zahlen. Sie sind deterministisch und basieren auf mathematische Abfolgen. **Quantencomputer** nutzen dagegen fundamentale Quantenprozesse wie Superposition und Kollaps, um echten Zufall zu generieren nach aktuellem Stand der Wissenschaft.

## Ziel des Projekts

Der Vergleich von klassischen Zufallsalgorithmen mit einem Quantenzufallsalgorithmus. Die Algorithmen werden eine Abfolge von **10.000** bis **100.000** Nullen und Einsen generieren. Die Datenreihe wird mittels statistischer Methoden und Tests Ausgewertet, mit der dann eine Aussage über Pseudozufall und echtem Zufall getroffen werden soll mit dem Ziel zu beweisen, dass Quantenzufallszahlen "echter" sind als klassische Pseudozufallszahlen.

Ein weiteres Ziel besteht darin, Interessenten und Praktikanten einen Einblick in den Beruf des Fachinformatikers für Daten- Und Prozessanalyse und in die Welt des Quantencomputing zu geben, die für den Einstieg relevant sind.

## Technische Mittel

Von den klassischen Zufallsalgorithmen wird das random-Modul von Python genutzt. Das Modul bedient sich dem Mersenne-Twister, der 32-Bit-Zahlen erzeugt mit einer guten statistischen Verteilung. Weiter werden alle für das Projekt benötigten Pakete in Python (Pandas, NumPy, Qiskit_IBM, Matplotlib) bereitgestellt. Das Ganze wird mit Python 3.13.5 ausgeführt im Jupyter Notebook, welches von Anaconda bereitgestellt wird.
Mitels dem Paket Qiskit_IBM werden die Quantenalgorithmen konzepiert. Die eigentliche Ausführung wird mittels Qiskit als Job an IBM gesandt, die diesen auf Quantenhardware anwendet und die Ergebnisse zurücksendet.
Die Dokumentationen und Aufzeichnungen gescheehn mittels Markdown und alle Ergebnisse und Dokumente werden im Repository Quantum_Computing_Team (https://github.com/Qbannes/Quantum_Computing_Team) hochgeladen.

## Klassische Zufallsgeneratoren (PRNGs)

Wie funktionieren sie?

    Pseudozufallszahlengeneratoren (PRNGs) nutzen einen Startwert (Seed) und eine mathematische Funktion, um eine deterministische, aber chaotisch aussehende Folge zu erzeugen.

        Beispiel: Der Mersenne Twister (in Python random verwendet) hat eine Periode von 219937−1219937−1.

    Probleme:

        Vorhersagbar, wenn der Seed bekannt ist.

        Bestimmte Muster können statistisch nachweisbar sein.

Beispiel: Python-PRNG

import random
random.seed(42)  # Fester Seed → reproduzierbare "Zufallsfolge"
zufallsbits = [random.randint(0, 1) for _ in range(100000)]

## Quantenzufallsgenerator (QRNGs)

Warum ist Quantenzufall anders?

    Ein Qubit in Superposition
$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$$
    ​kollabiert bei der Messung zufällig zu 0 oder 1.

    Anwendung: Kryptografie, Lotterien, wissenschaftliche Simulationen.

Beispiel: Quantenzufall mit Qiskit

from qiskit.circuit.library import HGate
from qiskit import QuantumCircuit
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService
from PIL import Image
import math


from qiskit_ibm_runtime.fake_provider import FakeAlmadenV2
from qiskit_aer import AerSimulator

hadamard_gate = HGate()
circuit = QuantumCircuit(1)
circuit.append(hadamard_gate, [0])
circuit.measure_all()

circuit.draw("mpl")

backend = AerSimulator(method='extended_stabilizer')
 
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(circuit)

job = backend.run(isa_circuit, shots = 100000, memory = True)

result = job.result()
memory = result.get_memory()
print(result)

## Statistische Analyse & Theoretische Grenzen

Wie vergleichen wir die Generatoren?

Als statistische Mittel werden Chi-Quadrat, Runs-p-Wert, Ljung-Box p, Lempel-Ziv, Max Power, Entropie, Pattern p-Wert eingesetzt, um die Generatoren miteinander zu vergleichen. 

Allerdings sind die statistischen Mittel begrenzt, da der Satz von Rice besagt, dass es keinen allgemeinen Algorithmus gibt, der für jede Folge beweist, ob sie "wirklich zufällig" ist. In der praktischen Konsequenz ziehen wir daraus, dass wir Pseudozufälle widerlegen, aber für echte Zufälle nur Plausabilitätsargumente liefern können.

