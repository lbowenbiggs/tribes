class Village:
    def __init__(self, name):
        self.name = name
        self.population = []
        self.food = 0
        self.gold = 0

    def isEmpty(self):
        if len(self.population) == 0:
            return True
        return False

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

    def __str__(self):
        return "The Village of {0}, Population: {1}\nFood: {2}\tGold: {3}\n".format(self.name, len(self.population), self.food, self.gold)
