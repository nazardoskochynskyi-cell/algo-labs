# Red-Black Tree based Priority Queue

## 📝 Project Overview
This project features a custom implementation of a **Priority Queue** backed by a **Red-Black Tree** to guarantee balanced performance. To demonstrate its practical utility, the data structure is integrated into an interactive **Airport Boarding Gate Simulator**, where passengers are dynamically managed and boarded based on their status priority (VIP, Special Needs, Business, Economy).

### 🎯 Exercise Task
Implement a "priority queue" data structure based on a Red-Black Tree. The tree must be structured such that a parent element has a higher priority than its right child, and a lower or equal priority compared to its left child. The queue must support the following operations:
1. Insert an element with a given value and priority.
2. Remove and return the element with the highest priority.
3. Peek at the highest priority element without modifying the queue.
Use a dedicated `Node` class where each element holds a value and a priority.
---

## ⚙️ Algorithm Explanation
Unlike a standard Binary Search Tree (BST), which can degrade into a linked list in the worst case, a **Red-Black Tree** self-balances after every insertion and deletion. This ensures strictly logarithmic height.

1. **Custom Ordering:** Based on the assignment constraints, higher priority values are routed to the *left* subtree (`new_node.priority >= current.priority`). This means the element with the absolute highest priority is always the leftmost node in the tree.
2. **Insertion (`_insert_fixup`):** Nodes are inserted as RED. If this violates the Red-Black properties (e.g., two consecutive RED nodes), the tree rebalances using color flips and structural rotations (Left-Rotate / Right-Rotate).
3. **Extraction (`pop`):** The algorithm traverses to the leftmost node, extracts its value, and safely deletes it from the tree. If the deleted node was BLACK, the tree calls `_delete_fixup` to restore balance and maintain the black-height property.

### ⏱️ Complexity
* **Time Complexity:**
  * **Insert:** $\mathcal{O}(\log N)$
  * **Pop (Extract Max):** $\mathcal{O}(\log N)$
  * **Peek:** $\mathcal{O}(\log N)$ (Traversal to the leftmost node)
* **Space Complexity:** $\mathcal{O}(N)$ to store the nodes in the tree, where $N$ is the number of items in the queue.

---

## 📁 Project Structure

```text
├── red_black_priority_queue.py                     # Core Red-Black Tree implementation
├── boarding_gate.py                                # Interactive Airport terminal CLI
├── test_red_black_priority_queue.py                # Unit tests for the Priority Queue
└── README.md