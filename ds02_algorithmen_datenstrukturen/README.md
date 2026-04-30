# Doppelstunde 2 – Algorithmen & Datenstrukturen

> **Leitfrage:** *Wie verwaltet ein Computer Daten effizient?*  
> **Zeitrahmen:** ca. 90 Minuten  
> **Vorwissen:** Listen in Python, einfache Schleifen

---

## 1. Motivation: Wozu brauchen wir das?

Stell dir vor, du bist Entwickler:in bei Spotify:
- 100 Millionen Songs in der Datenbank
- Nutzer:in sucht einen Song – Antwort soll in **Millisekunden** kommen

Wie findet man so schnell den richtigen Song?  
**→ Mit den richtigen Datenstrukturen und Algorithmen!**

---

## 2. Rekursion – Denken in Teilproblemen

### Die Idee

Rekursion bedeutet: Eine Funktion löst ein Problem, indem sie sich selbst mit einem **kleineren Teilproblem** aufruft – bis das Problem so klein ist, dass es direkt gelöst werden kann.

```
Fakultät(5) = 5 × Fakultät(4)
                   = 4 × Fakultät(3)
                        = 3 × Fakultät(2)
                             = 2 × Fakultät(1)
                                  = 1  ← Basisfall!
```

### Zwei Zutaten jeder Rekursion

1. **Basisfall**: Das kleinste Problem, das direkt lösbar ist (kein weiterer Aufruf)
2. **Rekursiver Fall**: Das Problem wird kleiner gemacht und die Funktion ruft sich selbst auf

### Beispiel in Python

```python
def fakultaet(n):
    if n <= 1:           # Basisfall
        return 1
    return n * fakultaet(n - 1)   # Rekursiver Fall

print(fakultaet(5))   # 120
print(fakultaet(0))   # 1
```

### ⚠️ Was kann schiefgehen?

```python
def endlos(n):
    return n * endlos(n - 1)   # Kein Basisfall → unendliche Rekursion!
```

Python bricht nach ca. 1000 Aufrufen mit `RecursionError` ab.

---

## 3. Datenstrukturen: Stack und Queue

### 3.1 Stack (Stapel)

Ein Stack funktioniert wie ein Tellerstapel: **Last In, First Out (LIFO)**  
→ Das zuletzt abgelegte Element wird zuerst herausgenommen.

```
Einfügen (push):   [  ] → [A] → [A,B] → [A,B,C]
Herausnehmen (pop):          [A,B,C] → [A,B] → [A] → [  ]
```

**Alltagsbeispiele:**
- Browser-Verlauf (Zurück-Taste)
- Rückgängig-Funktion (Ctrl+Z)
- Funktionsaufrufe im Programm

**Python-Implementierung:**
```python
stack = []

stack.append("Seite 1")   # push
stack.append("Seite 2")   # push
stack.append("Seite 3")   # push

print(stack)              # ['Seite 1', 'Seite 2', 'Seite 3']
print(stack.pop())        # 'Seite 3'  ← zuletzt rein, zuerst raus
print(stack.pop())        # 'Seite 2'
```

---

### 3.2 Queue (Warteschlange)

Eine Queue funktioniert wie eine Kassenschlange: **First In, First Out (FIFO)**  
→ Das zuerst abgelegte Element wird zuerst herausgenommen.

```
Einfügen (enqueue):  [  ] → [A] → [A,B] → [A,B,C]
Herausnehmen (dequeue):       [A,B,C] → [B,C] → [C] → [  ]
```

**Alltagsbeispiele:**
- Druckerwarteschlange
- Ticketkauf online (Warteschlange)
- Netzwerkpakete (die Reihenfolge bleibt erhalten)

**Python-Implementierung:**
```python
from collections import deque

queue = deque()

queue.append("Kunde 1")    # enqueue
queue.append("Kunde 2")    # enqueue
queue.append("Kunde 3")    # enqueue

print(queue)               # deque(['Kunde 1', 'Kunde 2', 'Kunde 3'])
print(queue.popleft())     # 'Kunde 1'  ← zuerst rein, zuerst raus
print(queue.popleft())     # 'Kunde 2'
```

---

## 4. Bäume – Hierarchische Struktur

### Grundbegriffe

