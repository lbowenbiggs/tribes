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
            if person.type == "Farmer" or person.type == "Civilian":
                roll = randint(0, 1)
                if roll == 0:
                    person.onFailure()
                else:
                    person.onSuccess()

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

    def _printVillagers(self):
        string = "ID\tType\tWounds\n"
        count = 1
        for villager in self.population:
            string += "{0}\t{1}\t{2}\n".format(count, villager.type, villager.wounds)
            count += 1
        return string

    def __str__(self):
        string = "The Village of {0}, Population: {1}\nFood: {2}\tGold: {3}\n".format(self.name, len(self.population), self.food, self.gold)
        string += self._printVillagers()
        return string
