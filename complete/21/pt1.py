from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    #content = f.readlines()
    content = [x.strip() for x in f.readlines()]

grid = {}
start = None
for y, v1 in enumerate(content):
    for x, v2 in enumerate(v1):
        grid[(x, y)] = v2
        if v2 == 'S':
            start = (x, y)


steps = 64
neighbors = [(1,0), (-1, 0), (0, 1), (0, -1)]
visited = defaultdict(set)
visited[0].add(start)
for s in range(steps):
    for point in visited[s]:
        x, y = point
        for n in neighbors:
            dx, dy = n
            ix, iy = x+dx, y+dy
            # print(x, dx, y, dy, ix, iy, grid.get((ix, iy), None))
            if grid.get((ix, iy), None) in['.', 'S']:
                visited[s+1].add((ix, iy))

print(len(visited.get(len(visited)-1)))

