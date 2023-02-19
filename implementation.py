from CreateGraph import Graph
from CreateGraph import Vertex
from CreateGraph import shortest_ 
from Dijkstra import dijkstra
if __name__ == '__main__':
    g = Graph.Graph()
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'e', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('d', 'e', 6)

    print("Graph: ")
    for v in g:
        for w in v.get_connection():
            vid = v.get_node()
            wid = w.get_node()
            print(f"({vid})--{v.get_weight(w)}-->({wid})",end="\n")
    dijkstra(g,g.get_vertex('a'),g.get_vertex('d'))
    target = g.get_vertex('e')
    path = [target.get_node()]
    shortest_.shortest(target,path)
    print("Shortest path: {}".format(path[::-1]))
