class Astar_graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_list = {node: set() for node in range(self.num_nodes)}

    def edge_add(self, first_node, second_node, weight):
        self.adj_list[second_node].add((first_node,weight))