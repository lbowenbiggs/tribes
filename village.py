class Village:
    def __init__(self, name):
        self.name = name
        self.population = []
        self.food = 0
        self.gold = 0

    def produce(self):
        pass

    def heal(self):
        pass

    def attack(self):
        pass

    def steal(self):
        pass

    def feed(self):
        self.food -= len(self.population)