```
            8          ← Wurzel (root)
           / \
          3   10       ← Knoten (nodes)
         / \    \
        1   6   14     ← Blätter (leaves) – ohne Kinder
           / \
          4   7
```

| Begriff | Bedeutung |
|---------|-----------|
| **Wurzel** | Oberster Knoten (kein Elternknoten) |
| **Knoten** | Element im Baum |
| **Blatt** | Knoten ohne Kinder |
| **Kante** | Verbindung zwischen zwei Knoten |
| **Tiefe** | Anzahl Ebenen ab Wurzel |

### Binärer Suchbaum (BST)

**Regel:** Jeder Knoten hat maximal **2 Kinder**:
- Links: alle Werte **kleiner** als der aktuelle Knoten
- Rechts: alle Werte **größer** als der aktuelle Knoten

**Suchen im BST:** Bei 7 Zahlen genügen maximal 3 Vergleiche!  
Bei einer Million Zahlen: nur ~20 Vergleiche (weil sich die Möglichkeiten halbieren)!

**Einfügen der Zahlen 8, 3, 10, 1, 6, 14, 4, 7:**

Schritt 1: 8 ist Wurzel  
Schritt 2: 3 < 8 → links von 8  
Schritt 3: 10 > 8 → rechts von 8  
Schritt 4: 1 < 8 < 3? Nein: 1 < 3 → links von 3  
... und so weiter → ergibt den Baum oben.

---

## 5. Sortieralgorithmen im Vergleich

### 5.1 Bubblesort – Der Anfänger

**Idee:** Vergleiche immer zwei benachbarte Elemente. Ist das linke größer, tausche sie.  
Wiederhole, bis nichts mehr getauscht wird.

```
[5, 3, 8, 1]
 ↑  ↑         → 5 > 3? Ja, tausche: [3, 5, 8, 1]
    ↑  ↑       → 5 < 8? Nein, kein Tausch
       ↑  ↑    → 8 > 1? Ja, tausche: [3, 5, 1, 8]
Nächste Runde:
[3, 5, 1, 8]
 ↑  ↑          → 3 < 5, kein Tausch
    ↑  ↑        → 5 > 1? Ja: [3, 1, 5, 8]
...
Ergebnis: [1, 3, 5, 8]
```

```python
def bubblesort(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

print(bubblesort([5, 3, 8, 1, 9, 2]))   # [1, 2, 3, 5, 8, 9]
```

**Problem:** Bei 1000 Elementen braucht Bubblesort bis zu 1.000.000 Vergleiche! 😱

---

### 5.2 Mergesort – Teile und herrsche

**Idee (Divide and Conquer):**
1. Teile die Liste in zwei Hälften
2. Sortiere jede Hälfte (rekursiv!)
3. Füge die zwei sortierten Hälften zusammen

```
[5, 3, 8, 1]
    /      \
 [5, 3]   [8, 1]        Teilen
  / \      /  \
[5] [3]  [8]  [1]       Basisfall (1 Element = sortiert)
  ↓          ↓
[3, 5]   [1, 8]         Zusammenfügen
       ↓
  [1, 3, 5, 8]          Fertig!
```

```python
def mergesort(liste):
    if len(liste) <= 1:        # Basisfall
        return liste

    mitte = len(liste) // 2
    links = mergesort(liste[:mitte])    # Rekursion links
    rechts = mergesort(liste[mitte:])   # Rekursion rechts

    return zusammenfuegen(links, rechts)

def zusammenfuegen(links, rechts):
    ergebnis = []
    i = j = 0
    while i < len(links) and j < len(rechts):
        if links[i] <= rechts[j]:
            ergebnis.append(links[i])
            i += 1
        else:
            ergebnis.append(rechts[j])
            j += 1
    ergebnis += links[i:]
    ergebnis += rechts[j:]
    return ergebnis

print(mergesort([5, 3, 8, 1, 9, 2]))   # [1, 2, 3, 5, 8, 9]
```

**Vorteil:** Bei 1000 Elementen nur ca. 10.000 Vergleiche statt 1.000.000! 🚀

### Vergleich

| Algorithmus | Vergleiche (n Elemente) | Bewertung |
|-------------|------------------------|-----------|
| Bubblesort  | ~n² | Langsam, aber leicht verständlich |
| Mergesort   | ~n × log(n) | Deutlich schneller |
| Python intern (`sorted`) | ~n × log(n) | Optimiert, immer bevorzugen |

