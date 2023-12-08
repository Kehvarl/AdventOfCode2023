from collections import defaultdict
from pprint import pprint
import functools

with open("input.txt") as f:
    content = f.readlines()
    # content = [int(x) for x in f.readlines()]

card_labels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def compare(hand1, hand2):
    if hand1[0] < hand2[0]:
        return -1
    elif hand1[0] > hand2[0]:
        return 1
    else:
        for i, c in enumerate(hand1[1]):
            if card_labels.index(c) < card_labels.index(hand2[1][i]):
                return 1
            elif card_labels.index(c) > card_labels.index(hand2[1][i]):
                return -1
        return 0


hands = []
for v1 in content:
    hand, bid = v1.split()
    bid = int(bid)
    counts = {}
    for card in hand:
        counts[card] = hand.count(card)
    most = 0
    second = 0
    for c in counts:
        if counts[c] >= most:
            second = most
            most = counts[c]
        elif counts[c] >= second:
            second = counts[c]

    if most == 5:
        hand_type = 6
    elif most == 4:
        hand_type = 5
    elif most == 3:
        if second == 2:
            hand_type = 4
        else:
            hand_type = 3
    elif most == 2:
        if second == 2:
            hand_type = 2
        else:
            hand_type = 1
    else:
        hand_type = 0

    hands.append([hand_type, hand, bid])

hands = sorted(hands, key=functools.cmp_to_key(compare), reverse=True)


#pprint(hands)

win = 0
rank = len(hands)
for hand in hands:
    win += rank * hand[2]
    print(rank, hand[0], hand[1], hand[2], rank * hand[2])
    rank -= 1
print(win)