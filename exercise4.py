#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:32:01 2018

@author: zinebmezzour
"""
#%% 4.1 Find NetworkX’ functions that do the following:
#• see if there’s a path between two nodes
#• find the shortest path between two nodes

import networkx as nx
import matplotlib.pyplot as plt

#Example Graph Structures
#graph = {
#        "a":["b","c"],
#        "b": ["d"],
#        "c":["d"],
#        "d" : ["e"],
#        "e" :[],
#        "f":[]
#}
#
#w_graph = {
#        "a":[{"node":"b","weight":1},{"node":"c","weight":2}],
#        "b": [{"node":"d","weight":3}],
#        "c":[{"node":"d","weight":10}],
#        "d" : [{"node":"e","weight":3}],
#        "e" :[],
#        "f":[]
#}

# Create Directed Graph with NetworkX according to example structure
graph = nx.DiGraph()
graph.add_edge('a', 'b', weight=1)
graph.add_edge('a', 'c', weight=2)
graph.add_edge('b', 'd', weight=100)
graph.add_edge('c', 'd', weight=10)
graph.add_node('e')
graph.add_edge('d', 'e', weight=3)
graph.add_node('f')

#Network X Functions:

nx.has_path(graph, 'a', 'd') #returns True
nx.has_path(graph, 'a', 'f') #returns False
nx.dijkstra_path_length(graph,"a","d") #returns Minimum path length
nx.shortest_path(graph, 'a', 'd', weight='weight') # returns shortest path



#%% 
#Draw graph with Network X & Matplotlib

plt.subplot(122)
nx.draw_shell(graph, with_labels=True, font_weight='bold')
plt.show()

#%%