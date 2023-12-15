# Cache with cache eviction algorithm
import time

'''
Cache works as follows:

Stores up to max_size players

Evicts based on score

'''
class Cache:
    
    def __init__(self, max_size=15):
        self.max_size = max_size
        self.players = []
        self.retrieveCount = 0
    
    def retrieveInfoFromDB(self, player):
        time.sleep(0.01)
        self.retrieveCount+=1

    def add(self, player):
        if not self.contains(player):
            self.retrieveInfoFromDB(player)
            if len(self.players) < self.max_size:
                self.players.append(player)
            else:
                self.evict()
                self.players.append(player)
    
    def contains(self, player):
        for player2 in self.players:
            if player.getName() == player2.getName():
                return True
        return False
    
    def evict(self):
        if len(self.players) > 0:
            # Evict player with the lowest score
            self.players.remove(min(self.players, key=lambda x: x.score()))
    
    def getRetrieveCount(self):
        return self.retrieveCount
    
    def getName(self):
        return "Score Cache"