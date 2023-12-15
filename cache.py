# Cache with cache eviction algorithm
import time

'''
Cache works as follows:

10 players per game

15 players in matchmaking cache, pick top 10 to matchmake

leave 10 players in the cache

'''
class Cache:
    
    def __init__(self, max_size=15):
        self.max_size = max_size
        self.players = []
    
    def retrieveInfoFromDB(self, player):
        time.sleep(0.1)

    def add(self, player):
        if not self.contains(player):
            self.retrieveInfoFromDB(player)
            if len(self.players) < self.max_size:
                self.players.append(player)
            else:
                self.evict()
                self.players.append(player)
    
    def matchmake(self):
        game = []
        for player in sorted(self.players, key=lambda x: x.score(), reverse=True)[:10]:
            game.append(player.getName())
        return game
    
    def contains(self, player):
        for player2 in self.players:
            if player.getName() == player2.getName():
                return True
        return False

    def evict(self):
        if len(self.players) > 0:
            # Evict player with the lowest score
            self.players.remove(min(self.players, key=lambda x: x.score()))
    
    def stats(self):
        # Provide any cache statistics if needed
        pass