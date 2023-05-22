from inhabitant import Inhabitant
from clothing import Clothing

class Human(Inhabitant):
    MAX_ENERGY = 100

    def __init__(self, name="Human", age=0, energy=MAX_ENERGY):
        super().__init__(name, age, energy)
        self.clothing = []

    def __str__(self):
        return f"{self.name} of age {self.age} has {self.energy} energy and wears {self.clothing}"

    def __repr__(self):
        return f"Human(name={self.name}, age={self.age}, energy={self.energy}, clothing={self.clothing})"

    def dress(self, clothing):
        self.clothing.append(clothing)

    def undress(self, clothing):
        if clothing in self.clothing:
            self.clothing.remove(clothing)

if __name__ == "__main__":
    h = Human("Patrick", 29)
    h.display()
    print(h)
    print(repr(h))
    h.move(55)
    h.eat(28)
    for i in range(4):
        h.grow()
    trousers = Clothing("Blue", "Denim")
    h.dress(trousers)
    print(h)