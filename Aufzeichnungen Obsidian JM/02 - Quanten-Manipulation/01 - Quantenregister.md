
Schreibweisen:
$$
|\psi \rangle = |\varphi_1\rangle |\varphi_2\rangle = |\varphi_1\varphi_2\rangle = |\varphi_1\rangle \otimes  |\varphi_2\rangle
$$
Tensorprodukte Beispiel:
$$
\begin{pmatrix} 1   \\ 2 \end{pmatrix} \otimes \begin{pmatrix} 3   \\ 4 \end{pmatrix}  = \begin{pmatrix} 1 \cdot \begin{pmatrix} 3  \\ 4 \end{pmatrix}  \\ 2 \cdot \begin{pmatrix} 3   \\ 4 \end{pmatrix} \end{pmatrix} =\begin{pmatrix} 3  \\ 4 \\ 6 \\ 8 \end{pmatrix} 
$$
Ausrechnen des Quantenregisters mit zwei Qubits:
$$
=\left[ \alpha _1 \cdot\begin{pmatrix}1\\0\end{pmatrix}+\beta_1 \cdot\begin{pmatrix}0\\1\end{pmatrix}\right] \otimes 
\left[ \alpha _2 \cdot\begin{pmatrix}1\\0\end{pmatrix}+\beta_2 \cdot\begin{pmatrix}0\\1\end{pmatrix}\right]
$$
$$
=\alpha_1\alpha_2\begin{pmatrix}1\\0\\0\\0\end{pmatrix}+\alpha_1\beta_2\begin{pmatrix}0\\1\\0\\0\end{pmatrix}+\alpha_2\beta_1\begin{pmatrix}0\\0\\1\\0\end{pmatrix}+\beta_1\beta_2\begin{pmatrix}0\\0\\0\\1\end{pmatrix}
$$
$$
=\alpha_{00}|00\rangle + \alpha_{01}|01\rangle +\alpha_{10}|10\rangle+\alpha_{11}|11\rangle
$$
