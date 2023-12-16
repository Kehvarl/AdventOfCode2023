from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    # content = f.read()
    content = [x.strip() for x in f.readlines()]

width = len(content[0])
height = len(content)
grid = {}
for y, v1 in enumerate(content):
    v1.replace("\\", "\\\\")
    width = max(width, len(v1))
    # print(v1)
    for x, v2 in enumerate(v1):
        # print(x, y, v2)
        grid[(x, y)] = v2


mirrors = {
    '\\': {(1, 0): (0, 1),
           (-1, 0): (0, -1),
           (0, 1): (1, 0),
           (0, -1): (-1, 0)},
    '/': {(1, 0): (0, -1),
          (-1, 0): (0, 1),
          (0, 1): (-1, 0),
          (0, -1): (1, 0)}
}

splits = {
    '|': {(1, 0): [(0, 1), (0, -1)],
          (-1, 0): [(0, 1), (0, -1)],
          (0, 1): [(0, 1)],
          (0, -1): [(0, -1)]},
    '-': {(1, 0): [(1, 0)],
          (-1, 0): [(-1, 0)],
          (0, 1): [(1, 0), (-1, 0)],
          (0, -1): [(1, 0), (-1, 0)]}
}

start = (0, 0, 1, 0)
bfs_q = deque()
bfs_q.append(start)
seen = set()
energized = set()

while len(bfs_q) > 0:
    curcell = bfs_q.popleft()
    if curcell in seen:
        continue
    seen.add(curcell)

    x, y, vx, vy = curcell
    seen.add(curcell)
    energized.add((x, y))
    if grid[(x, y)] in splits:
        print(x, y, grid[(x, y)], splits[grid[(x, y)]][(vx, vy)])
        for nxt in splits[grid[(x, y)]][(vx, vy)]:
            ivx, ivy = nxt
            if 0 <= x + ivx < width and 0 <= y + ivy < height:
                bfs_q.append((x + ivx, y + ivy, ivx, ivy))
    elif grid[(x, y)] in mirrors:
        print(x, y, grid[(x, y)], mirrors[grid[(x, y)]][(vx, vy)])
        ivx, ivy = mirrors[grid[(x, y)]][(vx, vy)]
        if 0 <= x + ivx < width and 0 <= y + ivy < height:
            bfs_q.append((x + ivx, y + ivy, ivx, ivy))
    else:
        if 0 <= x + vx < width and 0 <= y + vy < height:
            bfs_q.append((x + vx, y + vy, vx, vy))

for y in range(height):
    line = ""
    for x in range(width):
        if (x, y) in energized and grid[(x, y)] == '.':
            line += '#'
        else:
            line += grid[(x, y)]
    print(line)


print(len(energized))
