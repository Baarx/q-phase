# Algorithmen & Datenstrukturen – Vorlagen DS2

# ── TEIL 1: Rekursion ────────────────────────────────────────────────

def fakultaet(n):
    """Berechnet n! rekursiv."""
    if n <= 1:
        return 1
    return n * fakultaet(n - 1)


def summe(n):
    """Aufgabe 6: Vervollständige diese Funktion!
    Berechnet rekursiv 1 + 2 + ... + n
    """
    # TODO: Basisfall
    # TODO: Rekursiver Fall
    pass


# ── TEIL 2: Stack ────────────────────────────────────────────────────

class Stack:
    """Einfacher Stack (LIFO) mit Liste."""
    def __init__(self):
        self._daten = []

    def push(self, element):
        self._daten.append(element)

    def pop(self):
        if self.ist_leer():
            raise IndexError("Stack ist leer!")
        return self._daten.pop()

    def peek(self):
        """Zeigt oberstes Element ohne es zu entfernen."""
        if self.ist_leer():
            raise IndexError("Stack ist leer!")
        return self._daten[-1]

    def ist_leer(self):
        return len(self._daten) == 0

    def __str__(self):
        return f"Stack{self._daten} ← TOP"


# ── TEIL 3: Queue ────────────────────────────────────────────────────

from collections import deque

class Queue:
    """Einfache Queue (FIFO)."""
    def __init__(self):
        self._daten = deque()

    def enqueue(self, element):
        self._daten.append(element)

    def dequeue(self):
        if self.ist_leer():
            raise IndexError("Queue ist leer!")
        return self._daten.popleft()

    def ist_leer(self):
        return len(self._daten) == 0

    def __str__(self):
        return f"Queue FRONT→ {list(self._daten)} ←BACK"


# ── TEIL 4: Sortierung ───────────────────────────────────────────────

def bubblesort(liste):
    """Sortiert eine Liste mit Bubblesort (in-place)."""
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste


def mergesort(liste):
    """Sortiert eine Liste mit Mergesort (gibt neue Liste zurück)."""
    if len(liste) <= 1:
        return liste
    mitte = len(liste) // 2
    links = mergesort(liste[:mitte])
    rechts = mergesort(liste[mitte:])
    return _merge(links, rechts)


def _merge(links, rechts):
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


# ── TESTBEREICH ──────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Rekursion ===")
    print(f"5! = {fakultaet(5)}")
    # print(f"summe(4) = {summe(4)}")   # Auskommentieren, wenn fertig

    print("\n=== Stack ===")
    s = Stack()
    s.push(5)
    s.push(3)
    s.push(7)
    print(s)
    print(f"pop: {s.pop()}")
    print(s)

    print("\n=== Queue ===")
    q = Queue()
    q.enqueue("Kunde 1")
    q.enqueue("Kunde 2")
    q.enqueue("Kunde 3")
    print(q)
    print(f"dequeue: {q.dequeue()}")
    print(q)

    print("\n=== Sortierung ===")
    zahlen = [5, 3, 8, 1, 9, 2, 7, 4, 6]
    print(f"Unsortiert:   {zahlen}")
    print(f"Bubblesort:   {bubblesort(zahlen[:])}")
    print(f"Mergesort:    {mergesort(zahlen)}")
