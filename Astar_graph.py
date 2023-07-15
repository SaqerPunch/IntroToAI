from AStar_PriorityQueue import Astar_Node

class Astar_graph:
    def __init__(self, num):
        self.x = num
        self.graph = [None] * self.x

    def edge_add(self, x, y,weight):
        node = Astar_Node(index=x)
        node.next = self.graph[y]
        self.graph[y].append((node,weight))

        node = Astar_Node(index=y)
        node.next = self.graph[x]
        self.graph[x].append((node,weight))


"""
class Astar_graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_list = {node: set() for node in range(self.num_nodes)}

    def edge_add(self, first_node, second_node, weight):
        self.adj_list[second_node].add((first_node,weight))
"""

