import village

class SurviveGame:
    def __init__(self):
        self.villages = []
        self.maxPlayers = 2
        self._play()

    def _play(self):
        self._initGame()
        self._startGame()

    def _produce(self):
        for village in self.villages:
            village.produce()
    
    def _heal(self):
        for village in self.villages:
            village.heal()

    def _attack(self):
        for village in self.villages:
            village.attack()

    def _steal(self):
        for village in self.villages:
            village.steal()

    def _feed(self):
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
            village.food = 5
            village.gold = 0
            # Add initial population

    def _startGame(self):
        while len(self.villages) != 0:
            for village in self.villages:
                print village
                if village.isEmpty():
                    print "The village {0} has died out".format(village.name)
                    self.villages.remove(village)

if __name__ == '__main__':
    game = SurviveGame()
