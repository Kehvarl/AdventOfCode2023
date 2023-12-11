from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]


tiles = {
    '.': [],
    '|': [(0, -1), (0, 1)],
    '-': [(-1, 0), (1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, 1), (-1, 0)],
    'F': [(0, 1), (1, 0)],
    'S': []
}


def can_connect(cell1, cell2):
    if not cell1[1]:
        return False
    cx, cy = cell1[0]
    cell1_path1, cell1_path2 = cell1[1]
    dx1, dy1 = cell1_path1
    dx2, dy2 = cell1_path2
    return (cx+dx1, cy+dy1) == cell2[0] or (cx+dx2, cy+dy2) == cell2[0]


def find_tile(connections):
    c1, c2 = connections
    for tile in tiles:
        if tiles[tile] == [c1, c2] or tiles[tile] == [c2, c1]:
            return tile


def get_lowest_neighbor_value(x, y, max_dist):
    lowest = max_dist
    f = usable_grid[(x, y)]
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        tx, ty = x + dx, y + dy
        t = usable_grid.get((tx, ty), None)
        if t and can_connect(t, f):
            lowest = min(lowest, t[2])
    return lowest


def print_grid(grid, height, width):
    for y in range(0, height):
        line = ""
        for x in range(0, width):
            if not grid[(x, y)][1]:
                line += '.'
            else:
                line += str(grid[(x, y)][2])
        print(line)


height = len(content)
width = len(content[0].strip())
max_dist = height * width
grid = {}
usable_grid = {}
start = None
for i1, v1 in enumerate(content):
    #line = []
    for i2, v2 in enumerate(v1.strip()):
        if v2 == "S":
            start = (i2, i1)
        cell = [(i2, i1), tiles[v2], max_dist, False, v2]
        #line.append(cell)
        grid[(i2, i1)] = cell

# Input S == '|'

s = grid[start]
valid = []
for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    dx, dy = neighbor
    x, y = s[0]
    ix = x + dx
    iy = y + dy
    if grid.get((ix, iy), None) and can_connect(grid[(ix, iy)], s):
        valid.append((dx, dy))
t = find_tile(valid)
grid[start][1] = tiles[t]
grid[start][2] = 0
grid[start][4] = t

bfs_q = deque()
bfs_q.append(grid[start])
ans = (0, grid[start])

while len(bfs_q) > 0:
    curcell = bfs_q.popleft()
    # print(curcell)
    x, y = curcell[0]
    grid[(x,y)][3] = True
    for nxt in curcell[1]:
        dx, dy = nxt
        ix = x + dx
        iy = y + dy
        if grid[(ix, iy)][2] == max_dist:
            grid[(ix, iy)][2] = grid[(x, y)][2] + 1
            ans = max(ans, (grid[(ix, iy)][2], grid[(ix, iy)]))
            bfs_q.append(grid[(ix, iy)])

print(ans)


for y in range(height):
    for x in range(width):
        if not grid[(x, y)][3]:
            grid[(x, y)][4] = '.'

inside = 0
for y in range(height-1):
    walls = 0
    for x in range(width-1):
        if grid[(x, y)][4] in ['|', 'L', 'J']: # Count is way too high if you include F and 7.
            walls += 1
        elif walls % 2 == 1 and grid[(x, y)][4] == '.':
            inside += 1

print(inside)




