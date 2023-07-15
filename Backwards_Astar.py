import Astar_graph
import AStar_PriorityQueue

def backwards_Astar(g:Astar_graph.Astargraph, goal, start):
    path = []
    while start != goal:
        # Repeated A* Code
        frontier = AStar_PriorityQueue.Astar_PriorityQueue()
        cost = 0
        frontier.push(cost, start)
        path = []
        while frontier:
            current = frontier.pop()  # Node Type
            path.append(current)
            cost += g.graph[current.index][1]

            if current == goal:
                break

            for neighbors in range(g.x):
                temp = g.graph[current.index][neighbors]
                frontier.push(temp, cost)

        # Backwards A-Star
        for i in range(len(path) - 1):
            print(path[i])

def main():
    n = input("Enter Number of Nodes")
    graph = Astar_graph.Astar_graph(n)

    goal = input("Enter goal")
    start = input("Enter Start")

    backwards_Astar(graph,goal, start)
