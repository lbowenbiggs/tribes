import village, person

class SurviveGame:
    def __init__(self, startingFood, startingGold, startingPopulation):
        self.villages = []
        self.maxPlayers = 2
        self.startingFood = startingFood
        self.startingGold = startingGold
        self.startingPopulation = startingPopulation
        self._play()

    def _play(self):
        self._initGame()
        self._startGame()

    def _produceStep(self):
        for village in self.villages:
            village.produce()

    def _healStep(self):
        for village in self.villages:
            village.heal()

    def _attackStep(self):
        for village in self.villages:
            village.attack()

    def _stealStep(self):
        for village in self.villages:
            village.steal()

    def _feedStep(self):
        for village in self.villages:
            village.feed()

    def _initGame(self):
        try:
            playerInput = raw_input("How many human players? ")
            numHumanPlayers = int(playerInput)
            if numHumanPlayers > self.maxPlayers or numHumanPlayers < 0:
                raise ValueError("That's not a number")
        except ValueError as err:
            print str(err)
            return self._initGame()
        self._addHumans(numHumanPlayers)
        self._initVillages()

    def _addHumans(self, numHumans):
        for index in range(0, numHumans):
            villageName = raw_input("Enter a name for village {0}: ".format(index))
            newVillage = village.Village(villageName)
            self.villages.append(newVillage)

    def _initVillages(self):
        for village in self.villages:
            village.food = self.startingFood
            village.gold = self.startingGold
            # Add initial population (This is a test batch)
            village.population.append(person.Peasant(village))
            village.population.append(person.Civilian(village))
            village.population.append(person.Farmer(village))

    def _startGame(self):
        while len(self.villages) != 0:
            for village in self.villages:
                print village
                if village.isEmpty():
                    print "The village {0} has died out".format(village.name)
                    self.villages.remove(village)
            self._produceStep()
            self._healStep()
            self._attackStep()
            self._stealStep()
            self._feedStep()
            raw_input("Waiting....")

if __name__ == '__main__':
    game = SurviveGame(5, 0, 5)
