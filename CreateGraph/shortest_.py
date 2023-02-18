from CreateGraph import Graph
from CreateGraph import Vertex

def shortest(v,path):
    if v.previous:
        path.append(v.previous.get_node())
        shortest(v.previous,path)
    return
    