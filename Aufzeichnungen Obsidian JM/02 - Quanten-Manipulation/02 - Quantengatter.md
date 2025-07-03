Keine standardisierte Technologie für Qubits.
Reversibilität.

3 Grundgatter (X, Y, Z) als [[04 - Matrizen multiplizieren]].
$$
X = \begin{pmatrix} 0  & 1\\ 1 & 0 \end{pmatrix} 
$$
$$
Y = \begin{pmatrix} 0  & -\mathrm{i} \\ \mathrm{i} & 0 \end{pmatrix} 
$$
$$
Z = \begin{pmatrix} 1  & 0 \\ 0 & -1 \end{pmatrix} 
$$
Rotation der Blochkugel um die jeweilige Achse.
Hadamard-Gatter: 
$$
H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1  & 1 \\ 1 & -1 \end{pmatrix} 
$$
$$
H \cdot |0\rangle =  \frac{1}{\sqrt{2}}\begin{pmatrix} 1   \\ 1  \end{pmatrix}  = \frac{1}{\sqrt{2}}(|0\rangle +|1\rangle)
$$
50/50 Superpositionszustand.

Erster Quantenalgorithmus: Zufallszahlengenerator:
$$
|0\rangle \to \fbox{H} \to \fbox{Messung} \to \text{Zufallszahl}
$$
