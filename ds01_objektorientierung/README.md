# Doppelstunde 1 – Objektorientierte Programmierung (OOP)

> **Leitfrage:** *Wie modellieren Informatiker:innen die reale Welt im Code?*  
> **Zeitrahmen:** ca. 90 Minuten  
> **Vorwissen:** Variablen, einfache Funktionen in Python

---

## 1. Motivation: Warum OOP?

Stell dir vor, du schreibst ein Spiel mit 100 verschiedenen Monstern.  
Jedes Monster hat:
- einen **Namen**
- **Lebenspunkte**
- einen **Angriff**

Ohne OOP bräuchtest du für jedes Monster eigene Variablen:
```python
monster1_name = "Goblin"
monster1_hp = 30
monster1_angriff = 5

monster2_name = "Drachen"
monster2_hp = 200
monster2_angriff = 40
# ... und so weiter für 100 Monster 😫
```

**Lösung:** Mit OOP beschreibst du einmal den *Bauplan* eines Monsters – und erzeugst dann beliebig viele Exemplare davon.

---

## 2. Klassen und Objekte

### Die Grundidee

| Begriff | Bedeutung | Analogie |
|---------|-----------|----------|
| **Klasse** | Bauplan / Vorlage | Keksform |
| **Objekt** | Konkretes Exemplar nach dem Bauplan | Ein Keks |
| **Attribut** | Eigenschaft eines Objekts | Farbe des Kekses |
| **Methode** | Aktion/Verhalten eines Objekts | Keks essen |

### Beispiel in Python

```python
class Monster:
    # __init__ ist der "Konstruktor" – wird aufgerufen, wenn ein Objekt erstellt wird
    def __init__(self, name, hp, angriff):
        self.name = name        # Attribut
        self.hp = hp            # Attribut
        self.angriff = angriff  # Attribut

    def angreifen(self, ziel):  # Methode
        ziel.hp -= self.angriff
        print(f"{self.name} greift {ziel.name} an! Verbleibende HP: {ziel.hp}")

    def status(self):           # Methode
        print(f"{self.name}: {self.hp} HP")


# Objekte erstellen (= "Instanziieren")
goblin = Monster("Goblin", 30, 5)
drachen = Monster("Drachen", 200, 40)

# Methoden aufrufen
goblin.status()       # Goblin: 30 HP
drachen.angreifen(goblin)  # Drachen greift Goblin an! Verbleibende HP: -10
```

### 💡 Wichtig: `self`
`self` ist der Verweis des Objekts auf sich selbst. Über `self.attributname` greift ein Objekt auf seine eigenen Daten zu.

---

## 3. UML-Klassendiagramm

In der Q-Phase arbeitet ihr oft mit **UML-Klassendiagrammen** – das sind Bilder, die zeigen, wie Klassen aufgebaut sind, ohne Code zu schreiben.

```
┌──────────────────────┐
│       Monster        │  ← Klassenname
├──────────────────────┤
│ - name: String       │  ← Attribute (mit Typ)
│ - hp: int            │
│ - angriff: int       │
├──────────────────────┤
│ + angreifen(ziel)    │  ← Methoden
│ + status()           │
└──────────────────────┘
```

> **Konvention:** `-` bedeutet *privat* (nur die Klasse selbst kann es nutzen), `+` bedeutet *öffentlich* (von außen aufrufbar).

---

## 4. Vererbung

Manchmal gibt es Klassen, die *ähnlich*, aber nicht identisch sind.  
Beispiel: `Magier` und `Krieger` sind beides `Monster` – aber jeder hat zusätzliche Eigenschaften.

**Vererbung** bedeutet: Eine Klasse *erbt* alle Eigenschaften und Methoden der Elternklasse und kann zusätzliche hinzufügen.

```python
class Krieger(Monster):   # Krieger erbt von Monster
    def __init__(self, name, hp, angriff, ruestung):
        super().__init__(name, hp, angriff)  # Elternklasse initialisieren
        self.ruestung = ruestung

    def block(self):
        print(f"{self.name} blockt! Rüstung: {self.ruestung}")


class Magier(Monster):    # Magier erbt von Monster
    def __init__(self, name, hp, angriff, mana):
        super().__init__(name, hp, angriff)
        self.mana = mana

    def zauber(self, ziel):
        if self.mana >= 10:
            ziel.hp -= self.angriff * 2
            self.mana -= 10
            print(f"{self.name} wirkt einen Zauber auf {ziel.name}!")
        else:
            print("Kein Mana!")


held = Krieger("Arthus", 100, 15, 30)
hexe = Magier("Morgana", 60, 20, 50)

held.status()       # Geerbte Methode!
hexe.zauber(held)
```

### UML mit Vererbung

```
       ┌──────────────────────┐
       │       Monster        │
       ├──────────────────────┤
       │ - name: String       │
       │ - hp: int            │
       │ - angriff: int       │
       ├──────────────────────┤
       │ + angreifen(ziel)    │
       │ + status()           │
       └──────────┬───────────┘
                  │  (Vererbung, "ist ein")
       ┌──────────┴───────────┐
       │                      │
┌─────┴──────┐        ┌───────┴──────┐
│  Krieger   │        │    Magier    │
├────────────┤        ├──────────────┤
│ -ruestung  │        │ - mana: int  │
├────────────┤        ├──────────────┤
│ + block()  │        │ + zauber()   │
└────────────┘        └──────────────┘
```

**Merksatz:** "Krieger *ist ein* Monster" → Vererbung ist die "ist-ein"-Beziehung.

---

## 5. Aufgaben

### 🟢 Aufgabe 1 – Klasse entwerfen (Papier/Whiteboard)

