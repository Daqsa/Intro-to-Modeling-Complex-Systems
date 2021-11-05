from pylab import *
import networkx as nx

# graph is directed since transition is one-way 
g = nx.DiGraph()

"""
difference equation is x_t = x_{t-1}x_{t-2} (mod 6)
vertices u and v are connected iff u updates to v
each vertex u is characterized as the pair (x_{t-1}, x_{t-2})
"""
for x in range(6):
    for y in range(6):
        g.add_edge((x, y), (x * y % 6, x))

# make a list of vertices of components in g
ccs = [cc for cc in nx.connected_components(g.to_undirected())]

# visualize as closely as a square
n = len(ccs)
w = int(ceil(sqrt(n)))
h = int(ceil(n / w))
figure(figsize=(12,8), dpi=80)
for i in range(n):
    subplot(h, w, i + 1)
    # induce a subgraph from the generating vertices of the components
    nx.draw(nx.subgraph(g, ccs[i]), with_labels = True)

show()
