from CreateGraph import Graph
from CreateGraph import Vertex
from CreateGraph import shortest_ 
import heapq

def dijkstra(agraph,start,target):
    start.set_distance(0)

    unvisited_queue = [(v.get_distance(),v) for v in agraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        for next in current.adjacent:
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            if new_dist < next.get_distance():
                new_dist.set_distance(new_dist)
                next.set_previous(current)
                print(f"Updated:Current = {current.get_node()} next = {next.get_node()} new distance = {next.get_distance()}")
            else:
                print(f"Not Updated: current = {current.get_node()} next = {next.get_node()} new distance = {next.get_distance()}")
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        unvisited_queue = [(v.get_distance(),v) for v in agraph if not v.visited]
        heapq.heapify(unvisited_queue)