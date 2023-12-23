from collections import defaultdict

with open("input.txt") as f:
    # content = f.readlines()
    content = [x.strip() for x in f.readlines()]
bricks = []

for i, v1 in enumerate(content):
    a, b = v1.split('~')
    a = [int(x) for x in a.split(',')]
    b = [int(x) for x in b.split(',')]
    bricks.append(((a[0], a[1], a[2]), (b[0], b[1], b[2])))

bricks = sorted(bricks, key=lambda brick: brick[0][2])  # sort by starting Z


def drop(stack, skip=None):
    peaks = defaultdict(int)
    falls = 0

    for i, brick in enumerate(stack):
        a, b = brick
        ax, ay, az = a
        bx, by, bz = b
        if i == skip:
            continue
        area = []
        for x in range(ax, bx + 1):
            for y in range(ay, by + 1):
                area.append((x, y))

        max_a = 0
        for a in area:
            max_a = max(max_a, peaks[a])

        for a in area:
            peaks[a] = max_a + 1 + bz - az

        stack[i] = ((ax, ay, max_a), (bx, by, max_a + bz - az))
        falls += max_a < az

    return falls


drop(bricks)  # Drop all bricks as far as they'll fall

stable = 0
falling = 0
for brick in range(len(bricks)):
    f = drop(bricks.copy(), skip=brick)  # Use a copy so we only test each brick, not all bricks
    if f == 0:  # No bricks fall if we remove this brick
        stable += 1
    falling += f

print(stable, falling)
