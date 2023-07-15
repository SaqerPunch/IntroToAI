from AStar_PriorityQueue import Astar_Node
class Astargraph:
    def init(self, num):
        self.x = num
        self.graph = [[] for i in range(self.x)]

    def edge_add(self, x, y, weight):
        node = Astar_Node(index=x)
        self.graph[y].append((node, weight))

        node = Astar_Node(index=y)
        self.graph[x].append((node, weight))
