# Game Server Latency Minimization (Dijkstra's Algorithm) 🎮

## 📝 Project Overview
This project solves a network optimization problem using **Dijkstra's Algorithm** and a custom **Min-Heap (Priority Queue)**. The objective is to find the optimal placement for a central game server in a network topology to minimize the maximum network latency experienced by any client.

### 🎯 Exercise Task
You are developing an online game and need to place a central server to ensure the lowest possible maximum latency for all players (clients). The network is an undirected graph where nodes are routers, clients, or the server, and edges represent latency. The server can be placed on any node that is not a client. The program must find the optimal server location that minimizes the maximum shortest-path latency to any client, and return this minimum possible latency value.
---

## ⚙️ Algorithm Explanation
The solution uses a minimax approach on top of the shortest-path algorithm:

1. **Graph Representation:** The network topology is stored as an adjacency list.
2. **Custom Priority Queue:** A `MinHeap` class is implemented from scratch with `sift_up` and `sift_down` operations to efficiently fetch the node with the smallest current distance.
3. **Dijkstra's Algorithm:** For *each* potential server node (any node not in the clients list), the algorithm calculates the shortest paths to all other nodes in the network.
4. **Minimax Optimization:** For a given server, we find the maximum latency among all clients. We then compare this maximum across all possible server placements and select the overall minimum.

### ⏱️ Complexity
* **Time Complexity:** $\mathcal{O}(V \times (V + E) \log V)$, where $V$ is the number of vertices (up to 1000) and $E$ is the number of edges (up to 1000). Running Dijkstra's algorithm takes $\mathcal{O}((V + E) \log V)$ using the Min-Heap, and we run it at most $V$ times (for each potential server).
* **Space Complexity:** $\mathcal{O}(V + E)$ to store the graph as an adjacency list, plus $\mathcal{O}(V)$ for the distances array and the priority queue.

---

## 📁 Project Structure

```text
├── src/
│   └── server.py        # Core algorithm (Dijkstra + custom MinHeap)
├── tests/
│   └── test_server.py   # Unit tests for the given examples
└── README.md