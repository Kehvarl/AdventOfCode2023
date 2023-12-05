from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

_, rest = content[0].split(":")
seeds = rest.split()

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
        if source <= value < source + count:
            return dest + (value - source)
    return value


for seed in seeds:
    seed = int(seed)
    soil = get_from_map('seed-to-soil', seed)
    fertilizer = get_from_map('soil-to-fertilizer', soil)
    water = get_from_map('fertilizer-to-water', fertilizer)
    light = get_from_map('water-to-light', water)
    temperature = get_from_map('light-to-temperature', light)
    humidity = get_from_map('temperature-to-humidity', temperature)
    location = get_from_map('humidity-to-location', humidity)
    print(seed, soil, fertilizer, water, light, temperature, humidity, location)

    if lowest_location is None or location < lowest_location:
        lowest_location = location

print(lowest_location)






