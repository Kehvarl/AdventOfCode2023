from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

_, times = content[0].split(':')
times = times.split()
_, dist = content[1].split(':')
dist = dist.split()

results = []
for idx, time in enumerate(times):
    d = int(dist[idx])
    time = int(time)
    spd = 0
    delta_spd = 1
    can_beat = 0
    for ms in range(0, time+1):
        total = (time-ms) * ms
        print(time, d, spd, total)
        if total > d:
            can_beat += 1
    results.append(can_beat)

print(times)
print(dist)
print(results)
prod = 1
for r in results:
    prod *= r
print(prod)