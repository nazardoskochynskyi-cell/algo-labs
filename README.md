# Indiana Jones and the Last Rectangular Traversal

## 📝 Project Overview
This project solves an algorithmic pathfinding problem using **Dynamic Programming (DP)**. The goal is to calculate the total number of unique valid paths through a grid (corridor) based on specific movement rules.

### 🎯 Exercise Task
Indiana Jones needs to pass through a rectangular corridor made of fragile tiles, each marked with a lowercase English letter. He starts at any tile in the leftmost column and must exit through either the top-right or bottom-right tile. He can move one step to the right, or jump to any tile to his right that has the *same letter* as his current tile. The program must calculate the total number of ways to successfully navigate the corridor.

---

## ⚙️ Algorithm Explanation
The solution uses Dynamic Programming to avoid redundant calculations. Instead of recursively exploring every possible path (which would lead to an exponential time complexity), the algorithm processes the grid column by column from left to right.

1. **State Representation:** The array `dp` keeps track of the number of valid paths to reach each cell in the current column.
2. **Optimization:** A hash map (or array) `sums` is maintained to store the running total of paths for each character ('a' through 'z'). This allows checking the "jump" condition in constant time.
3. **State Transition:** For each cell in the next column, the number of ways to reach it is updated based on the total paths to the same character (`sums[char]`) and the path from the immediately adjacent left cell.

### ⏱️ Complexity
* **Time Complexity:** $\mathcal{O}(W \times H)$, where $W$ is the width and $H$ is the height of the grid. The algorithm processes each cell exactly once.
* **Space Complexity:** $\mathcal{O}(H)$ for storing the `dp` array of the current column. The memory used for the character `sums` dictionary is $\mathcal{O}(1)$ since the alphabet size is constant (26 letters).

---

## 📁 Project Structure

```text
├── in_ijones.txt        # Input file containing grid dimensions and matrix
├── out_ijones.txt       # Output file for the result
├── ijones.py            # Core algorithm implementation
└── README.md