from inhabitant import Inhabitant

class Robot(Inhabitant):
    MAX_ENERGY = 100

    def __init__(self, name="Robot", age=0, energy=0):
        super().__init__(name, age, energy)
        self.laws = "To Obey and Protect!"

    def __str__(self):
        return f"{self.name} of age {self.age} has {self.energy} energy"

    def __repr__(self):
        return f"Robot(name={self.name}, age={self.age}, energy={self.energy})"

    def the_laws(self):
        print(self.laws)

if __name__ == "__main__":
    r = Robot("Wall-E", 12, 88)
    r.display()
    print(r)
    print(repr(r))
    r.the_laws()

