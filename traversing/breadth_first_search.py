"""Module including all BFS algorithms"""
from collections import deque


def breadth_first_search(graph, start_node, target_node):
    """
    https://en.wikipedia.org/wiki/Breadth-first_search
    
    Time complexity:
        O(b^d) 
       
    Space complexity:
        O(b^d)  
    with b the branching factor and d the depth
    """

    visited = set()
    queue = deque([(start_node, [start_node])])
    visited.add(start_node)

    while queue:
        node, path = queue.popleft()

        if node == target_node:
            return True, path

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return False, []
