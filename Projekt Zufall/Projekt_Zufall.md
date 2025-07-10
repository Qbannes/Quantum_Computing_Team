# Projekt: Zufall
07.07.2025

## Einführung

Zufälle spielen eine zentrale Rolle in der Informatik, von Simulationen über Kryptografie bis hin zu Algorithmen des Maschinellen Lernens. Allerdings ist nicht jeder Zufall Gleich. Da wären die **klassischen Zufallsalgorithmen** die sogenannten PRNG (Pseudo Random Number Generator). Sie erzeugen nur scheinbar zufällige Zahlen. Sie sind deterministisch und basieren auf mathematische Abfolgen. **Quantencomputer** nutzen dagegen fundamentale Quantenprozesse wie Superposition und Kollaps, um echten Zufall zu generieren nach aktuellem Stand der Wissenschaft.

## Ziel des Projekts

Der Vergleich von klassischen Zufallsalgorithmen mit einem Quantenzufallsalgorithmus. Die Algorithmen werden eine Abfolge von **10.000** bis **100.000** Nullen und Einsen generieren. Die Datenreihe wird mittels statistischer Methoden und Tests Ausgewertet, mit der dann eine Aussage über Pseudozufall und echtem Zufall getroffen werden soll mit dem Ziel zu beweisen, dass Quantenzufallszahlen "echter" sind als klassische Pseudozufallszahlen.

Ein weiteres Ziel besteht darin, Interessenten und Praktikanten einen Einblick in den Beruf des Fachinformatikers für Daten- Und Prozessanalyse und in die Welt des Quantencomputing zu geben, die für den Einstieg relevant sind.

## Technische Mittel

