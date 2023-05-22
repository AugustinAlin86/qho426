from abc import ABC

class Inhabitant(ABC):

    MAX_ENERGY = 100

    def __init__(self, name="Inhabitant", age=0, energy= MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = energy

    def display(self):
        print(f"I am {self.name}")

    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.energy += amount
        if self.energy > Inhabitant.MAX_ENERGY:
            self.energy = Inhabitant.MAX_ENERGY

    def move(self, distance):
        self.energy -= distance
        if self.energy < 0:
            self.energy = 0

if __name__ == "__main__":
    jack = Inhabitant()
    jack.eat(2)
    print(jack)