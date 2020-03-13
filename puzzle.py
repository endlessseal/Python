x = '''-,16,12,21,-,-,-
16,-,-,17,20,-,-
12,-,-,28,-,31,-
21,17,28,-,18,19,23
-,20,-,18,-,-,11
-,-,31,19,-,-,27
-,-,-,23,11,27,-'''

from collections import defaultdict
from operator import itemgetter

class Node():
    def __init__(self,name,to_node,value):
        self.name = name
        self.paths = [(to_node,int(value))]
    
    def add_to_path(self,to_node,value):
        self.paths.append((to_node,int(value)))
        
    def __eq__(self,other):
        return self.name == other
    
    def __ne__(self,other):
        return not self.name == other
        
    def __repr__(self):
        return '{} -> {}'.format(self.name, self.paths)

def create_mapping(data):
    list_of_node = defaultdict(Node)
    grid = [[x for x in c.split(',')] for c in data.split('\n')]
    
    
    for row_index in range(0,len(grid)):
        for col_index in range(0,len(grid[0])):
            value = grid[row_index][col_index]
            if value != '-':
                if not row_index in list_of_node.keys():
                    list_of_node[row_index] = Node(row_index,col_index,value)
                else:
                    list_of_node[row_index].add_to_path(col_index,value)
    return list_of_node

            

def solve(nodes, found=set(),cost=0):
    for each_node in nodes:
        if each_node.name not in found:
            for potential_node in sorted(each_node.paths, key = itemgetter(1)):
                node, value = potential_node
                if node not in found:
                    found.add(node)
                    print(each_node.name, node)
                    print(each_node)
                    cost += value
                    break
    if len(found) != len(nodes):
        solve(nodes,found,cost)
    else:
        print(cost)


solve(create_mapping(x))
