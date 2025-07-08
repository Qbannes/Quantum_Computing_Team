Hier sind **verschiedene Sortieralgorithmen** in Python, visualisiert in Jupyter Notebook mit Matplotlib, um den Sortiervorgang Schritt für Schritt zu zeigen:

---------------------------------------------------------------

### **1. Bubble Sort**  
*Einfach, aber langsam (O(n²))*  
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr.copy()  # Für Visualisierung

# Beispiel:
data = [64, 34, 25, 12, 22, 11, 90]
```

---------------------------------------------------------------

### **2. Merge Sort**  
*Rekursiv, effizient (O(n log n))*  
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        yield from merge_sort(L)
        yield from merge_sort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            yield arr.copy()
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            yield arr.copy()
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            yield arr.copy()

# Beispiel:
data = [38, 27, 43, 3, 9, 82, 10]
```

---------------------------------------------------------------

### **3. Quick Sort**  
*Divide-and-Conquer (O(n log n) im Durchschnitt*  
```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = yield from partition(arr, low, high)
        yield from quick_sort(arr, low, pi-1)
        yield from quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr.copy()
    arr[i+1], arr[high] = arr[high], arr[i+1]
    yield arr.copy()
    return i + 1

# Beispiel:
data = [10, 80, 30, 90, 40, 50, 70]
```

---------------------------------------------------------------

### **Visualisierung in Jupyter**  
Nutze Matplotlib, um den Sortiervorgang als Animation anzuzeigen:  
```python
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
import time

def visualize_sorting(algorithm, data):
    fig, ax = plt.subplots(figsize=(10, 6))
    bar_rects = ax.bar(range(len(data)), data, color='skyblue')
    ax.set_title(f'{algorithm.__name__} Sort', fontsize=15)
    ax.set_xlabel('Index', fontsize=12)
    ax.set_ylabel('Value', fontsize=12)
    
    for step in algorithm(data.copy()):  # data.copy() für Unveränderlichkeit
        for rect, val in zip(bar_rects, step):
            rect.set_height(val)
        clear_output(wait=True)
        display(fig)
        time.sleep(0.1)  # Verlangsamt die Animation
    plt.close()

# Beispielaufruf:
visualize_sorting(bubble_sort, data)
```

---------------------------------------------------------------

### **Beispielausgabe (Bubble Sort)**  
![Bubble Sort Animation](https://i.imgur.com/XYZ123.gif)  
*Jeder Balken zeigt den aktuellen Zustand des Arrays während des Sortiervorgangs.*

---------------------------------------------------------------

### **Weitere Algorithmen**  
- **Insertion Sort**:  
  ```python
  def insertion_sort(arr):
      for i in range(1, len(arr)):
          key = arr[i]
          j = i-1
          while j >= 0 and key < arr[j]:
              arr[j+1] = arr[j]
              j -= 1
              yield arr.copy()
          arr[j+1] = key
          yield arr.copy()
  ```
- **Selection Sort**:  
  ```python
  def selection_sort(arr):
      for i in range(len(arr)):
          min_idx = i
          for j in range(i+1, len(arr)):
              if arr[j] < arr[min_idx]:
                  min_idx = j
          arr[i], arr[min_idx] = arr[min_idx], arr[i]
          yield arr.copy()
  ```

---------------------------------------------------------------

### **Tipps für Jupyter**  
1. **Installation**:  
   ```bash
   pip install matplotlib ipython
   ```  
2. **Interaktive Widgets**:  
   ```python
   from ipywidgets import interact
   @interact(algorithm=['bubble', 'merge', 'quick'])
   def show_sort(algorithm):
       if algorithm == 'bubble':
           visualize_sorting(bubble_sort, data)
       elif algorithm == 'merge':
           visualize_sorting(merge_sort, data)
       elif algorithm == 'quick':
           visualize_sorting(quick_sort, data)
   ```  

Mit diesem Code kannst du verschiedene Sortieralgorithmen live in Jupyter erkunden

Hier ist eine **komplette Anleitung**, wie du CSV-Daten einliest, Spalten auswählst und Sortieralgorithmen darauf anwendest – inklusive Visualisierung in Jupyter:

---

### **1. CSV einlesen & Spalten auswählen**
```python
import pandas as pd

# CSV laden (Beispiel: Datei mit Spalten "Name", "Alter", "Gehalt")
df = pd.read_csv("daten.csv")  # Pfad anpassen
print(df.head())  # Zeige die ersten 5 Zeilen

# Spalte auswählen (z. B. "Gehalt" als Liste)
daten = df["Gehalt"].tolist()  # Oder df["Alter"], etc.
print("Unsortiert:", daten)
```

---

### **2. Sortieralgorithmus anwenden**  
*(Nutze einen der Algorithmen von oben, z. B. Bubble Sort)*  
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr  # Rückgabe des sortierten Arrays

# Sortiere die ausgewählte Spalte
sortierte_daten = bubble_sort(daten.copy())  # .copy() vermeidet Überschreiben
print("Sortiert:", sortierte_daten)
```

---

### **3. Visualisierung der Sortierung (Schritt-für-Schritt)**  
```python
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
import time

def visualize_sorting(algorithm, data):
    fig, ax = plt.subplots(figsize=(10, 5))
    bar_rects = ax.bar(range(len(data)), data, color='skyblue')
    ax.set_title(f'{algorithm.__name__} - CSV-Daten', fontsize=14)
    
    for step in algorithm(data.copy()):  # Generator für Schritte
        for rect, val in zip(bar_rects, step):
            rect.set_height(val)
        clear_output(wait=True)  # Überschreibe vorherige Ausgabe
        display(fig)            # Zeige aktualisiertes Diagramm
        time.sleep(0.3)         # Pause für Animation
    plt.close()

# Beispiel mit Bubble Sort (Generator-Version)
def bubble_sort_gen(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr.copy()  # Für Animation

# Visualisierung starten
visualize_sorting(bubble_sort_gen, daten)
```

---

### **4. Beispiel-CSV-Inhalt & Ergebnis**  
**daten.csv** (Beispiel):  
```
Name,Alter,Gehalt
Anna,28,45000
Bob,32,60000
Clara,24,30000
David,45,75000
```
**Ausgabe**:  
- Vorher: `[45000, 60000, 30000, 75000]`  
- Nachher: `[30000, 45000, 60000, 75000]`  

![Sortieranimation](https://i.imgur.com/xyz456.gif)  
*Balken zeigen die Gehälter während des Sortiervorgangs.*

---

### **Wichtige Hinweise**  
1. **CSV-Format**:  
   - Stelle sicher, dass die CSV-Spalten numerische Werte enthalten (z. B. `int`/`float`).  
   - Bei Problemen: `daten = pd.to_numeric(df["Gehalt"]).tolist()` erzwingt Zahlen.  

2. **Andere Algorithmen**:  
   Ersetze `bubble_sort` durch `merge_sort`, `quick_sort`, etc. (siehe vorige Beispiele).  

3. **Große Datensätze**:  
   - Für >1000 Einträge: Nutze effiziente Algorithmen (Merge/Quick Sort).  
   - Deaktiviere die Animation (`time.sleep(0)`), da sie sonst langsam wird.  

4. **Daten speichern**:  
   ```python
   df["Gehalt_sortiert"] = sortierte_daten
   df.to_csv("daten_sortiert.csv", index=False)
   ```

---

Mit diesen Schritten kannst du **beliebige CSV-Daten einlesen, sortieren und visualisieren**!