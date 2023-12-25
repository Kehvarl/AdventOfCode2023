from collections import defaultdict, deque
from pprint import pprint
import networkx as nx

with open("input.txt") as f:
    content = [x.strip() for x in f.readlines()]
    # content = [int(x) for x in f.readlines()]

graph = defaultdict(set)
components = set()
for v1 in content:
    component, children = v1.split(': ')
    children = children.split(' ')
    components.add(component)
    for c in children:
        components.add(c)
        graph[component].add(c)
        graph[c].add(component)


nx_graph = nx.DiGraph()
for component in graph:
    for child in graph[component]:
        nx_graph.add_edge(component, child, capacity=1.0)
        nx_graph.add_edge(child, component, capacity=1.0)


component = components.pop()
for y in graph:
    joins, (set_a, set_b) = nx.minimum_cut(nx_graph, component, y)
    if joins == 3:
        print(len(set_a) * len(set_b))
        break
