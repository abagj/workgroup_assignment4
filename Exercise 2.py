# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 16:15:34 2018

@author: tancr
"""

#%%

#2. 2.5 points. In a weighted module, implement a weighted directed
#graph data structure using classes. Modify the cheapest path function
#so it works on them.


class Node:
    def __init__(self, node, edges):
        self.node = node
        self.edges = edges

        
    def add_edges(self,node, weight):
        self.edges.append({"node":node, "weight":weight})   

        
   
class Graph: 
    def __init__(self, lst):
        self.lst = lst
        
    def get_edges(self, node):
        return node.edges


    def find_all_paths(self,start,end,path = [],weight = 0):
            path = path + [{"node":start, "weight":weight}]
            if start == end:
                return [path]
            if start not in self.nodes:
                return []
            paths = []
            for conn in self.get_edges(start):
                if conn not in path:
                    new_paths = self.find_all_paths(conn["node"], end,path,conn["weight"])
                    for newpath in new_paths:
                        paths.append(newpath)
            return paths
    
    def cheapest_path(self,start,end):
            all_paths = self.find_all_paths(start, end)
            cheapest = None
            for path in all_paths:
                cost = 0
                for step in path:
                    cost += step["weight"]
                if cheapest is None or cost < cheapest:
                    cheapest = cost
            return cheapest
      
    

a = Node("a", [])
b = Node("b", [])
c = Node("c",[])
d = Node("d",[])
a.add_edge(b,6)
a.add_edge(c,2)
b.add_edge(d,3)
c.add_edge(d,8)

graph = Graph([a,b,c,d])


