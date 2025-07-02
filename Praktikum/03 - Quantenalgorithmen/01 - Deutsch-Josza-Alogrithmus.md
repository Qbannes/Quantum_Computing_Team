NICHT dazu da, um Rechenprobleme zu lösen
f ist ein Orakel / eine BlackBox, also unbekannt

Problem:
$$
f: \{0,1\}^n \to \{0,1\}
$$
Eingabe von x mit 
$$
0 \le x \le 2^n-1
$$

Klassischer Algoritmus:
Mindestens 
$$
2^{n-1} +1
$$
Überprüfungen, um sicher festzustellen, dass
1. f ist konstant, also jedes f(x) = 1 oder jedes f(x) = 0 oder
2. f ist balanciert, also die Hälfte aller f(x) = 1 und die andere Hälfte f(x) = 0.

Quantenalgorithmus:
![[{9F60E4C4-FB1B-41BE-84A5-178AEA694044}.png]]
...

[https://de.wikipedia.org/wiki/Deutsch-Jozsa-Algorithmus]()
