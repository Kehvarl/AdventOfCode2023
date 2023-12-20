from collections import defaultdict, deque
from math import lcm
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

rx_c = ""
for name in machines:
    t, destinations, states = machines[name]
    if t == '%':
        machines[name][2][True] = False
    if "rx" in destinations:
        rx_c = name
    for d in destinations:
        if d in machines:
            if machines[d][0] == '&':
                machines[d][2][name] = False


rx_conj_presses = {}

def pulse(press = 0):
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
                    if out is False and d == 'rx':
                        print(press)
                    queue.append((d, name, out))
                else:
                    pulses[out] += 1

        for s in machines[rx_c][2]:
            if machines[rx_c][2][s] is True and s not in rx_conj_presses:
                rx_conj_presses[s] = press

    return pulses


out = {True: 0, False: 0}
for i in range(1000):
    t = pulse(i)
    #print(t)
    out[True] += t[True]
    out[False] += t[False]
print(out, out[True] * out[False])

i = 1000
while len(rx_conj_presses) < 4:
    i += 1
    pulse(i)
print(rx_conj_presses)
print(lcm(*rx_conj_presses.values()))