from random import randint

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
        for person in self.population:
            if person.type == "Farmer":
                roll = randint(0, 1)
                if roll == 0:
                    person._onFailure()
                else:
                    person._onSuccess()

    def heal(self):
        pass

    def attack(self):
        pass

    def steal(self):
        pass

    def feed(self):
        if self.food < len(self.population):
            print "Wounding {0} villagers".format(len(self.population) - self.food)
            self._wound(len(self.population) - self.food)
        else:
            self.food -= len(self.population)

    def _wound(self, numPeople=1):
        for i in range(numPeople):
            if self.population[0].wound() == "Death":
                self.population.pop(0)

    def __str__(self):
        return "The Village of {0}, Population: {1}\nFood: {2}\tGold: {3}\n".format(self.name, len(self.population), self.food, self.gold)
