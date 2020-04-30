import random
import time
from os import system

def team_entry():
    number_of_players = int(input("Number of athletes: "))
    players = []

    while (len(players) < number_of_players):
        players.append([input("Player name: "), round(random.uniform(9,19), 2)])

    print("\n" * 50)
    print("And they're off!\n----------------")

    return players

def race(players):
    results = []
    for i in range (0, len(players) - 1):
        for j in range(0, len(players) - 1 - i):
             if (players[j][1] > players[j+1][1]):
                 players[j], players[j+1] = players[j+1], players[j]
    return players

def main():
    players = race(team_entry())
    for item in players:
        if item != players[0]:
            previous = players.index(item) - 1
            time.sleep(item[1] - players[previous][1])
        else:
            time.sleep(item[1])

        if (item[1] < 9.58):
            item[0] += " - World Record!"
        
        print(str(players.index(item)+1) + ". " + "Name: " + item[0] + "\n   Time: " + str(item[1]) + "s\n----------------")

    print ("Thanks for racing!")

main()
