from random import randint
import person

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
        for villager in self.population:
            if villager.type == "Medic":
                roll = randint(0, 1)
                if roll == 0:
                    villager.onFailure()
                else:
                    villager.onSuccess()

    def attack(self):
        pass

    def steal(self):
        pass

    def age(self):
        # 1) Babies grow up
        for villager in self.population:
            if villager.type == "Baby":
                self.population.remove(villager)
                self.population.append(person.Peasant(self))
        # 2) Train villagers
        for villager in self.population:
            if villager.type == "Peasant" and self.gold > 1:
                if (self._saysYes("Would you like to train this Peasant?")):
                    newVillager = self._chooseClass()
                    if (newVillager != None):
                        self.population.remove(villager)
                        self.population.append(newVillager)
                        self.gold = self.gold - 2
                    else:
                        print "Peasant not trained"
        # 3) Untrain villagers

    def feed(self):
        if self.food < len(self.population):
            print "Wounding {0} villagers".format(len(self.population) - self.food)
            self._wound(len(self.population) - self.food)
        else:
            self.food -= len(self.population)

    def healWounds(self, amount=2):
        for i in range(amount):
            healed = self._chooseVillager("Who do you want to heal? ")
            self.population[healed].heal()

    def _wound(self, numPeople=1):
        for i in range(numPeople):
            starving = self._chooseVillager("Who do you want to wound? ")
            if self.population[starving].wound() == "Death":
                self.population.pop(starving)

    def _saysYes(self, prompt):
        playerInput = raw_input(prompt)
        if "Y" in playerInput.upper():
            return True
        return False

    def _chooseClass(self):
        if (self._saysYes("Medic?")):
            return person.Medic(self)
        if (self._saysYes("Farmer?")):
            return person.Farmer(self)
        if (self._saysYes("Civilian?")):
            return person.Civilian(self)

    def _chooseVillager(self, prompt):
        print self._printVillagers()
        try:
            playerInput = raw_input(prompt)
            chosenOne = int(playerInput)
            if chosenOne > len(self.population) or chosenOne < 0:
                raise ValueError("That's not a number")
        except ValueError as err:
            # print str(err)
            return self._chooseVillager(prompt)
        return chosenOne - 1

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
