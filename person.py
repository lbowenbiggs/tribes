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

class Peasant(Person):
    def __init__(self, village):
        self.type = "Peasant"
        self.village = village

class Baby(Person):
    def __init__(self, village):
        self.type = "Baby"
        self.village = village
        self.wounds = 1

class Farmer(Person):
    def __init__(self, village):
        self.type = "Farmer"
        self.village = village

    def onSuccess(self):
        self.village.food += 3

    def onFailure(self):
        self.village.food += 1

class Civilian(Person):
    def __init__(self, village):
        self.type = "Civilian"
        self.village = village

    def onSuccess(self):
        self.village.gold += 2

    def onFailure(self):
        self.village.population.append(Baby(self.village))
