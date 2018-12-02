
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:33:20 2018

@author: zinebmezzour
"""
#%%

from Network_Path import find_path
from Network_Path import find_all_paths
from Network_Path import find_path_weighted
from Network_Path import find_all_weighted_paths

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

#Find path 

def value_one_path():
    assert find_path(graph,"a","b") == ['a', 'b']
    assert find_path(graph,"a","d") == ['a', 'b', 'd']
    assert find_path(graph2,"b","c") == ['b', 'a', 'c']
    assert find_path(graph2,"a","e")== ['a', 'c', 'd', 'e']
    
   
   
def same_value_find_path():
    assert find_path(graph,"a","a") == ['a']
    assert find_path(graph,"b","b") == ['b']
    
def none_value_find_path():
     assert find_path(graph,"a","g") == None 
     assert find_path(graph,"a","f") == None 
     
     
     
#All weighted     
     

def value_find_all_path():
    assert find_all_paths(graph,"a","b") == [['a', 'b']]
    assert find_all_paths(graph,"b","d") == [['b', 'd']]
    assert find_all_paths(graph,"a","d") == [['a', 'b', 'd'], ['a', 'c', 'd']]
    
def no_value_find_all_path():
    assert find_all_paths(graph,"b","c") == []
    assert find_all_paths(graph,"d","a") == []


#Path weighted


def value_find_path_weighted():
    assert find_path_weighted(weighted_graph,"a","b") == [{'node': 'a', 'weight': 0}, {'node': 'b', 'weight': 1}]
    assert find_path_weighted(weighted_graph,"a","c") == [{'node': 'a', 'weight': 0}, {'node': 'c', 'weight': 2}]
    assert find_path_weighted(weighted_graph,"b","d") == [{'node': 'b', 'weight': 0}, {'node': 'd', 'weight': 3}]


    
#ALL Path weighted

def value_find_all_weighted_path():
    assert find_all_weighted_paths(weighted_graph,"a","b") == [[{'node': 'a', 'weight': 0}, {'node': 'b', 'weight': 1}]]
    assert find_all_weighted_paths(weighted_graph,"a","c") == [[{'node': 'a', 'weight': 0}, {'node': 'c', 'weight': 2}]]

def same_value_find_all_weighted_path():
    assert find_all_weighted_paths(weighted_graph,"a","a") == [[{'node': 'a', 'weight': 0}]]
    assert find_all_weighted_paths(weighted_graph,"b","b") == [[{'node': 'b', 'weight': 0}]]