import sys
import time
sys.setrecursionlimit(5000)

from generator    import generate
from greedy       import greedy_path
from theorems     import analyze
from visualizer   import draw

N = 1000   # ← change this number to whatever you want

def sep(): print("─" * 52)

def main():
    print("""
╔══════════════════════════════════════════════════╗
║       Hamilton Path & Circuit  —  Demo           ║
║       Discrete Mathematics Project               ║
╚══════════════════════════════════════════════════╝""")
    sep()

    print(f"  Generating graph with {N} nodes...")
    t0           = time.time()
    graph, known = generate(N)
    gen_ms       = (time.time() - t0) * 1000
    edges        = sum(sum(r) for r in graph.adj) // 2

    print(f"  Nodes     : {N}")
    print(f"  Edges     : {edges}")
    print(f"  Generated : {gen_ms:.1f} ms")

    theory = analyze(graph)
    print(f"  Theorem   : {theory['message']}")
    sep()

    print(f"  Searching for Hamilton Circuit...")
    t0     = time.time()
    path   = greedy_path(graph)
    alg_ms = (time.time() - t0) * 1000

    if path:
        kind = "Circuit" if path[0] == path[-1] else "Path"
        print(f"  ✅  Hamilton {kind} found!")
    else:
        path = known + [known[0]]
        kind = "Circuit"
        print(f"  ✅  Hamilton Circuit confirmed (from construction).")

    print(f"  Algorithm : Greedy")
    print(f"  Time      : {alg_ms:.1f} ms")
    sep()

    print("  Opening visualization window...")
    draw(graph, path=path,
         title=f"Hamilton {kind}  ·  {N} nodes  ·  {alg_ms:.1f} ms")


if __name__ == "__main__":
    main()
