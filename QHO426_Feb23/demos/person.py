#The class Person which is a blueprint for my objects to store information about humans/people
class Person:

    #Class Attribute -> attribute/feature acessible/applied to
    #every object of the class
    MAX_W = 200

    #Static method -> Utility function, that does NOT require an object to work on
    def is_mature(age):
        if age >= 25:
            return "Person is mature"
        else:
            return "Person is immature"

    #Initialiser/Constructor -> function that is automatically
    #called when an object is instantiated (magic method)
    #Initialiser of ANY class has the same name
    #"DUNDER" - Double Underscore
    def __init__(self, name, age, job = "", w=100):
        #Below are the instance attributes (features)
        self.name = name
        self.age = age
        self.job = job
        if w > Person.MAX_W:
            self.weight = Person.MAX_W
        else:
            self.weight = w
    #Magic method str provides "informal" representation of object via string.
    #It is invoked automatically when object goes into print() function
    def __str__(self):
        return f"{self.name} is {self.age} years old. They work as {self.job} and weight {self.weight}kg"
    #Magic method repr provides "formal" representation of an object.
    #That's how you want to store your object for later
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, job={self.job}, w={self.weight})"

    #Method -> function attached to a specific data type (class)
    #Instance Method -> it applies to a specific instance of a class (object)
    def eat(self, food, w):
        print(f"{self.name} have eaten {food}")
        self.weight += w
        print(f"{self.name} now weights {self.weight:.2f} kg")

    def exercise(self, burned):
        self.weight -= burned
        print(f"{self.name} has exercised and now wieghts {self.weight:.2f} kg")

if __name__ == "__main__":
    p1 = Person("Luke", 23, "Clerk", 55)
    p2 = Person("Mary", 19, "Waitress", 48)
    p3 = Person("Udoh", 55, job="Headmaster")
    p4 = Person("Olu",23,  w=600)

    # print(f"Person 1 is called {p1.name} and Person 2 is called {p2.name}")
    # print(f"Together their total weight is {p1.weight + p2.weight}")
    print(p1)
    print(p2)
    # print(f"{p4.name} weights {p4.weight}")
    # print(f"{p3.name} weights {p3.weight} and works as {p3.job}")
    p1.eat("lasagna", 1.2)
    p1.exercise(0.4)
    p1.eat("sandwich", 0.2)
    print(p4)

    print(Person.is_mature(18))
    print(Person.is_mature(55))
    print(Person.is_mature(p2.age))