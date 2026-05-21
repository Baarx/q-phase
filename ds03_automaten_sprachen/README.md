# Doppelstunde 3 – Formale Sprachen & Automaten

> **Leitfrage:** *Wie können Maschinen "denken" und Sprachen erkennen?*  
> **Zeitrahmen:** ca. 90 Minuten  
> **Vorwissen:** Grundlegende Programmierkenntnisse aus der Einführungsphase  
> **Tool:** Alle Übungen in [FLACI – flaci.com](https://flaci.com/home/)

---

## 1. Motivation – Automaten begegnen uns überall

Stell dir folgende Systeme vor:

- Eine **Ampel** wechselt in festgelegter Reihenfolge zwischen Rot, Gelb und Grün.
- Ein **Drehkreuz** am Bahnhof lässt dich nur durch, wenn du ein gültiges Ticket eingescannt hast.
- Dein **Smartphone** akzeptiert einen PIN nur, wenn die richtige Ziffernfolge eingegeben wird.
- Eine **Suchmaschine** prüft, ob deine Suchanfrage gültige Zeichen enthält.

All diese Systeme haben etwas gemeinsam: Sie befinden sich immer in einem bestimmten **Zustand** und wechseln diesen Zustand je nach **Eingabe**. Genau das beschreibt ein **endlicher Automat**.

---

## 2. Grundbegriffe: Alphabete, Wörter, Sprachen

Bevor wir Automaten bauen, brauchen wir eine gemeinsame Sprache über… Sprachen.

| Begriff | Bedeutung | Beispiel |
|---------|-----------|---------|
| **Alphabet** Σ | Endliche Menge von Zeichen | Σ = {0, 1} oder Σ = {a, b, c} |
| **Wort** | Endliche Folge von Zeichen aus Σ | `01101`, `aba`, `bbc` |
| **Leeres Wort** ε | Wort der Länge 0 | (kein Zeichen) |
| **Sprache** L | Menge von Wörtern über Σ | L = alle Wörter, die mit `a` beginnen |

**Beispiel:** Σ = {0, 1}  
- `0`, `1`, `01`, `110`, `0011` sind Wörter über diesem Alphabet.  
- L = { alle Wörter, die mit `0` enden } = { `0`, `10`, `00`, `110`, … }

> **Kernfrage der theoretischen Informatik:** Wie kann eine Maschine entscheiden, ob ein Wort zu einer Sprache gehört oder nicht?

---

### 🟢 Aufgabe 1 – Alphabete und Wörter erkunden

Öffne das interaktive Tutorial auf [flaci.com/languages](https://flaci.com/languages) und bearbeite es vollständig.

Beantworte danach schriftlich:

a) Was ist der Unterschied zwischen einem **Alphabet** und einer **Sprache**?  
b) Nenne drei Wörter über dem Alphabet Σ = {a, b} mit genau 3 Zeichen.  
c) Wie viele verschiedene Wörter der Länge 2 gibt es über Σ = {0, 1}?

---

## 3. Endliche Automaten (DEA)

### 3.1 Aufbau eines endlichen Automaten

Ein **deterministischer endlicher Automat (DEA)** besteht aus fünf Dingen:

| Bestandteil | Beschreibung |
|-------------|-------------|
| **Q** | Endliche Menge von Zuständen |
| **Σ** | Alphabet (Eingabezeichen) |
| **δ** | Übergangsfunktion: δ(Zustand, Zeichen) → nächster Zustand |
| **q₀** | Startzustand (genau einer) |
| **F** | Menge der Endzustände (Akzeptierzustände) |

### 3.2 Beispiel: Drehkreuz

Ein Drehkreuz hat zwei Zustände: **gesperrt** und **offen**.  
Eingaben: `M` (Münze einwerfen), `D` (drücken/durchgehen)

