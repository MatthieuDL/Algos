"""Module including all BFS algorithms"""
from collections import deque


def breadth_first_search(graph, start_node):
    """
    https://en.wikipedia.org/wiki/Breadth-first_search
    
    Time complexity:
        O(b^d) 
       
    Space complexity:
        O(b^d)  
    with b the branching factor and d the depth
    """

    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while deque:
        node = queue.popleft()
        print(node) # Process node here

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
