# Zigzag 2D Array Traversal

## 📝 Project Overview
This project implements an algorithm to traverse and populate a 2D matrix in a **Zigzag** (diagonal) pattern. This is a classic algorithmic problem that tests matrix manipulation, boundary condition handling, and direction toggling.

### 🎯 Exercise Task
Write a program to traverse an $M \times N$ 2D array in a "zigzag" pattern. Starting from the top-left corner, the traversal moves diagonally across the matrix. The algorithm must receive dimensions $M$ and $N$ and return the matrix filled with sequential elements indicating the order of visitation. 

*Example for a 3x3 matrix:*
```text
  1  2  6
  3  5  7
  4  8  9
```
# ⚙️ Algorithm Explanation

The solution uses a state-machine-like approach to simulate the movement across the matrix. It keeps track of the current row, col, and the direct (direction of movement: 1 for up-right, -1 for down-left).

Initialization: An empty matrix of zeros is created. The starting position is (0, 0).

Traversal: A loop runs from 1 to M×N, assigning the current integer to the current cell matrix[row][col].

Boundary Checks (Direction 1 - Moving Up-Right): * If the rightmost column is hit, move down one row and reverse direction.

If the top row is hit, move right one column and reverse direction.

Otherwise, continue diagonally (row - 1, col + 1).

Boundary Checks (Direction -1 - Moving Down-Left):

If the bottom row is hit, move right one column and reverse direction.

If the leftmost column is hit, move down one row and reverse direction.

Otherwise, continue diagonally (row + 1, col - 1).

# ⏱️ Complexity

Time Complexity: O(M×N), where M is the number of rows and N is the number of columns. The algorithm visits and fills each cell exactly once.

Space Complexity: O(M×N) to create and store the resulting 2D array.

# 📁 Project Structure


        ├── lab1_1.py            # Core algorithm implementation (zigzag function)
        ├── test_lab1.py         # Unit tests for various matrix dimensions
        └── README.md