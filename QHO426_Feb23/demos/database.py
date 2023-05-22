from person import Person

class Database:

    def __init__(self, name):
        self.name = name + "'s database"
        self.people =[]
        self.n_ppl = len(self.people)

    def add_person(self, p):
        self.people.append(p)
        self.n_ppl += 1

    def remove_person(self,p):
        if p in self.people:
            self.people.remove(p)
        else:
            print("Person does not exist in the database")

    def display_all(self):
        for person in self.people:
            print(person)

if __name__ == "__main__":
    p1 = Person("Tadek", 67, "Truck Driver", 78)
    p2 = Person("Jamia", 54, "Teacher", 56)
    p3 = Person("Urduh", 23, "Unemployed", 77)
    db = Database("Piotr")
    db.add_person(p2)
    db.display_all()
    db.add_person(p1)
    db.remove_person(p3)
    db.add_person(p3)
    db.remove_person(p2)
    db.display_all()
