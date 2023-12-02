from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

sum = 0
for v1 in content:
    l = []
    for v2 in v1:
        if v2.isnumeric():
            l.append((v2))

#    print(l[0], l[-1])
    sum += int(str(l[0]) + str(l[-1]))

print(sum)
