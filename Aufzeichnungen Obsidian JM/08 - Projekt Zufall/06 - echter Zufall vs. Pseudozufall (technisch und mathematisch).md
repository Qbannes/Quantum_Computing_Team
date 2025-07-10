
Beweis, warum echter Uufall vs. Pseudo (mathematisch)
echter Zufall vs. Pseudozufall (technisch und mathematisch)
Ein Quantencomputer kann echten Zufall erzeugen, weil er auf den Prinzipien der Quantenmechanik basiert, insbesondere auf dem Konzept der Superposition und der Quantenmechanischen Messung.

Ein Quantencomputer kann, im Gegensatz zu einem klassischen Computer, ein Qubit (Quantenbit) in einen Zustand versetzen, der nicht eindeutig null oder eins ist, sondern beides gleichzeitig. Dieser Zustand nennt sich Superposition. Erst wenn man misst, „entscheidet“ sich das Qubit – und dieser Kollaps der Superposition erfolgt nicht aufgrund eines verborgenen Mechanismus, sondern ist laut allen experimentellen Ergebnissen wirklich zufällig. Es gibt keinerlei versteckte Parameter, die das Ergebnis im Voraus bestimmen, wie es die Bell’schen Ungleichungen gezeigt haben.

Das bedeutet: Wenn ein Quantencomputer ein Qubit vorbereitet (mithilfe von Quantengatter, hier: Hadamard-Gatter), etwa im Zustand $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$  und dieses misst, ist das Ergebnis jedes Mal entweder null oder eins. Dies geschieht mit exakt 50 Prozent Wahrscheinlichkeit ($\left|\frac{1}{\sqrt{2}}\right|^2 = 0,5$), und ohne dass irgendjemand oder irgendetwas vorhersehen kann, was es wird. Dieser Zufall ist fundamental, nicht simuliert. Das unterscheidet ihn grundlegend von jedem klassischen System. Er erzeugt echten Zufall, weil er aus Prinzip her unvorhersagbar ist.


Im Gegensatz zu den Quantencomputern werden in klassischen Systemen deterministische Algorithmen verwendet, um Zufall zu simulieren. Einer der besten und weitverbreitesteten dieser Algorithmen ist der Mersenne-Twister. Dieser wurde 1997 von Makoto Matsumoto und Takuji Nishimura entwickelt und erhält seinen Namen durch seine extrem lange Periode (Anzahl der Zeichen, nach der sich die Zufallszahlen wiederholen), nämlich die Mersenne-Primzahl $2^{19937}-1 \approx 4,3 \cdot 10^{6001}$. Dies gilt für den MT 19937, die neuere Version des Mersenne-Twister. 

Kurzgesagt, der Algorithmus erstellt bei jedem $1., 625., 1249., ..., (1 +n \cdot 624).$ Aufruf 624 Zustandswörter, die gespeichert werden. Bei jedem Aufruf wird das nächste Zustandswort in der Liste ausgewählt, vielfach verändert und ausgegeben. Bei schlechten Startwerten (z.B.: $[1, 1, 1, ..., 1, 1]$, 624 mal) benötigt der Algorithmus eine Aufwärmphase von idealerweise 800.000 Aufrufen, also 800.000 Zufallszahlen, um eine gleichverteilte Bitsequenz (guter Zufall) zu garantieren. Der Mersenne-Twister ist deterministisch, d.h. bei gleichem 624 Zustandswort Input auch immer der gleiche Output herauskommt. Anzumerken ist noch, dass der Mersenne-Twister nicht kryptographisch sicher ist.

https://de.wikipedia.org/wiki/Mersenne-Twister
https://en.wikipedia.org/wiki/Mersenne_Twister
https://de.wikipedia.org/wiki/Quantenmechanische_Messung
https://de.wikipedia.org/wiki/Quantencomputer