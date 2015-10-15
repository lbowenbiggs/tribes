import village

class SurviveGame:
    def __init__(self):
        self.villages = []
        self.maxPlayers = 2
        self._play()

    def _play(self):
        self._initGame()
        self._startGame()

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
            village.food = 5
            village.gold = 0
            # Add initial population

    def _startGame(self):
        for village in self.villages:
            print "The village of {0} has population {1}, food {2}, gold {3}".format(village.name, len(village.population), village.food, village.gold)

if __name__ == '__main__':
    game = SurviveGame()
