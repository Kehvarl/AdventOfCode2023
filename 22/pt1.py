from collections import defaultdict
from pprint import pprint

with open("test.txt") as f:
    #content = f.readlines()
    content = [x.strip() for x in f.readlines()]

bricks = {}
rx = [99999, -99999]
ry = [99999, -99999]
rz = [99999, -99999]

for i, v1 in enumerate(content):
    a, b = v1.split('~')
    a = [int(x) for x in a.split(',')]
    b = [int(x) for x in b.split(',')]
    lz = min(a[2], b[2])
    hz = max(a[2], b[2])
    rz[0] = min(rz[0], lz)
    rz[1] = max(rz[1], hz)
    ry[0] = min(ry[0], a[1], b[1])
    ry[1] = max(ry[1], a[1], b[1])
    rx[0] = min(rx[0], a[0], b[0])
    rx[1] = max(rx[1], a[0], b[0])
    for z in range(lz, hz+1):
        if z not in bricks:
            bricks[z] = {}
        bricks[z][(a[0], a[1], b[0], b[2])] = i


supported = {}
for z in range(rz[1], rz[0], -1):
    if z not in bricks:
        continue
    for brick in bricks[z]:
        for y in  range(brick[2], brick[3]):
            for x in range(brick[0], brick[1]):
                if bricks[z][(x, y)] != bricks[z][brick]



