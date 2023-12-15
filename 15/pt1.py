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

hashes = {}
total = 0
for v1 in content[0].split(','):
    c = 0
    for v2 in v1:
        c = hash(v2, c)
    hashes[v1] = c
    total += c

print(hashes)
print(total)