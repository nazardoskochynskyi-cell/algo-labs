Binary Tree In-Order Successor Search

## 📝 Project Overview
This project implements an algorithm to find the **in-order successor** of a given node in a Binary Tree. Additionally, it features a custom post-order deserializer to construct trees dynamically from text files and a neat console-based tree visualizer.

### 🎯 Exercise Task
Given a binary tree and a specific node within it, implement a function to find the next element during an in-order traversal (Left-Root-Right). The successor is the node with the smallest key greater than the key of the input node. The function `find_successor(tree, node)` takes the root of the tree and the target node as inputs and returns the successor node. 

*Example Tree:*
```text
      10
     /  \
    5    15
   / \   / \
  3   7 12  20

For the node with value 7, the in-order successor is the node with value 10.
```
## ⚙️ Algorithm Explanation
1. In-Order Successor Search

The algorithm operates in O(H) time, where H is the height of the tree, by handling two main cases without needing to traverse the entire tree:

Node has a right subtree: The successor is the leftmost node in that right subtree. The algorithm steps into the right child and continuously moves left until it hits a leaf.

Node does NOT have a right subtree: We must look up the parent chain. The successor is the lowest ancestor of the node whose left child is also an ancestor of the node. The algorithm traverses up the tree until it is no longer a right child.

2. Post-Order Deserialization & Visualization (Bonus)

The project includes a robust method to parse a serialized post-order string (e.g., nil nil 3 nil nil 6 nil 7 5 ...) to dynamically reconstruct the tree objects in memory, complete with parent pointers. It also includes a print_tree method that calculates dynamic offsets to beautifully render the tree structure directly in the terminal using ASCII formatting.
## ⏱️ Complexity

Time Complexity (Search): O(H), where H is the height of the tree. In a balanced tree, this is O(logN); in the worst case (a heavily skewed tree), it degrades to O(N).

Space Complexity (Search): O(1), as the search algorithm relies solely on constant extra space via pointer manipulation.

## 📁 Project Structure
```
├── pre_tree.txt         # Input file containing serialized post-order tree data
├── lab3.py              # Core implementation (find_successor function)
├── extra_lab3.py        # Tree deserializer and CLI visualizer
├── test_lab3.py         # Unit tests for the search logic
└── README.md
```