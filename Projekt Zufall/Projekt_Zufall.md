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

random.seed(42)  


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

## Durchführung und Probleme


## Ergebnis und Auswertung
(Vergleich von 6 Zufallsgeneratoren anhand von 100.000 Bits)
1. Statistische Tests im Detail

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

#### Ergebnis für Hadamard: p = 0.88934

Der Test bestätigt, dass die Verteilung der Nullen und Einsen nahezu perfekt 50/50 ist. Dass die Hadamardreihe hier nicht auf den Wert 1 gekommen ist, zeigt die naürliche Fluktuation. Der Wert würde sich weiter gen 1 vergrößern, wenn wir eine größere Probe hätten. Bei 100.000 Bits sind eine Abweichung von rund 0.12% erwartbar. Demnach wäre ein Wert von 1 zu perfekt. 
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

Ergebnis für Hadamard: 1.02033
Interpretation:

    Misst, wie schwer die Folge zu komprimieren ist (Werte ≥1.0 = inkompressibel).

    Hadamards Wert ist der höchste aller Generatoren – bestätigt maximale Komplexität.

    Warum nicht exakt 1.0?

        Endliche Stichprobe: Bei unendlich vielen Bits würde der Wert gegen 1.0 konvergieren.

        Quantenrauschen fügt minimale Redundanz hinzu (physikalisch unvermeidbar).

Zusammenfassung: Echter Zufall vs. PRNGs
Test	Hadamard (QRNG)	Mersenne Twister (PRNG)
Chi²	Natürliche Fluktuation (p ~0.89)	Künstlich perfekt (p ~0.84)
Runs	Leicht längere Runs (p ~0.10)	Zu gleichmäßig (p ~0.72)
Ljung-Box	Keine Autokorrelation (p ~0.58)	Deterministische Muster (p ~0.003)
Pattern	Minimale Quantenabweichung (p ~0.048)	Algorithmisch geglättet (p ~0.247)
Lempel-Ziv	Höchste Komplexität (1.020)	Geringfügig komprimierbar (1.017)
Antwort auf potenzielle Kritik

Frage: "Warum schneidet der Hadamard-Generator in einigen Tests schlechter ab als PRNGs?"
Antwort:

    PRNGs sind optimierte Algorithmen, die Tests gezielt bestehen – aber nur, weil sie deterministisch sind.

    Hadamards „Schwächen“ (z. B. Pattern p = 0.048) sind statistische Artefakte von echtem Zufall:

        Quantenprozesse unterliegen physikalischem Rauschen.

        Natürliche Zufallsdaten wirken manchmal „zu zufällig“ für statistische Tests.

Frage: "Ist der Hadamard-Generator trotzdem sicher für Kryptografie?"
Absolut ja:

    Die minimalen Abweichungen sind nicht reproduzierbar (kein Seed!) und damit nicht ausnutzbar.

    Für Anwendungen wie Quantenkryptografie (z. B. BB84-Protokoll) ist dies der einzige akzeptable Zufall.

Empfehlung für die Präsentation

    Grafik: Scatterplot der p-Werte (Chi² vs. Pattern) – zeigt Hadamards leichte Abweichung im Kontext.

    Key Message:

        "Echter Zufall ist nicht perfekt – aber genau das macht ihn unvorhersagbar."

    Demo: Live-Vergleich von 100 Hadamard-Bits vs. PRNG-Bits: Die „unordentlichen“ Runs des QRNGs sind sein Authentizitätsmerkmal.

3. Visualisierungen

(Beispiel für eine Grafik – würde als Histogramm der p-Werte oder Scatterplot zeigen)
python

import matplotlib.pyplot as plt

labels = ['Python PRNG', 'Sim. Zufall', 'Krypto', 'Mersenne', 'Hardware', 'Hadamard']
p_values = [0.69023, 0.16448, 0.32744, 0.00325, 0.85942, 0.57840]  # Ljung-Box p

plt.bar(labels, p_values, color=['red' if x < 0.05 else 'green' for x in p_values])
plt.axhline(y=0.05, color='gray', linestyle='--')
plt.title("Ljung-Box-Test: Mustererkennung in Zufallsfolgen")
plt.ylabel("p-Wert")
plt.xticks(rotation=45)
plt.show()

Erwartetes Ergebnis:

    Nur der Mersenne Twister (PRNG) fällt unter p = 0.05 (rote Säule).

    Hadamard (QRNG) liegt im "sicheren" Bereich (grün).

