from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

wins = []
for row in content:
    card, rest = row.strip().split(': ')
    card = card[5:-1]
    rest = rest.replace("  ", " ")
    win, game = rest.split(" | ")
    win = win.split(" ")
    game = game.split(" ")
    score = 0
    winning = []
    # print(card)
    # print(win)
    # print(game)
    for num in game:
        if num in win:
            winning.append(num)
            if score == 0:
                score = 1
            else:
                score = score * 2
    # print(winning)
    # print(card, score)
    wins.append(score)

print(sum(wins))
