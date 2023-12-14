import functools
from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    #content = f.readlines()
    content = [x.strip() for x in f.readlines()]

grid = []
w = len(content[0])
h = len(content)
for y, v1 in enumerate(content):
    line = []
    for x, v2 in enumerate(v1):
        line.append(v2)
    grid.append(line)


def roll_north(grid, h, w):
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 'O':
                grid[y][x] = "."
                pos = (x, y)
                for d in range(1, y+1):
                    iy = y-d
                    if iy >= 0 and grid[iy][x] == ".":
                        pos = (x, iy)
                    else:
                        break
                grid[pos[1]][pos[0]] = 'O'
    return grid


def roll_south(grid, h, w):
    for y in range(h-1, -1, -1):
        for x in range(w):
            if grid[y][x] == 'O':
                grid[y][x] = "."
                pos = (x, y)
                for d in range(1, h-y+1):
                    iy = y+d
                    if iy < h and grid[iy][x] == ".":
                        pos = (x, iy)
                    else:
                        break
                grid[pos[1]][pos[0]] = 'O'
    return grid


def roll_east(grid, h, w):
    for y in range(h):
        for x in range(w-1, -1, -1):
            if grid[y][x] == 'O':
                grid[y][x] = "."
                pos = (x, y)
                for d in range(1, w-x+1):
                    ix = x+d
                    if ix < w and grid[y][ix] == ".":
                        pos = (ix, y)
                    else:
                        break
                grid[pos[1]][pos[0]] = 'O'
    return grid


def roll_west(grid, h, w):
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 'O':
                grid[y][x] = "."
                pos = (x, y)
                for d in range(1, x+1):
                    ix = x-d
                    if ix >= 0 and grid[y][ix] == ".":
                        pos = (ix, y)
                    else:
                        break
                grid[pos[1]][pos[0]] = 'O'
    return grid


seen = []
target = 0
while True:
    s = hash(tuple([''.join(l) for l in grid]))

    if not target and s in seen:
        start = seen.index(s)
        length = len(seen) - start
        target = (1000000000 - start) % length + start + length

    if len(seen) == target and target:
        break

    seen.append(s)
    grid = roll_north(grid, h, w)
    grid = roll_west(grid, h, w)
    grid = roll_south(grid, h, w)
    grid = roll_east(grid, h, w)

ans = 0
for y in range(h):
    line = ""
    for x in range(w):
        line += grid[y][x]
        if grid[y][x] == 'O':
            ans += h-y
    print(line)

print(ans)
