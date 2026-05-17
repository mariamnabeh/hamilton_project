from itertools import permutations


def _is_valid_path(graph, path):
    for i in range(len(path) - 1):
        if graph.adj[path[i]][path[i + 1]] == 0:
            return False
    return True


def brute_force_path(graph):
    nodes = list(range(graph.V))
    for perm in permutations(nodes):
        if _is_valid_path(graph, perm):
            return list(perm)
    return None


def brute_force_circuit(graph):
    nodes = list(range(graph.V))
    for perm in permutations(nodes[1:]):
        path = [nodes[0]] + list(perm)
        if _is_valid_path(graph, path) and graph.adj[path[-1]][path[0]] == 1:
            return path + [path[0]]
    return None
