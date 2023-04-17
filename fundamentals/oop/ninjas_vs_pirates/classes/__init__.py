class Human:

    def __init__(self, name):
        self.name = name
        

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self

    def attack( self, opponent ):
        if self.health > opponent.strength:
            opponent.health -= self.strength
        if opponent.health <= 0:
            print(f"{opponent.name} has died")
        return self

    def battle(self, opponent):
        while opponent.health > 0 and self.health > 0:
            self.attack(opponent)
            opponent.attack(self)
        return self
        




