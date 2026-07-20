
from dataclasses import replace
from typing import Dict, Any
from collections import deque
import itertools

class Node:

    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __eq__(self, other) -> bool:

        visited = set()
    
        def dfs(a, b):
            
            if a.val != b.val or len(a.neighbors) != len(b.neighbors):
                return False
            
            if a.val in visited:
                return True
            
            visited.add(a.val)
            
            return all(dfs(*pair) for pair in zip(a.neighbors, b.neighbors))
        
        return isinstance(other, self.__class__) and dfs(self, other)
    
    def __repr__(self):
        return f"Node(val: {self.val}, neighbors: {self.neighbors})"
    
    def __str__(self):
        return self.__repr__()

class Graph:
    
    def __init__(self, adj_list=None, root_node_val=None, use_sample=False):
        
        sample_adj  = [
            [4, 5],
            [4],
            [1, 2],
            [7, 8],
            [4, 6],
            [10, 11],
            [9],
            [9, 10],
            [12],
            [12, 13],
            [10],
            [],
            [],
        ]
        
        self.adj_list = adj_list if not use_sample else sample_adj
        self.nodes = self.construct_val_node_dict(self.adj_list) if self.adj_list else None
        self.root_node_val = root_node_val or self.get_root_node_val()
        self.root = self.nodes[self.root_node_val] if self.nodes else None
        
    def __repr__(self):
        return str(self.root)
    
    def __str__(self):
        return self.__repr__()
    
    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.root == self.root
    
    def adj_list_to_dict(self):
        return {i+1:self.adj_list[i] for i in range(len(self.adj_list))}
    
    
    def get_root_node_val(self):
        '''
        Determine value of root node
    
        An index value that does not exist in the values of the neighbors
        in the adjacency list is a node that has no in-degree (no incoming edges)
        and hence it is considered as the root node.
        '''
        
        if self.adj_list:
                
            idxs = set(range(1, len(self.adj_list)+1))
            vertices = set(itertools.chain(*self.adj_list))
            diff = idxs-vertices

            return list(diff)[0] if diff else 1
        
    
    def construct_val_node_dict(self, adj_list):
        '''
        Construct a dictionary of node.val->node key,val pairs
        '''

        nodes = [Node(i + 1) for i in range(len(adj_list))]
        
        for i, neighbors in enumerate(self.adj_list):
            nodes[i].neighbors = [nodes[j-1] for j in neighbors]
        
        return {i+1:node for i, node in enumerate(nodes)}
    

    def dfs_traverse(self, start=None, leaf_stop=False):
        '''
        Traverse the graph depth first
        '''
        
        dfs_path = []
        visited = set()
        
        def dfs(node: Node):
            
            if node.val not in visited:
                dfs_path.append(node.val)
                visited.add(node.val)
                for n in node.neighbors:
                    if leaf_stop is False:
                        dfs(n)
                    else:
                        return dfs(n)
        
        start = self.nodes.get(start) if start is not None else self.root
                
        if not start:
            return None
        
        dfs(start)
        return dfs_path
    
    
    def get_top_sort(self):
        '''
        Get a topologically sorted array
        
        Verify output: https://techiedelight.com/compiler/?~testing
        Visualize: https://www.cs.usfca.edu/~galles/visualization/TopoSortDFS.html
        '''
        
        top_sorted = deque()
        visited = set()

        def topsort(node: Node):
            
            # print(f"\nProcessing: {node.val = }, {visited = }, {top_sorted = }")
            
            if node.val not in visited:
                visited.add(node.val)
                
                '''
                If there are no neighbors, it is a leaf node
                In the case there are no neighbors, the recursive
                calls will start returning. When this happens
                we start collecting the node values by adding them at
                beginning of the `top_sorted` queue.
                '''
                for n in node.neighbors:
                    if n.val not in visited:                        
                        top_sorted.appendleft(topsort(n))
            
            return node.val
            
        
        topsort(self.root)
        top_sorted.appendleft(self.root_node_val)
        return list(top_sorted)
    