---

## 6. Aufgaben

### 🟢 Aufgabe 1 – Rekursion nachvollziehen

Führe die Funktion `fakultaet(4)` von Hand durch und zeige alle Zwischenschritte.

---

### 🟢 Aufgabe 2 – Stack simulieren

Gegeben sind folgende Operationen auf einem leeren Stack:
```
push(5)
push(3)
push(7)
pop()
push(1)
pop()
pop()
```

a) Zeichne den Stack nach jeder Operation.  
b) Was ist der finale Zustand des Stacks?

---

### 🟢 Aufgabe 3 – Queue simulieren

Führe die gleichen Operationen wie in Aufgabe 2 auf einer Queue aus (statt `pop()` → `dequeue()`).  
Was ist der Unterschied?

---

### 🟡 Aufgabe 4 – BST aufbauen

Füge die Zahlen **15, 6, 20, 3, 8, 17, 25** in einen binären Suchbaum ein.  
Zeichne den fertigen Baum.

Bonus: In welcher Reihenfolge wird gesucht, wenn man nach `17` sucht?

---

### 🟡 Aufgabe 5 – Bubblesort per Hand

Sortiere die Liste `[4, 2, 7, 1, 5]` mit Bubblesort.  
Schreibe nach **jedem Vergleich** den aktuellen Zustand der Liste.

---

### 🟡 Aufgabe 6 – Rekursion selbst schreiben

Schreibe eine rekursive Funktion `summe(n)`, die die Summe aller Zahlen von 1 bis n berechnet:

```
summe(4) = 4 + 3 + 2 + 1 = 10
```

Hinweis: Definiere zuerst Basisfall und rekursiven Fall auf Papier.

---

### 🔴 Aufgabe 7 – Effizienz messen

Schreibe ein Python-Programm, das:
1. Eine Liste mit 1000 Zufallszahlen erstellt (`import random`)
2. Die Liste mit Bubblesort und Mergesort sortiert
3. Die Laufzeit beider Algorithmen mit `import time` misst und vergleicht

Tipp für die Zeitmessung:
```python
import time
start = time.time()
# ... Algorithmus ...
ende = time.time()
print(f"Dauer: {ende - start:.4f} Sekunden")
```

---

## 7. Lösungshinweise

<details>
<summary>Lösung Aufgabe 1 – Rekursion</summary>

```
fakultaet(4)
  = 4 × fakultaet(3)
       = 3 × fakultaet(2)
            = 2 × fakultaet(1)
                 = 1  (Basisfall)
            = 2 × 1 = 2
       = 3 × 2 = 6
  = 4 × 6 = 24
```
</details>

<details>
<summary>Lösung Aufgabe 2 – Stack</summary>

```
push(5):  [5]
push(3):  [5, 3]
push(7):  [5, 3, 7]
pop():    [5, 3]   → 7 wurde entfernt
push(1):  [5, 3, 1]
pop():    [5, 3]   → 1 wurde entfernt
pop():    [5]      → 3 wurde entfernt
Finaler Zustand: [5]
```
</details>

<details>
<summary>Lösung Aufgabe 4 – BST</summary>

```
           15
          /   \
         6    20
        / \   / \
       3   8 17  25
```

Suche nach 17: Start bei 15 → 17 > 15 → rechts zu 20 → 17 < 20 → links zu 17 → gefunden! (3 Schritte)
</details>

<details>
<summary>Lösung Aufgabe 6 – Rekursion</summary>

```python
def summe(n):
    if n <= 0:           # Basisfall
        return 0
    return n + summe(n - 1)   # Rekursiver Fall

print(summe(4))   # 10
print(summe(10))  # 55
```
</details>

---

## 8. Ausblick: Was kommt noch in der Q-Phase?

- **Graphen**: Verallgemeinerung des Baums – für Netzwerke, Routen, soziale Netzwerke
- **Weitere Suchalgorithmen**: Lineare Suche vs. Binäre Suche
- **Komplexitätstheorie**: O-Notation – wie "misst" man formell die Effizienz eines Algorithmus?
- **AVL-Bäume** (LK): Selbstbalancierende Suchbäume
