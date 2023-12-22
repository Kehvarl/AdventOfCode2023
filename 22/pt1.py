from collections import defaultdict
from pprint import pprint

with open("test.txt") as f:
    #content = f.readlines()
    content = [x.strip() for x in f.readlines()]

bricks = []

for i, v1 in enumerate(content):
    a, b = v1.split('~')
    a = [int(x) for x in a.split(',')]
    b = [int(x) for x in b.split(',')]
    bricks.append(((a[0], a[1], a[2]), (b[0], b[1], b[2])))


