class Person:
    wounds = 2

    def __init__(self):
        self.type = "Peasant"
        self.village = None
        self.wounds = 2

    def wound(self, amount=1):
        self.wounds -= amount
        if self.wounds < 1:
            return "Death"

class Farmer(Person):
    def __init__(self, village):
        self.type = "Farmer"
        self.village = village

    def _onSuccess(self):
        self.village.food += 3

    def _onFailure(self):
        self.village.food += 1

class Peasant(Person):
    def __init__(self, village):
        self.type = "Peasant"
        self.village = village
