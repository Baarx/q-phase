# Monster-Demo – Doppelstunde 1 (OOP)
# Vorlage für Schüler:innen – fehlende Teile ergänzen

class Monster:
    def __init__(self, name, hp, angriff):
        self.name = name
        self.hp = hp
        self.angriff = angriff

    def angreifen(self, ziel):
        ziel.hp -= self.angriff
        print(f"{self.name} greift {ziel.name} an! Verbleibende HP: {ziel.hp}")

    def status(self):
        print(f"{self.name}: {self.hp} HP")


# ── Aufgabe 2: Krieger-Klasse ergänzen ──────────────────────────────
class Krieger(Monster):
    def __init__(self, name, hp, angriff, ruestung):
        super().__init__(name, hp, angriff)
        self.ruestung = ruestung

    def block(self):
        # TODO: Gibt aus, wie viel Rüstung der Krieger hat
        pass


# ── Aufgabe 3: Magier-Klasse selbst schreiben ───────────────────────
# class Magier(Monster):
#     ...


# ── Testbereich ─────────────────────────────────────────────────────
if __name__ == "__main__":
    goblin = Monster("Goblin", 30, 5)
    held   = Krieger("Arthus", 100, 15, 30)

    goblin.status()
    held.status()
    held.angreifen(goblin)
    held.block()
