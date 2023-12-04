from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

wins = []
copies = defaultdict(int)
row = 0
while row < len(content):
    card, rest = content[row].strip().split(': ')
    card = card[5:]
    #print(card)
    rest = rest.replace("  ", " ")
    win, game = rest.split(" | ")
    win = win.split(" ")
    game = game.split(" ")
    matches = 0
    row += 1

    for num in game:
        if num in win:
            matches += 1

    if matches > 0:
        for i in range(matches):
            card = int(card)
            # print(f'adding card {card+i+1}')
            content.append(content[card+i])

print(len(content))
print(content)
