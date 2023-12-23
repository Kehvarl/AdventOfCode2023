from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    #content = [int(x) for x in f.readlines()]

grid = {}
start = None
goal = None
for y, v1 in enumerate(content):
    for x, v2 in enumerate(v1):
        if y == 0 and v2 == '.':
            start = (x, y)
        if y == len(content) - 1 and v2 == '.':
            goal = (x, y)
        grid[(x, y)] = v2


neighbors = {
    '.': [(1, 0), (-1, 0), (0, 1), (0, -1)],
    '^': [(0, -1)],
    'v': [(0, 1)],
    '>': [(1, 0)],
    '<': [(-1, 0)],
}

max_distance = 0
longest = []
queue = deque()
queue.append((start, [start]))
while len(queue) > 0:
    node, path = queue.popleft()
    #print(path, len(path))
    x, y = node
    for dx, dy in neighbors['.']:
        ix, iy = x + dx, y + dy
        if (ix, iy) == goal:
            max_distance = max(max_distance, len(path + [(ix, iy)]))
            longest = path + [(ix, iy)]
            print(max_distance)
        elif (ix, iy) not in path and (ix, iy) in grid and grid[(ix, iy)] != '#':
            queue.append(((ix, iy), path + [(ix, iy)]))
print(max_distance - 1)

