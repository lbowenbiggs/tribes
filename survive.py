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

    def _ageStep(self):
        for village in self.villages:
            village.age()

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
            for i in range(0, self.startingPopulation):
                newVillager = None
                while (newVillager == None):
                    newVillager = village._chooseClass()
                village.population.append(newVillager)

    def _startGame(self):
        roundCounter = 0
        while len(self.villages) != 0:
            roundCounter = roundCounter + 1
            print "***** ROUND {0} *****".format(roundCounter)
            for village in self.villages:
                print village
                if village.isEmpty():
                    print "The village {0} has died out after {1} rounds".format(village.name, roundCounter)
                    self.villages.remove(village)
            raw_input("Waiting....")
            self._produceStep()
            self._healStep()
            self._attackStep()
            self._stealStep()
            self._feedStep()
            self._ageStep()

if __name__ == '__main__':
    game = SurviveGame(5, 0, 5)
