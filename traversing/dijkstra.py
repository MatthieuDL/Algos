"""This module contains Dijkstra's algorithm"""
import heapq


def dijkstra(graph, start_node, target_node):
    """
    Dijkstra's algorithm calculates the shortest path from
    a starting node to all other nodes.

    https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

    Time complexity:
        O(V**2)

    Space complexity:
        O(V)  
    with V the number of vertices and E the number of edges
    """
    priority_queue = [(0, start_node)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_node] = 0

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def dijkstra_fib(graph, start_node):
    """
    
    Time complexity:
        O((V + E) log V)

    """
