Erzeugung von 100.000 zufälligen Bits mit dem Quantencomputer von IBM in Sherbrooke, Kanada
Nach 27 Sekunden fertiggestellt
Probleme beim Auslesen der Ergebnisse: Andere Speichermethode (vermutlich wegen größerer Datenmengen)

Eventuelle Lösung des Problems durch KI:
```
samples = result[0].data.meas.array

import numpy as np
flattened_array = samples.flatten()
```
Der erste Teil holt die Ergebnisse, der zweite Teil bringt sie in brauchbare Form.
