import sys
import Vertex

class Graph():
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
    
    def __iter__(self):
        return iter(self.vert_dict.values())
    
    def add_vertex(self,node):
        self.num_vertices +=1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex
    
    def add_edge(self,frm,to,cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        
        self.vert_dict[frm].add_neighbor(self.vert_dict[to],cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm],cost)
    
    def get_vertices(self):
        return self.vert_dict.keys()
    
    def set_previous(self,current):
        self.previous = current
    
    def get_previous(self,current):
        return self.previous