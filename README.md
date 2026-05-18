# Hamilton Paths & Circuits

## Description

This project is a Discrete Mathematics application that finds **Hamilton Paths and Circuits** in graphs using Python.

A **Hamilton Path** is a path that visits every node in a graph exactly once.
A **Hamilton Circuit** is a Hamilton Path that starts and ends at the same node.

The project is divided across 5 team members, each responsible for one module:

| Member | File | Responsibility |
|--------|------|----------------|
| 1 | `graph.py` | Graph class — adjacency matrix and connectivity check |
| 2 | `brute_force.py` | Exhaustive search using all permutations — O(n!) |
| 3 | `backtracking.py` | Recursive backtracking algorithm with pruning |
| 4 | `theorems.py` | Dirac's theorem and Ore's theorem |
| 5 | `visualizer.py` | Graph visualization — highlights the path in red |

---

## Tools Used

- **Python 3.8+**
- **NetworkX** — graph structure and layout
- **Matplotlib** — rendering and displaying the graph window
- **itertools** — generating permutations in the brute-force module

---

## How to Run Your Code

**Step 1 — Install the required libraries**

```bash
pip install networkx matplotlib
```

**Step 2 — Run the interactive program**

```bash
python main.py
```

The program will ask you to enter:
- Number of nodes
- Number of edges
- Each edge as two numbers (example: `0 1`)
- Which algorithm to use: Backtracking or Brute Force






