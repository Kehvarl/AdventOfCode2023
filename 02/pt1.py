from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

max_color = {'red': 12,
       'green': 13,
       'blue': 14}

valid_games = 0

games = {}
for v1 in content:
    valid = True
    g, rest = v1.strip().split(":")
    g = g[5:]
    games[g] = []
    rest = rest.split(";")
    for draw in rest:
        round = {}
        results = draw.split(",")
        for cubes in results:
            count, color = cubes.strip().split(" ")
            round[color] = int(count)
            if int(count) > max_color[color]:
                valid = False
        games[g].append(round)
    if valid:
        valid_games += int(g)

print(valid_games)



