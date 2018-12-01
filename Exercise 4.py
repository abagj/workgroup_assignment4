# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 16:16:43 2018

@author: tancr
"""

#%%

#4. 2.5 points. Investigate the NetworkX library. Create an instance of
#a digraph like the one we saw in class.
#graph = {
#"a": ["b", "c"],
#"b": ["d"],
#"c": ["d"],
#"d": ["e"],
#"e": [],
#"f": []
#}


import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from(
    [('A', 'B'), ('A', 'C'),('B', 'D'),('C', 'D'),('D', 'E'),('E', ''),
     ('F', '')])

val_map = {'A': 1.0,
           'D': 0.5714285714285714,
           'H': 0.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]

# Specify the edges you want here

edge_colours = ['black'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(G, pos)

nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()





