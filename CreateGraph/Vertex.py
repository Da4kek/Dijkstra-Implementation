import sys
class Vertex():
    def __init__(self,node):
        self.node = node
        self.adjacent = {}
        self.distance = sys.maxint
        self.visited = False
        self.previous = None 
    
    def add_neighbor(self,neighbor,weight = 0):
        self.adjacent[neighbor] = weight

    def get_connection(self):
        return self.adjacent.keys()
    
    def get_node(self):
        return self.node
    
    def get_weight(self,neighbor):
        return self.adjacent[neighbor]
    
    def set_distance(self,dist):
        self.distance = dist
    
    def get_distance(self):
        return self.distance
    
    def set_previous(self,prev):
        self.previous = prev
    
    def set_visited(self):
        self.visited = True
    
    def __str__(self):
        return f"{str(self.node)} adjacent: {str([x.node for x in self.adjacent])}"