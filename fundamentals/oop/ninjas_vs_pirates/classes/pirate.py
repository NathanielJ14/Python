from classes.__init__ import Human

class Pirate( Human ):
    def __init__( self, name ):
        super().__init__(name)
        self.strength = 15
        self.health = 100
        self.speed = 3
    
    def attack(self, human):
        return super().attack(human)

    def show_stats(self):
        return super().show_stats()

    def battle(self, opponent):
        return super().battle(opponent)
    