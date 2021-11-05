from pylab import *
import networkx as nx

# graph is directed since transition is one-way 
g = nx.DiGraph()

"""
difference equation is x_t = x_{t-1}^{x_{t-1}} (mod 100) 
vertices u and v are connected iff u updates to v
each vertex u is characterized as the state
"""

# possible states are 0..99
for x in range(100):
    g.add_edge(x, (x ** x) % 100)

# make a list of vertices of components in g
ccs = [cc for cc in nx.connected_components(g.to_undirected())]

# visualize as closely as a square
n = len(ccs)
halfn = int(round(n / 2))
w = int(ceil(sqrt(halfn)))
h = int(ceil(halfn / w))

# plot one two windows since there's too many graphs
figure(figsize=(12,8), dpi=80)
for i in range(halfn):
    subplot(h, w, i + 1)
    # induce a subgraph from the generating vertices of the components
    nx.draw(nx.subgraph(g, ccs[i]), with_labels = True)

figure(figsize=(12,8), dpi=80)
otherHalf = n - halfn
w = int(ceil(sqrt(otherHalf)))
h = int(ceil(otherHalf / w))
for i in range(otherHalf):
    subplot(h, w, i + 1)
    # induce a subgraph from the generating vertices of the components
    nx.draw(nx.subgraph(g, ccs[halfn+i]), with_labels = True)


show()
