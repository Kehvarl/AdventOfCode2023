from collections import defaultdict, deque
from heapq import heappush, heappop
from pprint import pprint

with open("test.txt") as f:
    #content = f.readlines()
    content = [x.strip() for x in f.readlines()]

width = len(content[0])
height = len(content)
grid = {}
for y, v1 in enumerate(content):
    for x, v2 in enumerate(v1):
        grid[(x, y)] = int(v2)


allowed_turns = {
    (0, 0): [(0, 1), (0, -1), (1, 0), (-1, 0)],
    (0, 1): [(0, 1), (1, 0), (-1, 0)],
    (0, -1): [(0, -1), (1, 0), (-1, 0)],
    (1, 0): [(1, 0), (0, 1), (0, -1)],
    (-1, 0): [(-1, 0), (0, 1), (0, -1)],
}


start = (0, 0, 0, 0, -1)
dist = {}
bfs_queue = [(0, start)]
goal = (width-1, height-1)
while bfs_queue:
    (cost, (x, y, vx, vy, last_turn)) = heappop(bfs_queue)

    if (x, y, vx, vy) in dist:
        continue
    dist[(x, y, vx, vy)] = cost
    for option in allowed_turns[(vx, vy)]:
        turn = (1 if option != (vx, vy) else last_turn + 1)
        isvalid = (turn <= 3)
        ivx, ivy = option
        if 0 <= x + ivx < width and 0 <= y + ivy < height and isvalid:
            ihl = grid[(x + ivx, y + ivy)]
            heappush(bfs_queue, (cost + ihl, (x + ivx, y + ivy, ivy, ivx, turn)))

ans = 999999
print(grid)
for (x, y, vx, vy), cost in dist.items():
    #print((x, y, vx, vy), cost)
    if (x, y) == goal:
        ans = min(ans, cost)
print(ans)

