"""Module including all DFS algorithms"""

def depth_first_search(graph, start_node, target_node, visited = None, path = None):
    """
    https://en.wikipedia.org/wiki/Depth-first_search
    
    Time complexity:
        O(V+E)
    
    Space complexity:
        O(V)
        
    with V the vertices and E the edges
    """

    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start_node)
    path.append(start_node)

    if start_node == target_node:
        return path

    for neighbor in graph[start_node]:
        if neighbor not in visited:
            result = depth_first_search(
                graph, neighbor, target_node, visited, path
                )
            if result:
                return result

    path.pop()
    return None


def iterative_deepening_dfs(graph, node, target_node, max_depth = 1):
    """
    https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search
    
    Time complexity:
        O(b^d)
        
    Space complexity:
        O(d)
        
    with b the branching factor and d the depth
    """

    for depth in range(1, max_depth+1):
        visited = set()
        path = []

        if _limited_dfs(graph, node, target_node, depth, visited, path):
            return path

    return None


def _limited_dfs(graph, node, target_node, depth, visited, path): # pylint: disable=R0913
    """ 
    Helper function for iterative_deepening_dfs()
    """
    if depth == 0:
        return False

    visited.add(node)
    path.append(node)

    if node == target_node:
        return True

    for neighbor in graph[node]:
        if neighbor not in visited:
            if _limited_dfs(graph, neighbor, target_node, depth - 1, visited, path):
                return True

    path.pop()
    return False
