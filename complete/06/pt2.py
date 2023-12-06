from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

_, times = content[0].split(':')
times = times.split()
_, dist = content[1].split(':')
dist = dist.split()

time = ""
for ch in content[0]:
    if ch.isnumeric():
        time += ch
time = int(time)

dist = ""
for ch in content[1]:
    if ch.isnumeric():
        dist += ch
dist = int(dist)


spd = 0
delta_spd = 1
can_beat = 0
for ms in range(0, time+1):
    total = (time-ms) * ms
    #print(time, dist, spd, total)
    if total > dist:
        can_beat += 1


print(time)
print(dist)
print(can_beat)