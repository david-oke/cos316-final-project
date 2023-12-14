# Client to demonstrate usage

from player import *
from cache import *

def main():    
    cache = Cache(15)
    matchmaking_queue = []

    # Create 100 players (randomly)
    for i in range(100):
        name = "Player "
        name += str(i+1)
        freq = i
        lp = i
        inf = i
        skill = i
        role = i % 5
        p = Player(name, freq, lp, inf, skill, role)
        matchmaking_queue.append(p)
    
    for player in matchmaking_queue:
        cache.add(player)

    print("Added to game: ")
    print(cache.matchmake()) 



if __name__ == "__main__":
    main()