class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        Pet.play(self)
        print("Walking Pet")

    def feed(self):
        Pet.eat(self)
        print("Feeding Pet")

    def bathe(self):
        Pet.noise(self)
        print("Bathe Pet")


class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25

    def eat(self):
        pet1.energy += 5
        pet1.health += 10

    def play(self):
        pet1.health += 5

    def noise(self):
        print("Woof")


pet1 = Pet(name="Fido", type="Dog", tricks="Backflip", health=100, energy=50)

ninja1 = Ninja(first_name="Bilbo", last_name="Baggins", treats=5, pet_food="Pizza", pet=pet1)

ninja1.feed()
ninja1.walk()
ninja1.bathe()
print(pet1.energy)
print(pet1.health)

