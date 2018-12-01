# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:30:19 2018

@author: tancr
"""



#%%

#1. 2.5 points. In a graphs module, implement a directed graph data
#structure using classes. Modify the find_path function for so it works
#on instances of your class.

class Node:
    def __init__(self, name, edges):
        self.name = name
        self.edges = edges
        
        
    def add_edges(self,node):
        self.edges.append(node)
        
        
        
class Graph: 
    def __init__(self, lst):
        self.lst = lst
        
    def get_edges(self, node):
        return node.edges
    
    
    def find_path(self, start, end, path = []):
        path = path + [start]    
        if start == end:
            return path
        if start not in self.lst:
            return None
        for conn in self.get_edges(start): 
            if conn not in path:
                new_path = self.find_path(conn, end, path)
                if new_path is not None: 
                    return new_path
        return None
    
    def find_path_names(self,start,end):
        lst = self.find_path(start,end)
        names = []
        for i in lst:
            names.append(i.name)
        return names




a = Node("a", [])
b = Node("b", [])
c = Node("c", [])
d = Node("d", [])
a.add_edges(b)
a.add_edges(c)
b.add_edges(d)
c.add_edges(d)


graph = Graph([a,b,c,d])

