Entwerfe ein UML-Klassendiagramm für ein `Auto`:
- Welche **Attribute** hat ein Auto? (mind. 4)
- Welche **Methoden** (Aktionen) kann ein Auto ausführen? (mind. 3)

---

### 🟢 Aufgabe 2 – Klasse in Python umsetzen

Schreibe die Python-Klasse für dein `Auto` aus Aufgabe 1.  
Erstelle danach **zwei verschiedene Auto-Objekte** und rufe jeweils eine Methode auf.

---

### 🟡 Aufgabe 3 – Vererbung lesen

Lies das folgende UML-Diagramm und beantworte die Fragen:

```
       ┌──────────────────────┐
       │       Tier           │
       ├──────────────────────┤
       │ - name: String       │
       │ - gewicht: float     │
       ├──────────────────────┤
       │ + fressen()          │
       │ + schlafen()         │
       └──────────┬───────────┘
                  │
       ┌──────────┴───────────┐
       │                      │
┌─────┴──────┐        ┌───────┴──────┐
│   Hund     │        │    Vogel     │
├────────────┤        ├──────────────┤
│ - rasse    │        │ - flugweite  │
├────────────┤        ├──────────────┤
│ + bellen() │        │ + fliegen()  │
└────────────┘        └──────────────┘
```

a) Welche Attribute hat ein `Hund`-Objekt insgesamt?  
b) Kann ein `Vogel`-Objekt die Methode `schlafen()` aufrufen? Begründe.  
c) Was bedeutet der Pfeil zwischen `Tier` und `Hund`?

---

### 🟡 Aufgabe 4 – Vererbung in Python

Erstelle auf Basis des UML-Diagramms aus Aufgabe 3 die drei Python-Klassen `Tier`, `Hund` und `Vogel`.  

- `Hund.bellen()` soll `"Wuff!"` ausgeben.  
- `Vogel.fliegen()` soll ausgeben, wie weit der Vogel fliegen kann.

Teste mit:
```python
bello = Hund("Bello", 12.5, "Labrador")
tweety = Vogel("Tweety", 0.3, 500)
bello.fressen()    # Geerbte Methode
bello.bellen()
tweety.fliegen()
```

---

### 🔴 Aufgabe 5 – Eigenes Modell

Modelliere ein System deiner Wahl (z. B. Schule, Streaming-Dienst, Online-Shop).

- Entwirf mindestens **2 Klassen**, die voneinander erben.
- Zeichne das UML-Klassendiagramm.
- Implementiere das Modell in Python.
- Schreibe ein kleines Testskript, das zeigt, wie die Klassen zusammenspielen.

---

## 6. Lösungshinweise

<details>
<summary>Lösung Aufgabe 2 – Auto (Beispiel)</summary>

```python
class Auto:
    def __init__(self, marke, modell, ps, farbe):
        self.marke = marke
        self.modell = modell
        self.ps = ps
        self.farbe = farbe
        self.tankstand = 100  # in Prozent

    def fahren(self, km):
        verbrauch = km * 0.01
        self.tankstand -= verbrauch
        print(f"{self.marke} {self.modell} fährt {km} km. Tank: {self.tankstand:.1f}%")

    def tanken(self):
        self.tankstand = 100
        print("Vollgetankt!")

    def beschreibung(self):
        print(f"{self.farbe} {self.marke} {self.modell} mit {self.ps} PS")


mein_auto = Auto("VW", "Golf", 115, "Blau")
nachbars_auto = Auto("BMW", "M3", 480, "Schwarz")

mein_auto.beschreibung()
mein_auto.fahren(300)
nachbars_auto.fahren(50)
```
</details>

<details>
<summary>Lösung Aufgabe 3</summary>

a) `name`, `gewicht` (von Tier geerbt) + `rasse` (eigenes Attribut) → insgesamt 3 Attribute  
b) Ja! `Vogel` erbt von `Tier`, daher erbt er auch die Methode `schlafen()`.  
c) Der Pfeil zeigt Vererbung: `Hund` ist ein spezieller `Tier` (ist-ein-Beziehung).
</details>

<details>
<summary>Lösung Aufgabe 4</summary>

```python
class Tier:
    def __init__(self, name, gewicht):
        self.name = name
        self.gewicht = gewicht

    def fressen(self):
        print(f"{self.name} frisst.")

    def schlafen(self):
        print(f"{self.name} schläft.")


class Hund(Tier):
    def __init__(self, name, gewicht, rasse):
        super().__init__(name, gewicht)
        self.rasse = rasse

    def bellen(self):
        print("Wuff!")


class Vogel(Tier):
    def __init__(self, name, gewicht, flugweite):
        super().__init__(name, gewicht)
        self.flugweite = flugweite

    def fliegen(self):
        print(f"{self.name} kann {self.flugweite} km weit fliegen.")


bello = Hund("Bello", 12.5, "Labrador")
tweety = Vogel("Tweety", 0.3, 500)
bello.fressen()
bello.bellen()
tweety.fliegen()
```
</details>

---

## 7. Ausblick: Was kommt noch in der Q-Phase?

In der Q-Phase vertieft ihr OOP deutlich:

- **Interfaces / abstrakte Klassen**: Was, wenn eine Methode in jeder Unterklasse *anders* implementiert werden muss?
- **Polymorphismus**: Ein Objekt kann je nach Typ unterschiedlich reagieren.
- **Komplexe UML-Diagramme** mit Assoziationen, Kompositionen und Abhängigkeiten.
- OOP als Grundlage für alle weiteren Themen (Datenstrukturen, Datenbanken, …).
