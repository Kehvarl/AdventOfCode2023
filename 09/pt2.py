from collections import defaultdict
from pprint import pprint

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

values = []
for v1 in content:
    values.append([int(x) for x in v1.strip().split(" ")])


def determine_sequence(sequence_values):
    sequence = []
    for idx in range(len(sequence_values)-1):
        sequence.append(sequence_values[idx+1] - sequence_values[idx])
    return sequence

history = []
for sequence in values:
    seq_sets = [sequence]
    while True:
        new_sequence = determine_sequence(sequence)
        seq_sets.append(new_sequence)
        if all([v == 0 for v in new_sequence]):
            break
        sequence = new_sequence

    working_sets = list(reversed(seq_sets))
    for idx, set in enumerate(working_sets):
        val = set[0]
        if idx > 0:
            val -= working_sets[idx-1][0]
        set = [val] + set
        working_sets[idx] = set
        print(set)
        if idx == len(working_sets)-1:
            history.append(val)

print(history, sum(history))
