class Astar_Node:
    def __init__(self, weight, heuristic):
        self.weight = weight
        self.heuristic = heuristic 
        self.priority = weight + heuristic
        self.next = None

class Astar_PriorityQueue:
    def __init__(self):
        self.front = None

    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False
        

    def push(self, weight, heuristic):
        
        temp = Astar_Node(weight,heuristic)
        if self.isEmpty() == True:
            self.front = temp
            return
        
        else:
            if temp.priority < self.front.priority:
                temp.next = self.front
                self.front = temp
            
            else:

                ptr = self.front
                while ptr:

                    if ptr.priority <= self.front.priority:
                        break
                    
                    ptr = ptr.next
                
                temp.next = ptr.next
                ptr.next = temp

        return
    
    def pop(self):

        if self.isEmpty():
            return None
        
        else:
            self.front = self.front.next
            return self.front

    def priority(self):
        if self.isEmpty():
            return None
        else:
            return self.front.priority

