from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as f:
    # content = f.readlines()
    content = [x.strip() for x in f.readlines()]

machines = {}
for v1 in content:
    machine, destinations = v1.split(' -> ')
    if machine == 'broadcaster':
        t = 'b'
        name = machine
    else:
        t = machine[0]
        name = machine[1:]
    destinations = [d.strip() for d in destinations.split(',')]
    machines[name] = [t, destinations, {}]

for name in machines:
    t, destinations, states = machines[name]
    if t == '%':
        machines[name][2][True] = False
    for d in destinations:
        if d in machines:
            if machines[d][0] == '&':
                machines[d][2][name] = False

def pulse():
    pulses = {True: 0, False: 0}
    queue = deque()
    queue.append(('broadcaster', 'button', False))
    while len(queue) > 0:
        name, source, message = queue.popleft()
        pulses[message] += 1
        t, destinations, states = machines[name]
        out = None
        if t == '%' and message is False:
            machines[name][2][True] = not machines[name][2][True]
            out = machines[name][2][True]
        elif t == '&':
            machines[name][2][source] = message
            if len(machines[name][2]) == 1:
                out = not message
            else:
                out = False
                for i in machines[name][2]:
                    if not machines[name][2][i]:
                        out = True
        elif t == 'b':
            out = message

        if out in [True, False]:
            #print(name, source, message, machines[name][2], out, destinations)
            for d in destinations:
                if d in machines:
                    queue.append((d, name, out))
                else:
                    pulses[out] += 1


    return pulses

out = {True: 0, False: 0}
for i in range(1000):
    t = pulse()
    #print(t)
    out[True] += t[True]
    out[False] += t[False]
print(out, out[True] * out[False])
