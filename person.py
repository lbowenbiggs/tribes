class Person:
    def __init__(self):
        self.type = "Peasant"
        self.village = None

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
