class Graph:
    def __init__(self, vertices):
        self.V   = vertices
        self.adj = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u][v] = 1
        self.adj[v][u] = 1

    def _dfs(self, v, visited):
        visited[v] = True
        for i in range(self.V):
            if self.adj[v][i] == 1 and not visited[i]:
                self._dfs(i, visited)

    def is_connected(self):
        visited = [False] * self.V
        self._dfs(0, visited)
        return all(visited)

    def get_degrees(self):
        return [sum(row) for row in self.adj]

    def from_input(self):
        edges = int(input("Number of edges: "))
        for _ in range(edges):
            line = input("Edge (e.g. 0 1): ").split()
            self.add_edge(int(line[0]), int(line[1]))