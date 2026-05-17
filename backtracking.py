def _util(graph, path, pos):
    if pos == graph.V:
        return True

    for v in range(graph.V):
        if graph.adj[path[pos - 1]][v] == 1 and v not in path:
            path[pos] = v
            if _util(graph, path, pos + 1):
                return True
            path[pos] = -1

    return False


def find_hamilton_path(graph):
    path = [-1] * graph.V
    path[0] = 0
    if not _util(graph, path, 1):
        return None
    return path


def find_hamilton_circuit(graph):
    path = find_hamilton_path(graph)
    if path and graph.adj[path[-1]][path[0]] == 1:
        return path + [path[0]]
    return None