Von den klassischen Zufallsalgorithmen wird das random-Modul von Python genutzt. Das Modul bedient sich dem Mersenne-Twister, der 32-Bit-Zahlen erzeugt mit einer guten statistischen Verteilung. Weiter werden alle für das Projekt benötigten Pakete in Python (Pandas, NumPy, Qiskit_IBM, Matplotlib) bereitgestellt. Das Ganze wird mit Python 3.13.5 ausgeführt im Jupyter Notebook, welches von Anaconda bereitgestellt wird.
Mitels dem Paket Qiskit_IBM werden die Quantenalgorithmen konzepiert. Die eigentliche Ausführung wird mittels Qiskit als Job an IBM gesandt, die diesen auf Quantenhardware in Sherbrooke anwendet und die Ergebnisse auf der IBM Plattform bereitstellt. 
Die Dokumentationen und Aufzeichnungen gescheehn mittels Markdown und alle Ergebnisse und Dokumente werden im Repository Quantum_Computing_Team (https://github.com/Qbannes/Quantum_Computing_Team) hochgeladen.

## Klassische Zufallsgeneratoren (PRNGs)
Pseudozufallszahlengeneratoren (PRNGs) nutzen einen Startwert (Seed) und eine mathematische Funktion, um eine deterministische, aber chaotisch aussehende Folge zu erzeugen. Beispielsweise ist der PRNG von Python (random) hat eine Periode von 219937−1219937−1. Das Problem hierbei ist, dass bestimmte Muster statistisch immer nachweisbar sein können und der Algorithmus vorhersagbar ist durch den gesetzten Seed.
Beispiel: Python-PRNG

**import random**                 

**random.seed(42)**  


**zufallsbits = [random.randint(0, 1) for _ in range(10)]**

Als Ausgabe erhalten wir in diesem Fall immer **[0, 0, 1, 0, 0, 0, 0, 0, 1, 0]**

## Quantenzufallsgenerator (QRNGs)
Quantenzufallsgeneratoren haben keinen Startwert sie nutzen den Superpositionszustand, der entsteht wenn ein Qubit das Hadamard-Gatter passiert bzw. pyhsikalisch in den Superpositionszustand gebracht wird. Mit der Messung also dem Hinschauen nimmt das Qubit einen der beiden Zustände null oder eins an und das zufällig. 

    Ein Qubit in Superposition
$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$$
    ​kollabiert bei der Messung zufällig zu 0 oder 1.

Beispiel: Quantenzufall mit Qiskit

**from qiskit.circuit.library import HGate**
**from qiskit import QuantumCircuit**
**from qiskit.transpiler import generate_preset_pass_manager**
**from qiskit_ibm_runtime import QiskitRuntimeService**
**from PIL import Image**
**import math**


**from qiskit_ibm_runtime.fake_provider import FakeAlmadenV2**
**from qiskit_aer import AerSimulator**

**hadamard_gate = HGate()**
**circuit = QuantumCircuit(1)**
**circuit.append(hadamard_gate, [0])**
**circuit.measure_all()**

**circuit.draw("mpl")**

**backend = AerSimulator(method='extended_stabilizer')**
 
**pm = generate_preset_pass_manager(backend=backend, optimization_level=1)**
**isa_circuit = pm.run(circuit)**

**job = backend.run(isa_circuit, shots = 10, memory = True)**

**result = job.result()**
**memory = result.get_memory()**
**print(result)**

Als Ergebnis erhalten wir folgende Ausgabe:
**Result({'results': [{'shots': 10, 'success': True, 'data': {'counts': {'0': 6, '1': 4}}, ...}]})**
6 Nullen und 4 Einsen werden ausgegeben aber beim erneuten Ausführen ändert sich das Ergebnis ständig und würde bei einer Zahlenreihe von 10 Stück auch zufällig das gleiche Ergebnis wieder ausgeben. 

## Statistische Analyse & Theoretische Grenzen

Wie vergleichen wir die Generatoren?

Als statistische Mittel werden Chi-Quadrat, Runs-p-Wert, Ljung-Box p, Lempel-Ziv, Max Power, Entropie, Pattern p-Wert eingesetzt, um die Generatoren miteinander zu vergleichen. 

Allerdings sind die statistischen Mittel begrenzt, da der Satz von Rice besagt, dass es keinen allgemeinen Algorithmus gibt, der für jede Folge beweist, ob sie "wirklich zufällig" ist. In der praktischen Konsequenz ziehen wir daraus, dass wir Pseudozufälle widerlegen, aber für echte Zufälle nur Plausabilitätsargumente liefern können.

## Durchführung und Probleme

### 1. Simulation 
Bei der Durchführung galt es zunächst, Qiskit einzurichten und eine Simulation durchzuführen ohne einen gültigen Account einzubinden. Der Folgende Code zeigt, das zunächst ein Schaltkreis eingerichtet werden muss in dem das Hadamard-Gate zum Einsatz kommt, der das Qubit auf Superposition bringt.

from qiskit.circuit.library import HGate
from qiskit import QuantumCircuit
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService
from PIL import Image
import math

// Simulatoren
from qiskit_ibm_runtime.fake_provider import FakeAlmadenV2
from qiskit_aer import AerSimulator

// Quantencircuit erstellen
hadamard_gate = HGate()
circuit = QuantumCircuit(1)
circuit.append(hadamard_gate, [0])
circuit.measure_all()

// Quantencircuit anzeigen
circuit.draw("mpl")

### 2. Token Einfügen
Nach der Simulation beginnen wir damit das KOnto einzurichten und lokal zu speichern. Hierzu verwenden wir den API-Token, den wir von IBM bekommen.

// Füge deinen API-Token ein:
**token = "Hier den API-Token einsetzen"**

// Speichere das Konto lokal und setze es als Standard:
**QiskitRuntimeService.save_account(**
    **channel="ibm_cloud",**           // oder "ibm_quantum_platform" bei neuer Plattform
    **token=token,**
    **instance="Projekt Zufall 1",**    // Instanzname
    **overwrite=True,**
    **set_as_default=True**
**)**

### 3. Backend festlegen
Hier legen wir unser Backend fest, also die Hardware, die wir nutzen möchten
# Backend wird festgelegt

**from qiskit_ibm_runtime import SamplerV2 as Sampler**

**service = QiskitRuntimeService()  # lädt deine gespeicherten Credentials**
**print(service.backends())**

**backend_name = service.least_busy()**
**print(backend_name)**
**sampler = Sampler(mode=backend_name)**

**pm = generate_preset_pass_manager(backend=backend_name, optimization_level = 3)**
**isa_circuit = pm.run(circuit)**
**isa_circuit.draw("mpl")**

Als Ausgabe erhalten wir hier:
**IBMBackend('ibm_brisbane'), IBMBackend('ibm_sherbrooke'), IBMBackend('ibm_torino')**
**IBMBackend('ibm_sherbrooke')** 

mit **backend_name = service.least_busy()** haben wir den am wenigsten ausgelasteten Quantencomputer gewählt

### 4. Job (Code) ausführen
Mit folgender Anweisung führen wir den Job aus, also das Qubit mittels Hadamard-Gatter in den Superositionszustand und es bei der Messung eine Null oder Eins ausgeben zu lassen und das Ganze 100.000 mal (100000 Shots) und erhalten eine Job-ID zurück

// Send the run request
**job = sampler.run([isa_circuit], shots = 100000)**
**print("Job-ID:", job.job_id())**

### 5. Statuscheck
Mit **print(job.status())** fragen wir den Status ab, ob der dieser erledigt (DONE) ist oder noch in Arbeit ist (IN PROGRESS).

### 6. Job-ID laden
Ist der Job erledigt laden wir den Job

// (irgendeinen) Job laden, nach Job ID

**aktueller_job = 'd1n1vi33rr0s73berb70'** //job.job_id()
**job_id = 'd1mf95n29o4s73aqu9c0'**
**job1 = service.job(aktueller_job)** // oder aktueller_job anstatt job_id

**job_status = job1.status()**
**print(f"Job-Status: {job_status}")**
**result = job1.result()**

Der Status des Jobs wird als "Job-Status:" "DONE" oder "IN ROGRESS" dargestellt

### 7. Ergebnisse ausgeben

**print("Ergebnisse auf echter Hardware:", result)**
**counts = result[0].data.meas.get_counts()**
**print(counts)**

Ausgabe: 

Ergebnisse auf echter Hardware: PrimitiveResult([SamplerPubResult(data=DataBin(meas=BitArray(<shape=(), num_shots=100000, num_bits=1>)), metadata={'circuit_metadata': {}})], metadata={'execution': {'execution_spans': ExecutionSpans([DoubleSliceSpan(<start='2025-07-09 07:52:42', stop='2025-07-09 07:53:09', size=100000>)])}, 'version': 2})
{'1': 50022, '0': 49978}

// Verwendbare Werte
samples = result[0].data.meas.array
print(samples)
import numpy as np
flattened_array = samples.flatten()
print(flattened_array)

[[1]
 [0]
 [1]
 ...
 [0]
 [0]
 [1]]
[1 0 1 ... 0 0 1]

### 8. Ergebnisse speichern

def csvBits(samples_int): 
    # Umwandeln in eine Liste von Listen
    memory_rows = [[bit] for bit in samples_int]
    with open("C:/Users/jojot/Documents/Quantum_Computing_Team/Quantum_Computing_Team/Projekt Zufall/Ergebnisse/ergebnisseIBMBits.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(memory_rows)



### 9. Statistische Auswertung
Der folgende Code enthält 4 Pseudozufallsgeneratoren und die zufällig erstellte Bit-Reihe vom Quantencomputer die hier mit 8 statistischen Tests überzogen werden. 
Des Weiteren werden die Tests in der Summe bewertet und eine Entscheidung getroffen, ob es sich bei jeweiligen Algorithmus um einen Pseudozufall handelt oder nicht.
Als Ausgabe erhalten wir:

Statistische Analyse:
                       Typ  Chi² p-Wert  Runs p-Wert  Ljung-Box p  Lempel-Ziv  Max Power  Entropie  Pattern p-Wert  Bitflip p-Wert Pseudozufall?
      Python Pseudozufall      0.97982      0.57783      0.69023     1.01701    4.82061   1.00000         0.39422         0.58216          Nein
Echter Zufall (simuliert)      0.24970      0.86273      0.16448     1.01535    5.01313   0.99999         0.15091         0.86441          Nein
  Kryptografischer Zufall      0.51477      0.31396      0.32744     1.01850    6.84183   1.00000         0.66327         0.31460          Nein
         Mersenne Twister      0.84456      0.72312      0.00325     1.01701    5.07737   1.00000         0.24715         0.72321            Ja
          Hardware-Zufall      0.92442      0.89436      0.85942     1.01867    5.58029   1.00000         0.67476         0.89934          Nein
                 Hadamard      0.88934      0.10544      0.57840     1.02033    6.08485   1.00000         0.04818         0.10679          Nein

Die Tests des Chi^2, der Ljung-Box, der Lempel-Komplexität, der Fourier-Analyse und der Bitflip-Verteilung sind visualisiert und liegen diesem Dokument bei unter \Quantum_Computing_Team\Projekt Zufall\zufallsanalyse_ergebnisse\bitflip_3d.png und \Quantum_Computing_Team\Projekt Zufall\zufallsanalyse_ergebnisse\uebersicht.png bei


import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.sandbox.stats.runs import runstest_1samp
from collections import Counter
import pandas as pd
from scipy.signal import periodogram
import os
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time

// 1. Datengenerierung
n = 100000

// Zufallsgenerierte Daten des Quantencomputers
ibm_random = flattened_array

// Pseudozufall (Python random)
// random.seed(42)
pseudo_data = [random.randint(0, 1) for _ in range(n)]

// Simulierter "echter" Zufall (mit besserem Generator)
true_random = np.random.Generator(np.random.SFC64()).integers(0, 2, n).tolist()

// Kryptografischer Zufall
def crypto_random(size):
    return [int(b) for byte in os.urandom(size//8+1) for b in f'{byte:08b}'][:size]

crypto_data = crypto_random(n)

// Mersenne Twister
mt_random = np.random.MT19937(int(time.time() * 1000))
mersenne_data = np.random.Generator(mt_random).integers(0, 2, n).tolist()

// Echter Hardware-Zufall
try:
    hardware_random = [int(bit) for bit in bin(int.from_bytes(os.urandom(n//8), 'big'))[2:].zfill(n)[:n]]
except Exception as e:
    print(f"Hardware-Zufall nicht verfügbar: {e}")
    hardware_random = [0]*n  # Fallback

// 2. Verbesserte statistische Analyse
// Entscheidungskriterien für Pseudozufall:
// - Chi² p < 0.01
// - Runs p < 0.01
// - Ljung-Box p < 0.01
// - Lempel-Ziv < 0.9
// - Max Power > 20
// - Entropie < 0.99
// - Bitflip p < 0.01
// - Pattern p < 0.01

def analyze_randomness(data, name):
    counts = Counter(data)
    chi2, p_chi2 = stats.chisquare([counts[0], counts[1]], f_exp=[len(data)/2, len(data)/2])
    _, p_runs = runstest_1samp(data, correction=False)
    lb_result = acorr_ljungbox(data, lags=[10, 50, 100], return_df=True)
    p_lb = lb_result["lb_pvalue"].min()
    def lempel_ziv(sequence):
        seq_str = ''.join(map(str, sequence))
        i, n, c = 0, len(seq_str), 0
        while i < n:
            j = 1
            while i + j <= n and seq_str[i:i+j] in seq_str[:i+j-1]:
                j += 1
            c += 1
            i += j
        return c / (n / np.log2(n))
    lz = lempel_ziv(data)
    freqs, power = periodogram(np.array(data) - np.mean(data))
    max_power = np.max(power)
    entropy = stats.entropy([counts[0]+1, counts[1]+1], base=2)
    def pattern_test(sequence, length=8):
        patterns = [''.join(map(str, sequence[i:i+length])) for i in range(0, len(sequence)-length+1, length)]
        freq = Counter(patterns)
        return stats.chisquare(list(freq.values())).pvalue
    p_pattern = pattern_test(data)
    diffs = np.diff(data)
    p_bitflip = stats.binomtest(sum(diffs != 0), n=len(diffs), p=0.5).pvalue
    // Entscheidung anhand der 8 Werte
    is_pseudo = (
        (p_chi2 < 0.01) or
        (p_runs < 0.01) or
        (p_lb < 0.01) or
        (lz < 0.9) or
        (max_power > 20) or
        (entropy < 0.99) or
        (p_bitflip < 0.01) or
        (p_pattern < 0.01)
    )
    return {
        "Typ": name,
        "Chi² p-Wert": p_chi2,
        "Runs p-Wert": p_runs,
        "Ljung-Box p": p_lb,
        "Lempel-Ziv": lz,
        "Max Power": max_power,
        "Entropie": entropy,
        "Pattern p-Wert": p_pattern,
        "Bitflip p-Wert": p_bitflip,
        "Pseudozufall?": "Ja" if is_pseudo else "Nein"
    }

data_sets = {
    "Python Pseudozufall": pseudo_data,
    "Echter Zufall (simuliert)": true_random,
    "Kryptografischer Zufall": crypto_data,
    "Mersenne Twister": mersenne_data,
    "Hardware-Zufall": hardware_random,
    "Hadamard": ibm_random
}

results = [analyze_randomness(data, name) for name, data in data_sets.items()]

// 3. Ergebnisse speichern und anzeigen
results_df = pd.DataFrame(results)
output_dir = Path("zufallsanalyse_ergebnisse")
output_dir.mkdir(exist_ok=True)

results_df.to_csv(output_dir / "statistische_analyse.csv", index=False, float_format="%.5f")
print("Statistische Analyse:\n", results_df.to_string(index=False, float_format="%.5f"))

// 4. Visualisierungen
plt.figure(figsize=(18, 15))
generator_names = [result["Typ"] for result in results]

// Plot 1: Chi²-Test p-Werte
plt.subplot(2, 3, 1)
plt.bar(range(len(results)), [result["Chi² p-Wert"] for result in results])
plt.xticks(range(len(results)), generator_names, rotation=45)
plt.title("Chi²-Test p-Werte")
plt.axhline(0.05, color='r', linestyle='--')

// Plot 2: Autokorrelation
plt.subplot(2, 3, 2)
for name, data in data_sets.items():
    plt.plot(acorr_ljungbox(data, lags=50, return_df=True)['lb_pvalue'], label=name)
plt.axhline(0.05, color='r', linestyle='--')
plt.title("Autokorrelation (Ljung-Box)")
plt.legend()

// Plot 3: Lempel-Ziv-Komplexität
plt.subplot(2, 3, 3)
plt.bar(range(len(results)), [result["Lempel-Ziv"] for result in results])
plt.xticks(range(len(results)), generator_names, rotation=45)
plt.title("Lempel-Ziv-Komplexität")
plt.axhline(0.9, color='r', linestyle='--')

// Plot 4: Fourier-Analyse
plt.subplot(2, 3, 4)
for name, data in data_sets.items():
    freqs, power = periodogram(np.array(data) - np.mean(data))
    plt.semilogy(freqs[:100], power[:100], label=name)
plt.title("Fourier-Analyse (Periodizität)")
plt.legend()

// Übersichtsgrafik als PNG speichern
plt.tight_layout()
plt.savefig(output_dir / "uebersicht.png", dpi=200)
plt.show()

// Plot 6: Bitflip-Verteilung als 3D-Plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
colors = cm.viridis(np.linspace(0, 1, len(data_sets)))
for idx, (name, data) in enumerate(data_sets.items()):
    diffs = np.diff(data)
    vals, counts = np.unique(diffs, return_counts=True)
    xs = np.full_like(vals, idx)
    ax.bar(xs, counts, zs=vals, zdir='y', alpha=0.7, color=colors[idx], label=name)
ax.set_xlabel('Generator')
ax.set_ylabel('Bitflip-Wert')
ax.set_zlabel('Häufigkeit')
ax.set_xticks(range(len(data_sets)))
ax.set_xticklabels(list(data_sets.keys()), rotation=45, ha='right')
ax.set_yticks([-1, 0, 1])
ax.set_title('Bitflip-Verteilung (3D)')
ax.legend()
plt.tight_layout()
fig.savefig(output_dir / "bitflip_3d.png", dpi=200)
plt.show()

// 5. Rohdaten werden nicht mehr als einzelne CSVs gespeichert
print(f"\nAlle Ergebnisse wurden in '{output_dir}' gespeichert:")
print(f" - statistische_analyse.csv")
print(f" - uebersicht.png")
print(f" - bitflip_3d.png")

## Ergebnis und Auswertung
Vergleich von 6 Zufallsgeneratoren anhand von 100.000 Bits:

Die folgende Tabelle fasst die Ergebnisse der Tests zusammen. Ein p-Wert > 0.05 deutet auf Zufälligkeit hin, während Lempel-Ziv-Werte nahe 1.0 und hohe Entropie (~1.0) für geringe Muster sprechen:
Typ	                        Chi² p-Wert	Runs p-Wert	Ljung-Box p	Lempel-Ziv	Max Power	Entropie	Pattern p-Wert	Bitflip p-Wert	Pseudozufall?
Python Pseudozufall	        0.97982	    0.57783	    0.69023	    1.01701	    4.82061	    1.00000	    0.39422	        0.58216         Nein
Echter Zufall (simuliert)	0.24970	    0.86273	    0.16448	    1.01535	    5.01313	    0.99999	    0.15091	        0.86441         Nein
Kryptografischer Zufall	    0.51477	    0.31396	    0.32744	    1.01850	    6.84183	    1.00000	    0.66327	        0.31460	        Nein
Mersenne Twister	        0.84456	    0.72312	    0.00325	    1.01701	    5.07737	    1.00000	    0.24715	        0.72321	        Ja
Hardware-Zufall	            0.92442	    0.89436	    0.85942	    1.01867	    5.58029	    1.00000	    0.67476	        0.89934	        Nein
Hadamard (QRNG)	            0.88934	    0.10544	    0.57840	    1.02033	    6.08485	    1.00000	    0.04818	        0.10679	        Nein

### Interpretation der statistischen Tests mit Fokus auf echtem Zufall, hier: Hadamard
 Chi²-Test (Goodness-of-Fit)

#### Chi-QUadrat-Test 

Der Test bestätigt, dass die Verteilung der Nullen und Einsen nahezu perfekt 50/50 ist bei einem Wert von p = 0.88934. Dass die Hadamardreihe hier nicht auf den Wert 1 gekommen ist, zeigt die naürliche Fluktuation. Der Wert würde sich weiter gen 1 vergrößern, wenn wir eine größere Probe hätten. Bei 100.000 Bits sind eine Abweichung von rund 0.12% erwartbar. Demnach wäre ein Wert von 1 zu perfekt. 
Anders als der Python Pseudozufall (p = 0.97982). Dieser Algortihmus ist darauf getrimmt eine sehr hohe Gleichverteilung zu haben.

#### Runs-Test (Wald-Wolfowitz)

Der Runs-Test prüft, ob die Abfolge keine Muster aufweist wie zum Beispiel "000111", "0101010101010101" oder "110011001100110011"
Ergebnis für Hadamard mit p = 0.10544 zeigt auffällig ein leicht über 0.05 liegenden Wert, der auf echten Zufall hindeutet, da der Zufall auch längere Runs (x-fache Abfolge eines Wertes) von 15 oder mehr zulässt. Dagegen bewegen sich die Pseudozufallsgeneratoren auf deutlisch höheren Werten, da diese es tunlichst Musterbildungen vermeiden. Somit sind seltene aber natürliche "Klumpen" in der Datenreihe erwartbar.

#### Ljung-Box-Test (Autokorrelation)

Der Ljung-Box-Test sucht nach linearen Abhängigkeiten. Das wäre zum Beispiel eine 1 nach jeder 10. Stelle oder eine o nach jeder 5. Stelle.
Ein Ergebnis von p = 0.57840 beim Hadamard ist gut, da dieser über 0,05 liegt. Anders sieht es beim Mersenne Twister aus, der deutlich unter 0.05 bei 0,00325 liegt. Hier finden sich deutliche Anzeichen für lineare Abhängigkeiten und weist somit auf eine Pseudozufälligkeit hin. Das Ergebnis bestätigt, dass Quantenbits keine linearen Abhängigkeiten aufweisen.

#### Pattern-Test (NIST STS)

Der Pattern-Test ducht gezielt nach nichtlinearen Mustern also nach Mustern, die nicht in gleichen Abständen auftreten wie zum Beispiel die "1010".
Das Ergebnis bei für Hadamard mit p = 0,04818 liegt leicht unter 0,05 und zeigt ganz klar nichtlineare Muster, die aber bei echten Zufällen auch erwartet werden in 5% der Tests. Hinzu kommt, dass Quantenrauschen die Werte ebenfalls unter die 0,05 drücken zum Beispiel durch Relaxation der Qubits. Vergleicht man den Wert mit dem von Kryptografischer Zufall (p = 0.66327), erkennt man, dass dieser PRNG gegen Muster gewappnet ist und zeigt, dass die Unvollkommenheit eines echten Zufalls ein Nachweis ist. 

#### Lempel-Ziv-Komplexität

Die Lempel-ZIV-Komplexität misst wie schwer die Abfolge zu komprimieren ist. Der Hadamard mit dem Wert 1.02033 schneidet hier sehr gut ab unter Rücksichtnahme von Quantenrauschen. Denn das Quantenrauschen erzeugt minimal Abweichungen von der perfekten Zufälligkeit.
    Quantenrauschen: Ist ein nicht exakt berechenbares Verhalten von Quantenteilchen, welches Ergebnisse beeinflusst und physikalisch unvermeidbar ist.

#### Zusammenfassung: Echter Zufall          vs.             PRNGs
Test	         Hadamard (QRNG)	                    Mersenne Twister (PRNG)
Chi²	         Natürliche Fluktuation (p ~0.89)	    Künstlich perfekt (p ~0.84)
Runs	         Leicht längere Runs (p ~0.10)	        Zu gleichmäßig (p ~0.72)
Ljung-Box	     Keine Autokorrelation (p ~0.58)	    Deterministische Muster (p ~0.003)
Pattern	         Minimale Quantenabweichung (p ~0.048)	Algorithmisch geglättet (p ~0.247)
Lempel-Ziv	     Höchste Komplexität (1.020)	        Geringfügig komprimierbar (1.017)

#### 1. Frage: "Warum schneidet der Hadamard-Generator in einigen Tests schlechter ab als PRNGs (p ~0.048)?"

PRNGs sind Algorithmen, die darauf getrimmt wurden solche Tests wie wir sie benutzt haben zu bestehen. Das können sie auch sehr gut, denn sie sind deterministisch sind somit anpassbar. Betrachten wir dagegen die Datenreihe von Hdamard so sehen wir Statistische Ausreißer, die gerade nicht der Logik der Tests folgen. Somit ist die Schwäche bei Pattern-Test ein Merkmal für echten Zufall.

#### Echter Zufall vs. Pseudozufall (technisch und mathematisch)
Die Auswertungen zeigen, dass lediglich Ausprägungen der erzeugten Datenreihen nachweisbar sind. Einen absoluten Beweis können die statistischen Mittel nicht erbringen. Somit ist bewiesen, dass wir nicht absoulut beweisen konnten, ob es sich um Pseudozufälle oder echte Zufälle handelt. Allerdings konnten wir aufzeigen, dass diese beiden Arten statistisch nahe beieinander lagen. Anhand eines einzelnen Testergebnisses war nicht von einem echten oder unechten Zufall zu sprechen. Erst bei Betrachtung mehrerer Ergebnisse sind Tendenzen zu erkennen, allerdings blieb es dabei auch. Somit bleibt uns lediglich Pseudozufallsalgorithmen und Quantenzufallsalgorithmen mathematisch und technisch voneinander zu trennen.

Ein Quantencomputer kann echten Zufall erzeugen, weil er auf den Prinzipien der Quantenmechanik basiert, insbesondere auf dem Konzept der Superposition und der Quantenmechanischen Messung. Ein Quantencomputer kann, im Gegensatz zu einem klassischen Computer, ein Qubit (Quantenbit) in einen Zustand versetzen, der nicht eindeutig null oder eins ist, sondern beides gleichzeitig. Dieser Zustand nennt sich Superposition. Erst wenn man misst, „entscheidet“ sich das Qubit – und dieser Kollaps der Superposition erfolgt nicht aufgrund eines verborgenen Mechanismus, sondern ist laut allen experimentellen Ergebnissen wirklich zufällig. Es gibt keinerlei versteckte Parameter, die das Ergebnis im Voraus bestimmen, wie es die Bell’schen Ungleichungen zeigen würden.

Das bedeutet: Wenn ein Quantencomputer ein Qubit vorbereitet (mithilfe von Quantengatter, hier: Hadamard-Gatter), etwa im Zustand $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$  und dieses misst, ist das Ergebnis jedes Mal entweder null oder eins. Dies geschieht mit exakt 50 Prozent Wahrscheinlichkeit ($\left|\frac{1}{\sqrt{2}}\right|^2 = 0,5$), und ohne dass irgendjemand oder irgendetwas vorhersehen kann, was es wird. Dieser Zufall ist fundamental, nicht simuliert. Das unterscheidet ihn grundlegend von jedem klassischen System. Er erzeugt echten Zufall, weil er aus Prinzip her unvorhersagbar ist.


Im Gegensatz zu den Quantencomputern werden in klassischen Systemen deterministische Algorithmen verwendet, um Zufall zu simulieren. Einer der besten und weitverbreitesteten dieser Algorithmen ist der Mersenne-Twister. Dieser wurde 1997 von Makoto Matsumoto und Takuji Nishimura entwickelt und erhält seinen Namen durch seine extrem lange Periode (Anzahl der Zeichen, nach der sich die Zufallszahlen wiederholen), nämlich die Mersenne-Primzahl $2^{19937}-1 \approx 4,3 \cdot 10^{6001}$. Dies gilt für den MT 19937, die neuere Version des Mersenne-Twister.

Kurzgesagt, der Algorithmus erstellt bei jedem $1., 625., 1249., ..., (1 +n \cdot 624).$ Aufruf 624 Zustandswörter, die gespeichert werden. Bei jedem Aufruf wird das nächste Zustandswort in der Liste ausgewählt, vielfach verändert und ausgegeben. Bei schlechten Startwerten (z.B.: $[1, 1, 1, ..., 1, 1]$, 624 mal) benötigt der Algorithmus eine Aufwärmphase von idealerweise 800.000 Aufrufen, also 800.000 Zufallszahlen, um eine gleichverteilte Bitsequenz (guter Zufall) zu garantieren. Der Mersenne-Twister ist deterministisch, d.h. bei gleichem 624 Zustandswort Input auch immer der gleiche Output herauskommt. Anzumerken ist noch, dass der Mersenne-Twister nicht kryptographisch sicher ist.

#### 2. Frage: "Warum beweist die Statistik nichts?"
Die statistische Untersuchung der Bitreihen in Bezug auf ihre Zufälligkeit lässt keine Schlüsse auf die Herkunft ebendieser zu. 
D.h., nur anhand der Ergebnisse ist es unmöglich zu sagen, ob eine Bitreihe einem deterministischen oder tatsächlich echtem Zufallsgenerator entspringt.
Ausschlaggebend für diese Erkenntnis ist, dass echte und Pseudozufallsalgorithmen dieselbe zufällige Bitreihe erzeugen können, zwar ist dies extrem unwahrscheinlich, aber trotzdem möglich.
Daraus und der Tatsache, dass die Algorithmen der statistischen Untersuchung deterministisch, also gleicher Input führt zu gleichem Output, sind, folgt nun die Erkenntnis, dass die Auswertung der Zufälligkeit einer 
jeglicher Informationskette lediglich Aussagen über die Zufälligkeit ermöglicht und nicht über die Herkunft Dieser.

#### Technische Unterschiede der Herkunft der Zufälligkeit:
Pseudozufall vs. echter Zufall
Pseudozufall entsteht mithilfe deterministischer Algorithmen. Wie oben erklärt, ein deterministischer Algorithmus gibt dem gleichen Input, den man bei Zufallsalgorithmen "Seed" (lit. Saat, Startwert) nennt, den gleichen Output.
Bei einem Zufallsgenerator möchte man aber unterschiedliche Outputs haben. Deswegen werden diese PRNG (Pseudo Random Number Generator) häufig bei Simulationsexperimenten verwendet, da sie wiederholbar sind.
Da liegt auch der entscheidende Unterschied zwischen PRNGs und TRNGs (True Random Number Generator). TRNGs sind nicht wiederholbar, denn ihre Seeds basieren auf nichtdeterministischen Quellen. Zu den bekanntesten zählen die Quantenphysik, radioaktiver Zerfall und thermisches Rauschen. Weil aber der normale PC keinen Zugriff auf diese Werte hat, greift er auf Quasi-Zufälle zurück, z.B. die Zeit, die zwischen zwei Mausklicks verstreicht. 
Quantencomputing gehört nicht zu der klassischen Informatik, im Gegensatz zu den beiden eben genannten Algorithmen. Es basiert auf der Quantenmechanik und kann deswegen echten Zufall erzeugen.

quelle alles: http://www.fim.uni-linz.ac.at/lva/Web_Security/Abgaben/Schuerz-RNG.pdf

Von KI überarbeitet:
Warum beweist Statistik nichts über die Herkunft von Zufallsdaten?

Die statistische Analyse von Bitreihen hinsichtlich ihrer Zufälligkeit erlaubt keinerlei Rückschluss auf deren Ursprung. Das bedeutet: Allein anhand statistischer Testergebnisse lässt sich nicht entscheiden, ob eine Bitfolge aus einem deterministischen Pseudozufallsalgorithmus stammt oder durch einen echten, physikalischen Zufallsprozess erzeugt wurde. Ausschlaggebend für diese Erkenntnis ist ein fundamentaler Umstand: Echte und pseudozufällige Generatoren können rein theoretisch exakt dieselbe Bitreihe erzeugen. Diese Übereinstimmung ist zwar extrem unwahrscheinlich, aber nicht unmöglich. Daraus folgt: Statistische Zufälligkeit impliziert keine ontologische Aussage über die Quelle. Verschärft wird dieses Dilemma durch die Tatsache, dass auch die statistischen Tests selbst deterministisch arbeiten – das heißt, sie liefern bei gleichem Input stets denselben Output. Daraus ergibt sich eine Art erkenntnistheoretische Schranke: Die Tests prüfen lediglich ob eine Bitfolge „zufällig aussieht“, aber sie verraten nicht woher diese kommt. Sie urteilen über das Erscheinungsbild, nicht über das Wesen.
Fazit:
Statistische Analysen können nur Aussagen über das Maß der Zufälligkeit einer Datenreihe treffen, aber niemals über deren technische oder physikalische Herkunft.

Pseudozufall vs. echter Zufall: Ein technischer Blick
Pseudozufall entsteht durch deterministische Algorithmen. Gibt man einem solchen Algorithmus denselben Startwert, den sogenannten Seed, so produziert er immer dieselbe Ausgabe. Dieser deterministische Charakter ist gewollt: In Simulationen, Tests und Debugging-Szenarien ist Reproduzierbarkeit ein Segen.
Echte Zufallsgeneratoren (TRNGs – True Random Number Generators) hingegen operieren auf Basis nichtdeterministischer Quellen wie quantenmechanischen Effekten, radioaktivem Zerfall oder thermischem Rauschen. Diese Prozesse sind, nach heutigem Stand der Physik, fundamental unvorhersagbar. Da normale Computer jedoch keinen direkten Zugang zu solchen Quellen haben, greifen sie auf sogenannte Quasi-Zufälle zurück, z.B. die Zeitabstände zwischen Tastatureingaben oder Mausbewegungen. Auch wenn das auf den ersten Blick „echt“ wirkt, handelt es sich hierbei oft um eine Notlösung mit eingeschränkter Entropiequelle. Quantencomputer wiederum spielen in einer eigenen Liga. Sie basieren auf den Prinzipien der Quantenmechanik und können daher echten Zufall erzeugen, nicht als Nebeneffekt, sondern als inhärente Eigenschaft ihres Rechenmodells. Dies unterscheidet sie fundamental von klassischen Pseudozufalls- und sogar von manchen TRNG-Verfahren.

### Fazit Ausblick

Unser Projekt „Zufall“ hatte zum Ziel, klassische Pseudozufallsgeneratoren (PRNGs) mit einem Quantenzufallsgenerator (QRNG) zu vergleichen und zu untersuchen, inwiefern sich echte Zufälligkeit von simuliertem Zufall unterscheidet. Durch die statistische Analyse von Bitfolgen konnten wir zeigen, dass Quantenzufall zwar nicht „perfekter“ ist als Pseudozufall, aber bestimmte Eigenschaften aufweist, die auf eine nicht-deterministische Struktur hindeuten.

Die Ergebnisse bestätigen, dass PRNGs wie der Mersenne Twister zwar sehr gute statistische Eigenschaften aufweisen, jedoch durch ihre deterministische Struktur vorhersehbar bleiben. Der Quantenzufallsgenerator hingegen lieferte Werte, die zwar leicht von der idealen Verteilung abweichen (z. B. im Pattern-Test), aber gerade diese Abweichungen sind ein Indiz für echten Zufall, denn perfekte Gleichverteilung ist in der Natur selten.

Ein zentrales Ergebnis ist auch die Erkenntnis, dass statistische Tests allein keine absolute Aussage über die Herkunft von Zufallsdaten liefern können. Sie können Pseudozufall entlarven, aber echten Zufall nur plausibel machen.

Das Projekt hat gezeigt, dass Quantencomputing eine Möglichkeit zur Erzeugung von Zufallszahlen bietet, insbesondere in Bereichen wie Kryptografie und maschinellem Lernen, wo echte Unvorhersehbarkeit entscheidend ist.

Zukünftige Arbeiten könnten folgende Aspekte vertiefen:
Größere Datenmengen: Eine Analyse mit noch mehr Bits (1.000.000 Stück oder mehr), um statistische Schwankungen zu vergleichen 
Vergleich mit anderen QRNGs: Nutzung verschiedener Quantenalgorithmen oder Hardware-basierter Zufallsgeneratoren z.B. optische Quantenexperimente.
Echtzeit-Anwendungen: Integration des Quantenzufalls in eine kleine Verschlüsselungsanwendung, um den praktischen Nutzen zu demonstrieren.
Fehlerkorrektur und Rauschunterdrückung: Untersuchung, wie sich Quantenrauschen auf die Zufälligkeit auswirkt und ob Algorithmen das ausfiltern können.

Ein letzter Gedanke: "Vielleicht ist Zufall lediglich Chaos, welches wir noch nicht verstehen"

#### Projektende
07.07.2025 bis 10.07.2025

Quantum Computing Team

**Juan & Jonas**

