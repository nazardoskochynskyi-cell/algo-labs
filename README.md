# lood Fill Algorithm (Matrix Traversal) 🎨

## 📝 Project Overview
This project implements the **Flood Fill** algorithm (also known as bucket fill), a classic matrix traversal technique used in computer graphics (like the "paint bucket" tool) and games (like Minesweeper or Go). Additionally, this repository includes an extended application of the algorithm to count the number of independent "islands" (connected components) on a 2D map.

### 🎯 Exercise Task
Create a program that reads a 2D matrix of colors from an `input.txt` file. Given a starting coordinate $(r, c)$ and a `replacement_color`, the algorithm must find all adjacent cells connected to the starting cell that share the same original color and change them to the replacement color. The modified matrix is then saved to `output.txt`.
---

## ⚙️ Algorithm Explanation
The solution uses **Breadth-First Search (BFS)** to traverse the matrix:

1. **Initialization:** The target color of the starting cell is identified. If the target color is already the replacement color, the algorithm safely terminates.
2. **Queue-based Traversal:** The starting coordinates are placed in a queue, and the cell's color is immediately updated.
3. **Exploration:** While the queue is not empty, the algorithm pops a cell and checks its 4 directional neighbors (Up, Down, Left, Right). 
4. **Validation:** If a neighbor is within the matrix boundaries and matches the original target color, its color is updated, and it is added to the queue for further exploration.

### 🌟 Bonus Feature: Connected Components
The project also includes a `count_islands` function, which leverages the Flood Fill algorithm to scan a satellite map (Land/Water) and count the total number of disjoint landmasses.

### ⏱️ Complexity
* **Time Complexity:** $\mathcal{O}(R \times C)$, where $R$ is the number of rows and $C$ is the number of columns. Each cell is processed and pushed to the queue at most once.
* **Space Complexity:** $\mathcal{O}(R \times C)$ in the worst-case scenario (e.g., a massive matrix of a single color) due to the memory required to store the coordinates in the BFS queue.

---

## 📁 Project Structure

```text
├── input.txt            # Input file with dimensions, start coordinates, and matrix
├── output.txt           # Generated output matrix after applying flood fill
├── bucket_mode.py       # Core BFS algorithm and file parser
├── count_islands.py     # Bonus implementation: Number of Islands
└── tests.py             # Unit tests for automated verification