```
          M                    D
  ┌───────────────┐   ┌────────────────┐
  │               ▼   │                ▼
(gesperrt) ──M──▶ (offen) ──D──▶ (gesperrt)
  ▲   │                              │
  │   └──D (drücken, aber gesperrt)──┘  
  │      → bleibt gesperrt
  └──────────── M (nochmal einwerfen) ──┘
                → bleibt offen
```

**Formale Beschreibung:**

| | M (Münze) | D (Drücken) |
|---|---|---|
| **gesperrt** (→ Startzustand) | offen | gesperrt |
| **offen** | offen | gesperrt |

- Startzustand: `gesperrt`
- Endzustand: `offen` (Durchgang möglich)
- Wörter wie `MD`, `MMD`, `MMDD` werden akzeptiert
- Wörter wie `D`, `DDM`, `DDD` werden **nicht** akzeptiert

### 3.3 Zustandsdiagramm – die visuelle Darstellung

Im Zustandsdiagramm gilt:
- **Kreise** = Zustände
- **Doppelkreis** = Endzustand (Akzeptierzustand)
- **Pfeile** = Übergänge, beschriftet mit dem Eingabezeichen
- **Pfeil ohne Quelle** → Startzustand

```
        M           D
  ──▶ ((gesperrt)) ──M──▶ ((offen))
          ◀──────────────────D──────
          └──D──┐    └──M──┐
                ▼           ▼
             (gesperrt) (offen)   ← Schleifen
```

---

### 🟢 Aufgabe 2 – Drehkreuz in FLACI simulieren

