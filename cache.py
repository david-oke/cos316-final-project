# Cache with cache eviction algorithm

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
    
    def add(self, player):
        if len(self.players) < self.max_size:
            self.players.append(player)
        else:
            self.evict()
            self.players.append(player)
    
    def get(self):
        return sorted(self.players, key=lambda x: x.score(), reverse=True)[:10]
    
    def evict(self):
        if len(self.players) > 0:
            # Evict player with the lowest score
            self.players.remove(min(self.players, key=lambda x: x.score()))
    
    def stats(self):
        # Provide any cache statistics if needed
        pass