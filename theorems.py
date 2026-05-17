def check_dirac(graph):
    n       = graph.V
    degrees = graph.get_degrees()
    return all(d >= n // 2 for d in degrees)


def check_ore(graph):
    n = graph.V
    for u in range(n):
        for v in range(u + 1, n):
            if graph.adj[u][v] == 0:
                deg_sum = sum(graph.adj[u]) + sum(graph.adj[v])
                if deg_sum < n:
                    return False
    return True


def analyze(graph):
    results = {}
    if check_dirac(graph):
        results["message"] = "Dirac's Theorem: Hamilton Circuit is GUARANTEED"
    elif check_ore(graph):
        results["message"] = "Ore's Theorem: Hamilton Circuit is GUARANTEED"
    else:
        results["message"] = "No theorem guarantees a circuit (may still exist)"
    results["degrees"] = graph.get_degrees()
    return results