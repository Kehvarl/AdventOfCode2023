from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]


symbols = []
for iv1, v1 in enumerate(content):
    for iv2, v2 in enumerate(v1.strip()):
        if not v2.isnumeric() and not v2 == '.':
            symbols.append([iv1, iv2])

nums = []
used = set()
for pos in symbols:
    y, x = pos
    for ymod in [-1, 0, 1]:
        for xmod in [-1, 0, 1]:
            #if x == y == 0:
            #    continue
            if (y+ymod, x+xmod) in used:
                continue
            row = content[y+ymod]

            if row[x+xmod].isnumeric():
                valid_x = x+xmod
                search = 0
                while row[valid_x+search].isnumeric():
                    used.add((y+ymod, valid_x+search))
                    search -= 1

                start = valid_x + search + 1
                search = 1
                while row[start+search].isnumeric():
                    used.add((y + ymod, start+search))
                    search += 1

                num = row[start:start+search]
                nums.append(int(num))

print(nums)
print(sum(nums))