1. Öffne den Automaten-Editor: [flaci.com/autoedit](https://flaci.com/autoedit)
2. Klicke oben auf **„Neuer Automat"** → wähle **DEA** (Deterministischer endlicher Automat)
3. Baue den Drehkreuz-Automaten nach:
   - Erstelle zwei Zustände (`gesperrt`, `offen`)
   - Markiere `gesperrt` als Startzustand (→ Pfeil)
   - Markiere `offen` als Endzustand (Doppelkreis)
   - Zeichne alle 4 Übergänge (inkl. Schleifen)
4. Teste mit dem **Simulator**:
   - Gibt `MD` einen akzeptierten Pfad?
   - Gibt `D` einen akzeptierten Pfad?
   - Was passiert bei `MMDD`?

---

### 3.4 Beispiel: Binärzahlen durch 2 teilbar

**Aufgabe des Automaten:** Erkenne alle Binärzahlen, die durch 2 teilbar sind (d. h. mit `0` enden).

Alphabet: Σ = {0, 1}

```
         0              1
  ──▶ ((q0)) ──0──▶ ((q0))   (Endzustand: endet auf 0)
          └──1──▶  (q1) ──0──▶ ((q0))
                    └──1──┘
```

**Übergangstabelle:**

| | 0 | 1 |
|---|---|---|
| **q0** (Startzustand, Endzustand) | q0 | q1 |
| **q1** | q0 | q1 |

Intuition: `q0` = "letztes Zeichen war 0 (oder Anfang)", `q1` = "letztes Zeichen war 1".  
Endet das Wort in `q0`, ist die Binärzahl durch 2 teilbar.

Teste: `110` → q0→q1→q1→q0 ✓ (6 in Dezimal, durch 2 teilbar)  
Teste: `101` → q0→q1→q0→q1 ✗ (5 in Dezimal, nicht durch 2 teilbar)

---

### 🟡 Aufgabe 3 – Binärzahl-Automat in FLACI

1. Baue den Binärzahl-Automaten aus Abschnitt 3.4 in [flaci.com/autoedit](https://flaci.com/autoedit) nach.
2. Teste mit dem Simulator:

| Wort | Erwartetes Ergebnis | Ergebnis in FLACI |
|------|--------------------|--------------------|
| `0` | ✓ akzeptiert (0) | |
| `10` | ✓ akzeptiert (2) | |
| `110` | ✓ akzeptiert (6) | |
| `1` | ✗ nicht akzeptiert | |
| `101` | ✗ nicht akzeptiert | |
| `111` | ✗ nicht akzeptiert | |

3. Bonusfrage: Was akzeptiert der Automat, wenn du `q1` statt `q0` als Endzustand setzt?

---

### 🟡 Aufgabe 4 – Eigenen Automaten entwerfen

Entwirf in [flaci.com/autoedit](https://flaci.com/autoedit) einen DEA, der folgende Sprache erkennt:

> L = { alle Wörter über Σ = {a, b}, die mit **`ab`** enden }

Beispiele:  
- `ab` ✓ | `aab` ✗ | `abb` ✗ | `bab` ✓ | `aaab` ✗ | `baab` ✗ | `bbab` ✓

Vorgehen:
1. Überlege: Welche Zustände brauche ich? (Tipp: mind. 3)
2. Zeichne den Automaten auf Papier, bevor du ihn in FLACI eingibst.
3. Teste mindestens 6 Wörter im Simulator.

<details>
<summary>Lösungshinweis – Zustände</summary>

Drei Zustände reichen:
- `q0`: Startzustand – noch kein relevantes Präfix gesehen
- `q1`: Letztes Zeichen war `a`
- `q2`: Endzustand – letzten zwei Zeichen waren `ab`

Übergänge:

| | a | b |
|---|---|---|
| q0 | q1 | q0 |
| q1 | q1 | q2 |
| q2 | q1 | q0 |
</details>

---

## 4. Akzeptor-Automaten: Was wird akzeptiert?

Ein DEA als **Akzeptor** entscheidet: Gehört ein Wort zur Sprache L oder nicht?

**Algorithmus:**
1. Starte im Startzustand q₀
2. Lies das Wort Zeichen für Zeichen
3. Folge jedem Mal dem entsprechenden Übergang
4. Nach dem letzten Zeichen: Bist du in einem **Endzustand**? → **akzeptiert** ✓  
   Bist du in keinem Endzustand? → **abgelehnt** ✗

### Zustandsübergangstabelle lesen

Gegeben sei folgende Tabelle für einen Automaten über Σ = {0, 1}:

| | 0 | 1 |
|---|---|---|
| **→ q0** | q1 | q0 |
| **q1** | q1 | q2 |
| **((q2))** | q1 | q0 |

(→ = Startzustand, (( )) = Endzustand)

**Wort `010` prüfen:** q0 →⁰ q1 →¹ q2 →⁰ q1 → **q1 ist kein Endzustand → abgelehnt** ✗  
**Wort `01` prüfen:** q0 →⁰ q1 →¹ q2 → **q2 ist Endzustand → akzeptiert** ✓

---

### 🟡 Aufgabe 5 – Tabelle analysieren und Automat bauen

Gegeben ist die Zustandsübergangstabelle von oben (Σ = {0, 1}, Endzustand q2).

a) Welche der folgenden Wörter werden akzeptiert? Zeige den Weg durch die Tabelle.

| Wort | Zustandsfolge | Akzeptiert? |
|------|--------------|-------------|
| `01` | | |
| `001` | | |
| `0101` | | |
| `11` | | |
| `ε` (leeres Wort) | | |

b) Baue diesen Automaten in [flaci.com/autoedit](https://flaci.com/autoedit) und überprüfe deine Antworten aus a) mit dem Simulator.

c) Welche Sprache beschreibt dieser Automat? Formuliere es in eigenen Worten.

<details>
<summary>Lösung a)</summary>

| Wort | Zustandsfolge | Akzeptiert? |
|------|--------------|-------------|
| `01` | q0→q1→q2 | ✓ |
| `001` | q0→q1→q1→q2 | ✓ |
| `0101` | q0→q1→q2→q1→q2 | ✓ |
| `11` | q0→q0→q0 | ✗ |
| `ε` | q0 | ✗ |

c) Der Automat akzeptiert alle Wörter, die mit `01` enden.
</details>

---

