# Monster-Demo – Musterlösung DS1
# Nicht vor der Stunde verteilen!

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


class Krieger(Monster):
    def __init__(self, name, hp, angriff, ruestung):
        super().__init__(name, hp, angriff)
        self.ruestung = ruestung

    def block(self):
        print(f"{self.name} blockt! Rüstungswert: {self.ruestung}")


class Magier(Monster):
    def __init__(self, name, hp, angriff, mana):
        super().__init__(name, hp, angriff)
        self.mana = mana

    def zauber(self, ziel):
        if self.mana >= 10:
            schaden = self.angriff * 2
            ziel.hp -= schaden
            self.mana -= 10
            print(f"{self.name} wirkt einen Zauber auf {ziel.name}! Schaden: {schaden}. Verbleibende HP: {ziel.hp}")
        else:
            print(f"{self.name} hat kein Mana mehr!")

    def status(self):
        super().status()
        print(f"  Mana: {self.mana}")


# Testlauf
if __name__ == "__main__":
    goblin = Monster("Goblin", 30, 5)
    held   = Krieger("Arthus", 100, 15, 30)
    hexe   = Magier("Morgana", 60, 20, 50)

    print("=== Statusübersicht ===")
    goblin.status()
    held.status()
    hexe.status()

    print("\n=== Kampf ===")
    hexe.zauber(goblin)
    held.angreifen(goblin)
    goblin.angreifen(held)
    held.block()
    hexe.zauber(hexe)   # Testet "Kein Mana" nach mehrfachem Zaubern
