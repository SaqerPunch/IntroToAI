class Astar_Node:
    def __init__(self, weight, heuristic,):
        self.weight = weight
        self.heuristic = heuristic 
        self.next = None

class SaqerPriorityQueue:
    def __init__(self):
        self.front = None

    def push(self, val):
        temp = SaqerNode(val)

        if self.front == None:
            self.front = temp
            return

        pnt = self.front
        while temp.val < self.front.val:
            pnt = self.front.next
        

            

