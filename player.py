from datetime import datetime

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
    
    def __init__(self, name, play_frequency, last_played, latency, infractions, skill_level, role=None):
        self.name = name
        self.play_frequency = play_frequency
        self.last_played = last_played
        self.latency = latency
        self.infractions = infractions
        self.skill_level = skill_level
        self.role = role
    
    # algorithm for computing score
    # Weigh heavily different factors (for example, latency should be prioritized)

    def score(self):

        return (
            self.play_frequency +
            (-self.last_played) * 0.1 +
            (100 - self.latency) +
            (-10 * self.infractions) +
            (2 * self.skill_level)
        )
    
    def getLatency(self):
        return self.latency
    
    def getRole(self):
        return self.role
    
    def getName(self):
        return self.name