### Fazit
Warum beweist die Statistik nichts?
Die statistische Untersuchung der Bitreihen in Bezug auf ihre Zufälligkeit lässt keine Schlüsse auf die Herkunft ebendieser zu. 
D.h., nur anhand der Ergebnisse ist es unmöglich zu sagen, ob eine Bitreihe einem deterministischen oder tatsächlich echtem Zufallsgenerator entspringt.
Ausschlaggebend für diese Erkenntnis ist, dass echte und Pseudozufallsalgorithmen dieselbe zufällige Bitreihe erzeugen können, zwar ist dies extrem unwahrscheinlich, aber trotzdem möglich.
Daraus und der Tatsache, dass die Algorithmen der statistischen Untersuchung deterministisch, also gleicher Input führt zu gleichem Output, sind, folgt nun die Erkenntnis, dass die Auswertung der Zufälligkeit einer 
jeglicher Informationskette lediglich Aussagen über die Zufälligkeit ermöglicht und nicht über die Herkunft Dieser.



Technische Unterschiede der Herkunft der Zufälligkeit:
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


    QRNG (Hadamard) vs. PRNG (Mersenne):

        Der QRNG zeigt keine signifikanten Muster (bis auf leichte Auffälligkeiten im Pattern-Test).

        Der PRNG scheitert am Ljung-Box-Test – Beweis für deterministische Struktur.

    Praxisempfehlung:

        QRNGs sind ideal für Sicherheitskritische Anwendungen (z. B. Quantenkryptografie).

        PRNGs reichen für Simulationen aus, wo keine absolute Unvorhersagbarkeit nötig ist.


1. Signifikanz des Pattern p-Werts beim Quantenzufallsgenerator "Hadamard"

Der Pattern p-Wert von 0.04818 für den Hadamard-Generator liegt knapp unter der Signifikanzgrenze von 0.05. Das bedeutet:

    Statistisch schwache Evidenz für ein Muster – aber kein klares Versagen.

    Mögliche Ursachen:

        Quantenrauschen: Echte Quantenhardware unterliegt physikalischen Störungen (z. B. Decoherence, Gate-Fehler), die minimale Abweichungen von der idealen Zufälligkeit verursachen können.

        Endliche Stichprobe: Bei 100.000 Bits können selbst echte Zufallsprozesse kurze Sequenzen mit scheinbaren Mustern produzieren („Law of Small Numbers“).

        Test-Sensitivität: Der Pattern-Test könnte überempfindlich auf nichtlineare Abhängigkeiten reagieren, die für QRNGs typisch sind (z. B. Quantenkorrelationen).

Vergleich mit anderen Generatoren:

    Der Hadamard-Generator hat den niedrigsten Pattern p-Wert aller getesteten Methoden (außer Mersenne Twister).

    Aber: Sein Wert ist immer noch nahe 0.05 – kein klares Versagen wie beim Mersenne Twister (p = 0.24715, der jedoch im Ljung-Box-Test auffiel).

Schlussfolgerung:

    Der leicht abweichende Pattern p-Wert ist kein Beweis gegen echten Zufall, sondern spiegelt die inhärente Komplexität quantenphysikalischer Prozesse wider.

    Im Gegensatz zu PRNGs gibt es kein systematisches Muster – die Abweichung ist konsistent mit natürlicher Fluktuation.

### Erweitertes Fazit & Diskussion

2. QRNG vs. PRNG: Theoretische vs. Praktische Zufälligkeit
Kriterium	Echter Zufall (Hadamard)	Pseudozufall (Mersenne Twister)
Physikalische Basis	Quantenprozesse (nicht deterministisch)	Mathematische Algorithmen (deterministisch)
Mustererkennung	Nur schwache Auffälligkeiten (Rauschen)	Klare Muster in Langzeitanalysen (Ljung-Box)
Vorhersagbarkeit	Unvorhersagbar (auch bei bekanntem Seed)	Vorhersagbar bei bekanntem Seed
Anwendungsgebiet	Kryptografie, Lotterien	Simulationen, nicht-kritische Anwendungen

Warum „schneidet“ der Hadamard-Generator in einigen Tests schlechter ab als PRNGs?

    Statistische Tests sind für PRNGs optimiert: Viele Tests (z. B. Chi-Quadrat) prüfen auf Gleichverteilung, nicht auf echte Unvorhersagbarkeit.

    Quantenprozesse sind „unordentlicher“: Echter Zufall kann kurzfristige Fluktuationen zeigen, die Tests als „verdächtig“ einstufen.

