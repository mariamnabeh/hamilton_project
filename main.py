from graph        import Graph
from theorems      import analyze
from backtracking  import find_hamilton_path, find_hamilton_circuit
from brute_force   import brute_force_path, brute_force_circuit
from visualizer    import draw
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hamilton_ui.html')

if __name__ == '__main__':
    app.run(debug=True)

def main():
    n = int(input("Number of nodes: "))
    g = Graph(n)
    g.from_input()

    if not g.is_connected():
        print("Graph is not connected — no Hamilton Path possible.")
        draw(g, title="Disconnected Graph")
        return

    theory = analyze(g)
    print("Theorem check:", theory["message"])
    print("Degrees:",        theory["degrees"])

    choice = input("Method? [1] Backtracking  [2] Brute Force: ")

    if choice == "2":
        path    = brute_force_path(g)
        circuit = brute_force_circuit(g)
    else:
        path    = find_hamilton_path(g)
        circuit = find_hamilton_circuit(g)

    if circuit:
        print("Hamilton Circuit:", " → ".join(map(str, circuit)))
        draw(g, path=circuit, title="Hamilton Circuit")
    elif path:
        print("Hamilton Path:", " → ".join(map(str, path)))
        draw(g, path=path, title="Hamilton Path")
    else:
        print("No Hamilton Path or Circuit found.")
        draw(g, title="No Solution Found")


if __name__ == "__main__":
    main()