## 5. Reguläre Ausdrücke (Regex)

Reguläre Ausdrücke sind eine **kompakte Schreibweise** für Sprachen – ohne einen Automaten zeichnen zu müssen.

### 5.1 Grundsymbole

| Ausdruck | Bedeutung | Beispiel |
|----------|-----------|---------|
| `a` | Das Zeichen a | `a` matcht genau `"a"` |
| `ab` | a gefolgt von b (Konkatenation) | `ab` matcht `"ab"` |
| `a\|b` | a oder b (Alternation) | `a\|b` matcht `"a"` oder `"b"` |
| `a*` | 0 oder mehr mal a (Kleene-Stern) | `a*` matcht `""`, `"a"`, `"aa"`, … |
| `a+` | 1 oder mehr mal a | `a+` matcht `"a"`, `"aa"`, … |
| `a?` | 0 oder 1 mal a | `a?` matcht `""` oder `"a"` |
| `(ab)*` | Gruppe mit Kleene-Stern | matcht `""`, `"ab"`, `"abab"`, … |

### 5.2 Beispiele

| Regulärer Ausdruck | Beschreibung | Beispiel-Matches |
|-------------------|-------------|-----------------|
| `(0\|1)*` | Alle Binärwörter (auch leer) | `""`, `"0"`, `"10"`, `"110"` |
| `(0\|1)*0` | Alle Binärwörter, die mit 0 enden | `"0"`, `"10"`, `"110"` |
| `a*b+` | Beliebig viele a, dann mind. ein b | `"b"`, `"ab"`, `"aaab"` |
| `(ab)+` | Mindestens ein `ab` | `"ab"`, `"abab"`, `"ababab"` |

### 5.3 Zusammenhang mit Automaten

> **Satz von Kleene:** Jede reguläre Sprache (beschreibbar durch einen regulären Ausdruck) kann auch von einem endlichen Automaten erkannt werden – und umgekehrt.

FLACI kann automatisch einen DEA aus einem regulären Ausdruck generieren!

---

### 🟢 Aufgabe 6 – Reguläre Ausdrücke erkunden

Öffne das interaktive Tutorial auf [flaci.com/regexp](https://flaci.com/regexp) und bearbeite es vollständig.

Notiere danach: Welche drei Operatoren hältst du für die wichtigsten? Begründe.

---

### 🟡 Aufgabe 7 – Reguläre Ausdrücke formulieren

Formuliere reguläre Ausdrücke über Σ = {a, b} für folgende Sprachen:

a) Alle Wörter, die **nur aus a's** bestehen (auch das leere Wort)  
b) Alle Wörter, die mit **b beginnen und mit a enden**  
c) Alle Wörter, die **mindestens ein b** enthalten  
d) Alle Wörter, bei denen **nach jedem a ein b folgt** (also kein alleinstehendes a am Ende)

---

### 🟡 Aufgabe 8 – Regex zu Automat in FLACI

1. Öffne [flaci.com/autoedit](https://flaci.com/autoedit) und wähle **„Aus regulärem Ausdruck"**
2. Gib den regulären Ausdruck `(a|b)*ab(a|b)*` ein (alle Wörter, die `ab` als Teilwort enthalten)
3. Lass FLACI automatisch den DEA generieren.
4. Teste folgende Wörter:
   - `ab` ✓ | `ba` ✗ | `bab` ✓ | `aaba` ✓ | `bbbb` ✗
5. Vergleiche den generierten Automaten mit deiner Lösung aus Aufgabe 4 – was fällt auf?

<details>
<summary>Hinweis zu Aufgabe 7</summary>

a) `a*`  
b) `b(a|b)*a`  
c) `(a|b)*b(a|b)*`  
d) `(ab|b)*` (nach jedem a kommt direkt ein b, oder es kommt nur b)
</details>

---

## 6. Grenzen endlicher Automaten

Endliche Automaten sind mächtig – aber sie haben Grenzen.

