# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:30:19 2018

@author: tancr
"""



#%%

#1. 2.5 points. In a graphs module, implement a directed graph data
#structure using classes. Modify the find_path function for so it works
#on instances of your class.
#2. 2.5 points. In a weighted module, implement a weighted directed
#graph data structure using classes. Modify the cheapest path function
#so it works on them.
#3. 2.5 points. Create tests for all the graph functions we have seen so
#far:
#• find_path
#• find_all_paths
#• find_path (weighted)
#• find_all_paths (weighted)
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




#1. 2.5 points. In a graphs module, implement a directed graph data
#structure using classes. Modify the find_path function for so it works
#on instances of your class.

class Node:
    def __init__(self, node, edges):
        self.node = node
        self.edges = edges
        
        
    def add_edges(self,x):
        self.edges.append(x)
        
        
        
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
                new_path = self.find_path( conn, end, path)
                
                if new_path is not None: 
                    return new_path
                
                
        return None




a = Node("a", [])
b = Node("b", [])
c = Node("c", [])
d = Node("d", [])
a.add_edges(b)
a.add_edges(c)
b.add_edges(d)
c.add_edges(d)


nn = Graph([a,b,c,d])


#%%

#2. 2.5 points. In a weighted module, implement a weighted directed
#graph data structure using classes. Modify the cheapest path function
#so it works on them.

#graph = {
#        "a":[{"node":"b", "weight": 5},{"node":"c","weight":2}],
#        "b":{"node":"d","weight":9},
#        "c":{"node":"d","weight":1},
#        "d":{},
#        "e":{}        
#}
class Node:
    def __init__(self, node, edges):
        self.node = node
        self.edges = edges

        
    def add_edges(self,x, y):
        dic = {"node":x,"weight":y}
        self.edges.append(dict(dic))
        

#down vote
#Also with dict
#
#a = []
#b = {1:'one'}
#
#a.append(dict(b))
#print a
#b[1]='iuqsdgf'
#print a
#        
        
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















