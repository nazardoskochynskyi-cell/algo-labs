# Venice Fiber Optic Network (Prim's Algorithm) 🌉

## 📝 Project Overview
This project solves a network design problem using **Prim's Algorithm** to find the **Minimum Spanning Tree (MST)** of a graph. The goal is to determine the minimum total length of fiber optic cables required to connect all islands in Venice, ensuring every island is accessible within the same network.

### 🎯 Exercise Task
The municipality of Venice has requested an optical fiber internet setup. The city consists of islands separated by canals and connected by bridges. The goal is to connect all islands directly or indirectly using the minimum possible length of underwater cables. The input is a CSV file (`islands.csv`) containing an adjacency matrix representing distances between islands $i$ and $j$. The number of islands $N$ is up to 100.

---

## ⚙️ Algorithm Explanation
The solution uses **Prim's Algorithm**, a greedy approach that builds the Minimum Spanning Tree one vertex at a time:

1. **Initialization:** Start with the first island (index 0) and mark it as connected.
2. **Greedy Expansion:** Iterate through all currently connected islands and look for the shortest available edge (cable) that connects to an *unvisited* island.
3. **Connection:** Add the shortest edge to the total cable length, mark the newly reached island as connected, and increment the connections count.
4. **Termination:** Repeat the process until $N - 1$ connections are made, meaning all islands are successfully linked into a single network.

### ⏱️ Complexity
* **Time Complexity:** $\mathcal{O}(V^3)$ based on the current implementation, where $V$ is the number of vertices (islands). For each of the $V-1$ edges added, the algorithm scans the entire $V \times V$ matrix to find the minimum valid edge. Given the constraint $V \le 100$, this executes well within acceptable limits. 
* **Space Complexity:** $\mathcal{O}(V^2)$ to store the 2D adjacency matrix parsed from the CSV file, plus $\mathcal{O}(V)$ for the `connected_islands` boolean array.

---

## 📁 Project Structure

```text
├── islands.csv          # Input file (Adjacency Matrix)
├── islands_mst.py       # Core algorithm implementation
└── README.md