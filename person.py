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

    def heal(self, amount=1):
        # For now, there is no Maximum Health
        self.wounds += 1

''' Basic types: No actions '''
class Peasant(Person):
    def __init__(self, village):
        self.type = "Peasant"
        self.village = village

class Baby(Person):
    def __init__(self, village):
        self.type = "Baby"
        self.village = village
        self.wounds = 1

''' Producers '''
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

''' Special Types '''
class Medic(Person):
    def __init__(self, village):
        self.type = "Medic"
        self.village = village

    def onSuccess(self):
        self.village.healWounds()

    def onFailure(self):
        pass
