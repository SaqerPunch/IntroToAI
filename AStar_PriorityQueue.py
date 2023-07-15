
class Astar_Node:
    def __init__(self, heuristic):
        self.heuristic = heuristic 
        self.priority = None
        self.next = None

class Astar_PriorityQueue:
    def __init__(self):
        self.front = None

    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False

    def push(self, cost, node:Astar_Node):

        node.priority = node.heuristic + cost
        
        if self.isEmpty() == True:
            self.front = node
            return
        
        else:
            if  node.priority < self.front.priority:
                node.next = self.front
                self.front = node
            
            else:

                ptr = self.front
                while ptr:

                    if ptr.priority<= self.front.priority:
                        break
                    
                    ptr = ptr.next
                
                node.next = ptr.next
                ptr.next = node

        return
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            front_node = self.front
            self.front = self.front.next
            return front_node

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.front.heuristic
    
   