**Was kann ein DEA nicht?**

> Ein DEA kann sich nicht **merken**, wie viele Zeichen er schon gesehen hat.

**Beispiel:** Die Sprache L = { aⁿbⁿ | n ≥ 1 } = { `ab`, `aabb`, `aaabbb`, … }

Diese Sprache kann **kein** endlicher Automat erkennen, weil er sich die Anzahl der `a`'s nicht merken kann (dafür bräuchte er unendlich viele Zustände).

**Lösung:** Für solche Sprachen braucht man mächtigere Maschinen:

```
Endliche Automaten (DEA)          → Reguläre Sprachen
         ↓ mächtiger
Kellerautomaten (mit Stack!)      → Kontextfreie Sprachen (z. B. Programmiersprachen)
         ↓ mächtiger
Turingmaschine                    → Alle berechenbaren Sprachen
```

### Die Turingmaschine – kurzer Ausblick

Eine **Turingmaschine** ist das theoretische Modell eines universellen Computers:
- Unbegrenztes Band (wie ein unendliches Speicherband)
- Lese-/Schreibkopf, der das Band bearbeitet
- Kann vorwärts und rückwärts laufen
- Alan Turing (1936): Alles, was ein Computer berechnen kann, kann auch eine Turingmaschine berechnen

> **These (Church-Turing):** Ein Problem ist genau dann algorithmisch lösbar, wenn es eine Turingmaschine dafür gibt.

---

### 🔴 Aufgabe 9 – Turingmaschine in FLACI erkunden

1. Öffne [flaci.com/autoedit](https://flaci.com/autoedit) und wähle als Typ **„Turingmaschine"**
2. Lade ein Beispiel (z. B. eine TM, die Einsen zählt oder Wörter spiegelt)
3. Beobachte die Simulation:
   - Was ist der Unterschied zum DEA?
   - Was kann die Turingmaschine, was der DEA nicht konnte?
4. Erkläre in 3–4 Sätzen, warum eine Turingmaschine mächtiger ist als ein DEA.

---

## 7. Zusammenfassung

| Konzept | Kernidee |
|---------|---------|
| **Alphabet / Wort / Sprache** | Grundbausteine zum Beschreiben von Zeichenfolgen |
| **DEA** | Maschine mit endlich vielen Zuständen, erkennt reguläre Sprachen |
| **Zustandsdiagramm** | Visuelle Darstellung eines Automaten |
| **Akzeptor** | DEA entscheidet: Wort ∈ L oder nicht? |
| **Regulärer Ausdruck** | Kompakte Notation für reguläre Sprachen |
| **Kleene-Satz** | DEA und reguläre Ausdrücke beschreiben dieselben Sprachen |
| **Turingmaschine** | Universelles Berechnungsmodell, mächtiger als DEA |

---

## 8. Ausblick: Was kommt in der Q-Phase?

- **Minimierung von DEAs**: Automaten mit möglichst wenigen Zuständen bauen
- **NEA → DEA Umwandlung**: Nicht-deterministische Automaten (mehrere Übergänge pro Zeichen)
- **Kellerautomaten**: DEA + Stack → erkennt Programmiersprachen
- **Chomsky-Hierarchie**: Vier Klassen von Sprachen (Typ 0–3)
- **Turingmaschinen** im Detail: Berechenbarkeit und Entscheidbarkeit
- Im **LK**: Halteproblem – es gibt Probleme, die kein Computer lösen kann

---

## Ressourcen

- [flaci.com/languages](https://flaci.com/languages) – Tutorial: Formale Sprachen
- [flaci.com/regexp](https://flaci.com/regexp) – Tutorial: Reguläre Ausdrücke
- [flaci.com/autoedit](https://flaci.com/autoedit) – Automaten-Editor (DEA, NEA, Turingmaschine)
- [FLACI Desktop App (Mac/Windows/Linux)](https://flaci.com/home/#downloads) – Offline-Version
