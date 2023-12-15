from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    #content = f.readlines()
    content = [x.strip() for x in f.readlines()]


def hash(char, current=0):
    ascii = ord(char)
    current += ascii
    current *= 17
    return current % 256


boxes = defaultdict(list)
for v1 in content[0].split(','):
    c = 0
    focal = False
    fl = ''
    label = ''
    for v2 in v1:
        if focal:
            fl += v2
        else:
            if v2 == '-':
                for b in boxes[c]:
                    l, f = b
                    if l == label:
                        boxes[c].remove(b)
            elif v2 == '=':
                focal = True
            else:
                label += v2
                c = hash(v2, c)
    if focal:
        fl = int(fl)
        if c not in boxes:
            boxes[c] = []

        for i, b in enumerate(boxes[c]):
            l, f = b
            if l == label:
                boxes[c][i] = (label, fl)
                break
        else:
            boxes[c].append((label, fl))

#pprint(boxes)
power = 0
for id, box in enumerate(boxes):
    for slot, lens in enumerate(boxes[box]):
        label, focal = lens
        val = (box +1) * (slot + 1) * focal
        power += val
        print(id, box, slot, focal, val, power)

print(power)