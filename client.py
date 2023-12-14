# Client to demonstrate usage

from player import *
from cache import *
import pandas as pd

matchmaking_queue = []

def parse_csv(file):
    try:
        data = pd.read_csv(file)
        rows = data.values.tolist()
        for row in rows:
            p = Player (row[0], row[1], row[2], row[3], row[4], row[5])
            matchmaking_queue.append(p)
    except Exception as e:
        return f"An error occurred: {e}"


def main():    
    parse_csv('testProfiles100.csv')
    cache = Cache(15)
    # matchmaking_queue = []

    # Create 100 players (randomly)
    # for i in range(100):
    #     name = "Player "
    #     name += str(i+1)
    #     freq = i
    #     lp = i
    #     inf = i
    #     skill = i
    #     role = i % 5
    #     p = Player(name, freq, lp, inf, skill, role)
    #     matchmaking_queue.append(p)
    
    for player in matchmaking_queue:
        cache.add(player)

    print("Added to game: ")
    print(cache.matchmake()) 



if __name__ == "__main__":
    main()