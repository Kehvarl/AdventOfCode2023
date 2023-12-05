import itertools
from collections import defaultdict
from pprint import pprint
from itertools import count

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

_, rest = content[0].split(":")
temp_seeds = rest.split()
seeds = []
for i in range(0, len(temp_seeds), 2):
    seeds.append((temp_seeds[i], temp_seeds[i+1]))

maps = {}

read_map = True
map_type = ""
for v1 in content[2:]:
    if v1 == "\n":
        read_map = True
        continue

    if read_map:
        map_type = v1.strip()[:-5]
        maps[map_type] = []
        read_map = False
        continue

    dest, source, count = v1.strip().split()
    dest = int(dest)
    source = int(source)
    count = int(count)
    maps[map_type].append([dest, source, count])

lowest_location = None


def get_from_map(map_name, value):
    working_map = maps[map_name]
    for entry in working_map:
        dest, source, count = entry
        if dest <= value < dest + count:
            return source + (value - dest)
    return value


def valid_seed(seed, seeds):
    for temp_seed in seeds:
        start, count = temp_seed
        start = int(start)
        count = int(count)
        if start <= seed < start + count:
            print(seed, val)
            return True
    return False


for val in itertools.count():
    humidity = get_from_map('humidity-to-location', val)
    temperature = get_from_map('temperature-to-humidity', humidity)
    light = get_from_map('light-to-temperature', temperature)
    water = get_from_map('water-to-light', light)
    fertilizer = get_from_map('fertilizer-to-water', water)
    soil = get_from_map('soil-to-fertilizer', fertilizer)
    seed = get_from_map('seed-to-soil', soil)
    if valid_seed(seed, seeds):
        break

