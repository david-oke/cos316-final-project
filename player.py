# Player representation

'''
Players have the following attributes:
    - overall play frequency
    - most recent time played
    - latency to central server
    - number of community infractions
    - skill level
    - player role?

All of the above attributes will contribute to a player 'score' 
based on the matchmaking pool they are potentially added to.

Add player to matchmaking cache:

If cache is full:
    - evict player with lowest score in the cache
'''
class Player:
    
    def __init__(self):
        pass
    
    def score(self):
        pass
