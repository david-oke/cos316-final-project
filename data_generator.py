import csv
from random import randint
import argparse

def generate(num):
    with open('testProfiles' + str(num) + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["ID", "Play Frequency", "Time Since Played", "Latency", "Infractions", "Skill Level"]
        writer.writerow(field)

        for i in range(num):
            name = "Player "
            name += str(i+1)
            freq = randint(0, 24)
            lat = randint(0, 200)
            lp = randint(0, 24)
            inf = randint(0, 5)
            skill = randint(0, 100)
            writer.writerow([name, freq, lat, lp, inf, skill])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('rows', type=int, help='Number of rows')
    args = parser.parse_args()
    generate(args.rows)

if __name__ == '__main__':
    main()