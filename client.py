# Client to demonstrate usage

from player import *
from cache import *
from fifo_cache import *
import pandas as pd
import argparse
import time

matchmaking_queue = []
CACHES = [Cache, FIFO_Cache]
def parse_csv(file):
    try:
        data = pd.read_csv(file)
        rows = data.values.tolist()
        for row in rows:
            p = Player (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            matchmaking_queue.append(p)
    except Exception as e:
        return f"An error occurred: {e}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('cache', type=int, help='Cache Type')
    parser.add_argument('max', type=int, help='Max Size')
    args = parser.parse_args()

    parse_csv('testProfiles10000-50000.csv')
    cache = CACHES[args.cache](args.max)
    print(cache.getName())
    
    total_time = 0
    groups = 0 
    noComplete = False
    for i in range(0, int(len(matchmaking_queue) / 5)):
        tic = time.perf_counter()
        roles = set()
        index = 0
        while len(roles) < 5:
            if not matchmaking_queue[index].getRole() in roles:
                roles.add(matchmaking_queue[index].getRole())
                cache.add(matchmaking_queue.pop(index))
                index = 0
            else:
                index += 1
                if index >= len(matchmaking_queue):
                    noComplete = True
                    break
        if noComplete:
            break
        toc = time.perf_counter()
        total_time += toc - tic
        groups += 1
    
    print(total_time/groups)
    print(str(cache.getRetrieveCount()) + " retrievals")




if __name__ == "__main__":
    main()