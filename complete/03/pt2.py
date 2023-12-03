from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]


symbols = []
gears = []
for iv1, v1 in enumerate(content):
    for iv2, v2 in enumerate(v1.strip()):
        if not v2.isnumeric() and not v2 == '.':
            symbols.append([iv1, iv2])
            if v2 == '*':
                gears.append([iv1, iv2])

nums = []
used = set()
for pos in gears:
    cur_gears = []
    y, x = pos
    for ymod in [-1, 0, 1]:
        for xmod in [-1, 0, 1]:

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
                cur_gears.append(int(num))
    if len(cur_gears) == 2:
        nums.append(cur_gears[0] * cur_gears[1])

print(nums)
print(sum(nums))