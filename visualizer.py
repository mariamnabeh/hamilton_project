import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def _build_nx(graph):
    G = nx.Graph()
    G.add_nodes_from(range(graph.V))
    for u in range(graph.V):
        for v in range(u + 1, graph.V):
            if graph.adj[u][v] == 1:
                G.add_edge(u, v)
    return G


def draw(graph, path=None, title="Hamilton Graph"):
    G   = _build_nx(graph)
    pos = nx.spring_layout(G, seed=42)

    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor("#0f0f1a")
    ax.set_facecolor("#0f0f1a")

    nx.draw_networkx_nodes(G, pos, node_color="#4f46e5", node_size=900, ax=ax)
    nx.draw_networkx_labels(G, pos, font_color="white", font_size=13, font_weight="bold", ax=ax)
    nx.draw_networkx_edges(G, pos, edge_color="#555577", width=2, ax=ax)

    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                               edge_color="#ef4444", width=5, ax=ax)

        is_circuit = path[0] == path[-1]
        label = "Hamilton Circuit 🔴" if is_circuit else "Hamilton Path 🔴"
        patch = mpatches.Patch(color="#ef4444", label=label)
        ax.legend(handles=[patch], facecolor="#1e1e3a", labelcolor="white", fontsize=11)

    ax.set_title(title, color="white", fontsize=15, pad=15)
    ax.axis("off")
    plt.tight_layout()
    plt.show()
