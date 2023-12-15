# Client to demonstrate usage

from player import *
from cache import *
from latency_cache import *
import pandas as pd
import time

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
    parse_csv('testProfiles1000-5000.csv')
    cache = Cache(15)
    tic = time.perf_counter()
    for player in matchmaking_queue:
        cache.add(player)

    print("Added to game: ")
    print(cache.matchmake())
    print(str(cache.getRetrieveCount()) + " retrievals")
    print(f"{time.perf_counter() - tic:0.4f} seconds") 


    lcache = Latency_Cache(15)
    tic = time.perf_counter()
    for player in matchmaking_queue:
        lcache.add(player)

    print("Added to game: ")
    print(lcache.matchmake())
    print(str(lcache.getRetrieveCount()) + " retrievals")
    print(f"{time.perf_counter() - tic:0.4f} seconds") 



if __name__ == "__main__":
    main()