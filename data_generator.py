import csv
from random import randint
import argparse

'''
Generates a csv file given a number of needed players
Theoretically, code should work for a realistic set of players,
but this acts as a substitute
'''

def generate(players, entries):
    with open('testProfiles' + str(players) + '-' + str(entries) + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["ID", "Play Frequency", "Time Since Played", "Latency", "Infractions", "Skill Level", "Role"]
        writer.writerow(field)
        playerList = []

        for i in range(players):
            name = "Player "
            name += str(i+1)
            freq = randint(0, 24)
            lat = randint(0, 200)
            lp = randint(0, 24)
            inf = randint(0, 5)
            skill = randint(0, 100)
            role = randint(0, 4)
            playerList.append([name, freq, lp, lat, inf, skill, role])
        
        for i in range(entries):
            writer.writerow(playerList[randint(0, len(playerList) - 1)])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('players', type=int, help='Number of players')
    parser.add_argument('entries', type=int, help='Number of entries')
    args = parser.parse_args()
    generate(args.players, args.entries)

if __name__ == '__main__':
    main()