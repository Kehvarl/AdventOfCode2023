from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    # content = f.readlines()
    content = [x.strip() for x in f.readlines()]

directions = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
    '3': (0, -1),
    '1': (0, 1),
    '2': (-1, 0),
    '0': (1, 0),
}


def add_direction(point, dir):
    return (point[0] + dir[0], point[1] + dir[1])


#pit = {(0, 0): '(#000000)'}
pit = [(0, 0)]

min_x = 0
max_x = 0
min_y = 0
max_y = 0

current = (0, 0)
for v1 in content:
    _, _, color = v1.split()
    distance = int(color[2:7], 16)
    direction = color[-2]
    for d in range(int(distance)):
        current = add_direction(current, directions[direction])
        #pit[current] = color
        pit.append(current)
        min_x = min(min_x, current[0])
        max_x = max(max_x, current[0])
        min_y = min(min_y, current[1])
        max_y = max(max_y, current[1])

# Shoelace formula
area = 0
for i in range(len(pit) - 1):
    x1, y1 = pit[i]
    x2, y2 = pit[i + 1]
    area += x1 * y2 - x2 * y1

# Pick's theorem
perimeter = len(pit)
interior_area = abs(area) // 2 - perimeter // 2
print(interior_area + perimeter)
