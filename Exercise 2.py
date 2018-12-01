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

        
    def add_edges(self,x, y):
        dic = {"node":x,"weight":y}
        self.edges.append(dict(dic))
        
   
class Graph: 
    def __init__(self, lst):
        self.lst = lst
        
    def get_edges(self, node):
        return node.edges



    def find_path_weighted(self, start, end, path = [], weight = 0):
        
        
        path = path + [{"node":start,"weight":weight}]    
        
        if start == end:
            return path
        
        if start not in self.lst:
            return None
        
        for conn in self.get_edges:
            
            if conn not in path:
                new_path = self.find_path_weighted(
                        self.lst,
                        conn["node"],
                        end,
                        path,
                        conn["weight"]
                        )
                
                if new_path is not None: 
                    return new_path
                
                
        return None






a = Node("a", [])
b = Node("b", [])
c = Node("c", [])
d = Node("d", [])
a.add_edges(b, 9)
a.add_edges(c, 2)
b.add_edges(d, 6)
c.add_edges(d, 6)


