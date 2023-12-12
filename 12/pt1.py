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
            rows_b.append(v1[index:].strip().split(','))
            break


# print(rows_a)
# print(rows_b)


def count_row(row):
    count = []
    length = 0
    for c in row:
        if c == '#':
            length += 1
        elif length > 0:
            count.append(str(length))
            length = 0
    if length > 0:
        count.append(str(length))
    return count


def get_bin (x, n):
    return format(x, 'b').zfill(n)

rows_valid = []

for r, row in enumerate(rows_a):
    unknown = set()
    for i in range(len(row)):
        if row[i] == '?':
            unknown.add(i)
    temp = row
    valid = 0
    for b in range(2 ** (len(unknown))):
        b_num = get_bin(b, len(unknown))
        for i, v in enumerate(unknown):
            if b_num[i] == '0':
                temp[v] = '.'
            else:
                temp[v] = '#'
        if count_row(temp) == rows_b[r]:
            # print(b_num, temp, count_row(temp), rows_b[r])
            valid += 1
    rows_valid.append(valid)

print(rows_valid)
print(sum(rows_valid))