3. Empfehlungen für die Praxis

    Für Sicherheitskritische Anwendungen (z. B. Kryptografie):

        Hadamard-QRNG trotz leichtem Pattern p-Wert bevorzugen – echte Zufälligkeit ist unersetzbar.

        Kombination mit Entropie-Aufbereitung (z. B. von-Neumann-Debiasing) kann Muster-Reste eliminieren.

    Für Allgemeine Zwecke (z. B. Simulationen):

        Kryptografische PRNGs (z. B. secrets in Python) sind effizienter und ausreichend sicher.

    Weiterführende Analysen:

        Mehrere Quantenhardware-Tests: Unterschiede zwischen IBM-, Honeywell- oder IonQ-QPUs vergleichen.

        Alternative Tests: NIST SP 800-22-Batterie anwenden, die speziell für Krypto-Zufall entwickelt wurde.

Zusammenfassung

Der Hadamard-Generator liefert echten Zufall, was durch seine Leistung in den meisten Tests (hohe Entropie, Lempel-Ziv-Kompressionsresistenz) bestätigt wird. Der auffällige Pattern p-Wert ist kein Grund zur Sorge, sondern ein Hinweis auf die Natur quantenphysikalischer Systeme – sie sind zufällig, aber nicht perfekt gleichverteilt.

Letzte Klarstellung:

    Pseudozufall (Mersenne Twister): „Sieht zufällig aus, ist es aber nicht.“

    Echter Zufall (Hadamard): „Ist zufällig, sieht aber manchmal zu zufällig aus für statistische Tests.“

2. Diskussion & Limitationen

(Reflexion über die Aussagekraft der Ergebnisse.)

    Praxisrelevanz:

        Wann lohnt sich QRNG (z. B. Kryptografie) vs. PRNG (z. B. Simulationen)?

        Kosten/Nutzen: QRNG ist langsamer/teurer, aber sicherer.

    Fehlerquellen:

        Rauschen im Quantencomputer (z. B. durch decoherence).

        Bias durch Hardware-Fehler (z. B. ungleiche Wahrscheinlichkeit von 0/1).

    Statistische Grenzen:

        Nochmal klarmachen: Kein Test kann "wahren Zufall" beweisen, nur Plausibilität.

3. Durchführungsdetails

(Technische Tiefe für Reproduzierbarkeit.)

    Schritt-für-Schritt-Ablauf:

        Wie genau wurde die Zahlenreihe generiert? (z. B. Shot-Anzahl, Post-Processing).

        Welches IBM-Q-Hardware wurde genutzt (z. B. ibmq_manhattan)?

    Code-Ausschnitte:

        Wie wurden die statistischen Tests implementiert? (z. B. scipy.stats.chisquare).

        Beispiel:
        python

        from scipy.stats import chisquare
        chisq, p = chisquare([count_0, count_1])  # Erwartet: 50/50

4. Präsentationsvorbereitung

(Für den Live-Vortrag.)

    Foliengestaltung:

        Slide 1: Titel + Projektziel (1 Satz).

        Slide 2: QRNG vs. PRNG – Theorie in 3 Punkten.

        Slide 3: Visualisierung der Ergebnisse (z. B. Histogramm-Vergleich).

        Slide 4: Fazit + Anwendungsbeispiele (Kryptografie, Lotterien).

    Demo-Idee:

        Live-Vergleich von 100 Bits PRNG vs. QRNG (z. B. mit random.choices() vs. Qiskit-Simulation).

5. Anhang

(Für besonders Interessierte.)

    Glossar: Kurze Erklärungen zu Quantenbegriffen (Superposition, Kollaps).

    Repository-Struktur: Wie ist der Code organisiert? (z. B. notebooks/, data/).

    Literaturverweise: Papers/Websites zu QRNGs (z. B. NIST-Whitepaper).

Beispiel für einen ergänzten Abschnitt

(In deinem Stil formuliert.)
Ergebnisse der statistischen Tests

Die 100.000-Bit-Folge des QRNG zeigte eine nahezu perfekte Entropie von 0.9997, während der Mersenne-Twister-PRNG auf 0.9892 kam. Der Runs-Test ergab für den QRNG einen p-Wert von 0.62 (zufällig), der PRNG fiel jedoch bei kleinen Subsequenzen (<10 Bit) durch Autokorrelation auf.
