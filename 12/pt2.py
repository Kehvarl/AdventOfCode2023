from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    # content = [int(x) for x in f.readlines()]

rows_a = []
rows_b = []

for r, v1 in enumerate(content):
    rows_a.append([])
    for index, v2 in enumerate(v1):
        if v2 in ['#', '.', '?']:
            rows_a[r].append(v2)
        if v2 == " ":
            rows_b.append([int(x) for x in v1[index:].strip().split(',')])
            break

new = []
for r in rows_a:
    new.append((r+['?'])*4 + r)
rows_a = new

new = []
for r in rows_b:
    new.append(r*5)
rows_b = new


def count_row(memo, row, counts, pos, current_count, countpos):
    key = (pos, current_count, countpos)

    if key in memo:
        return memo[key]

    if pos == len(row):
        if len(counts) == countpos:
            ret = 1
        else:
            ret = 0
    elif row[pos] == '#':
        ret = count_row(memo, row, counts, pos + 1, current_count + 1, countpos)
    elif row[pos] == '.' or countpos == len(counts):
        if countpos < len(counts) and current_count == counts[countpos]:
            ret = count_row(memo, row, counts, pos + 1, 0, countpos + 1)
        elif current_count == 0:
            ret = count_row(memo, row, counts, pos + 1, 0, countpos)
        else:
            ret = 0
    else:
        broken_cnt = count_row(memo, row, counts, pos + 1, current_count + 1, countpos)
        good_cnt = 0
        if current_count == counts[countpos]:
            good_cnt = count_row(memo, row, counts, pos + 1, 0, countpos + 1)
        elif current_count == 0:
            good_cnt = count_row(memo, row, counts, pos + 1, 0, countpos)
        ret = broken_cnt + good_cnt
    memo[key] = ret

    return ret


res = 0
for r, row in enumerate(rows_b):
    res += count_row({}, ''.join(rows_a[r]) + '.', row, 0, 0, 0)
print(res)
