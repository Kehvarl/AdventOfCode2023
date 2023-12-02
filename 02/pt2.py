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
    min_color = {'red': 0, 'green': 0, 'blue': 0}

    rest = rest.split(";")
    for draw in rest:
        results = draw.split(",")
        for cubes in results:
            count, color = cubes.strip().split(" ")
            if int(count) > min_color[color]:
                min_color[color] = int(count)
    print(min_color)
    games[g] = min_color['red'] * min_color['green'] * min_color['blue']

print(games)
print(sum(games.values()))

