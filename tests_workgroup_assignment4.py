#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 12:31:44 2018

@author: alemeneses
"""

#%%

# 3. 2.5 points. Create tests for all the graph functions we have seen so
# far:
# • find_path
# • find_all_paths
# • find_path (weighted)
# • find_all_paths (weighted)

from workgroup_4 import find_path
from workgroup_4 import find_all_paths
from workgroup_4 import find_path_weighted
from workgroup_4 import cheapest_path

#Graph exemples
graph = {
        "a":["b","c"],
        "b": ["d"],
        "c":["d"],
        "d" : ["e"],
        "e" :[],
        "f":[]
}

graph2 = {
        "a":["c"],
        "b": ["d","a"],
        "c":["d"],
        "d" : ["e","f"],
        "e" :[],
        "f":[]
}

weighted_graph = {
        "a":[{"node":"b","weight":1},{"node":"c","weight":2}],
        "b": [{"node":"d","weight":3}],
        "c":[{"node":"d","weight":1}],
        "d" : [{"node":"e","weight":3}],
        "e" :[],
        "f":[]
}

#Test Find path 

class TestGraphs(unittest.TestCase):

    def test_find_path():
        assert find_path(graph,"a","b") == ['a', 'b']
        assert find_path(graph,"a","d") == ['a', 'b', 'd']
        assert find_path(graph2,"b","c") == ['b', 'a', 'c']
        assert find_path(graph2,"a","e")== ['a', 'c', 'd', 'e']
        assert find_path(graph2,"a","f")== ['a', 'c', 'd', 'f']
        assert find_path(graph,"a","a") == ['a']
        assert find_path(graph,"b","b") == ['b']
        assert find_path(graph,"a","g") == None 
        assert find_path(graph,"a","f") == None 
        assert find_path(graph2,"e","f")== None

# Test Find all paths
                      
    def test_find_all_path():
        assert find_all_paths(graph,"a","b") == [['a', 'b']]
        assert find_all_paths(graph,"b","d") == [['b', 'd']]
        assert find_all_paths(graph,"a","d") == [['a', 'b', 'd'], ['a', 'c', 'd']]
        assert find_all_paths(graph,"b","c") == []
        assert find_all_paths(graph,"d","a") == []
        
    
    
# Test Path weighted
    
    def test_find_path_weighted():
        assert find_path_weighted(weighted_graph,"a","b") == [{'node': 'a', 'weight': 0}, {'node': 'b', 'weight': 1}]
        assert find_path_weighted(weighted_graph,"a","c") == [{'node': 'a', 'weight': 0}, {'node': 'c', 'weight': 2}]
        assert find_path_weighted(weighted_graph,"b","d") == [{'node': 'b', 'weight': 0}, {'node': 'd', 'weight': 3}]
        
    
# Test Cheapest Path
    
    def test_cheapest_path():
        assert cheapest_path(weighted_graph,"a","b") == [[{'node': 'a', 'weight': 0}, {'node': 'b', 'weight': 1}]]
        assert cheapest_path(weighted_graph,"a","c") == [[{'node': 'a', 'weight': 0}, {'node': 'c', 'weight': 2}]]
        assert cheapest_path(weighted_graph,"a","a") == [[{'node': 'a', 'weight': 0}]]
        assert cheapest_path(weighted_graph,"b","b") == [[{'node': 'b', 'weight': 0}]]
        assert cheapest_path(weighted_graph,"a","d") == [[{'node': 'a', 'weight': 0}, {'node': 'c', 'weight':2}, {'node':'d', 'weight':1}]]
        
        
        