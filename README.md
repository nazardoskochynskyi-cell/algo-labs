# Hamsters Diet Optimization (Greedy & Binary Search)

## 📝 Project Overview
This project solves a resource allocation problem using a combination of **Binary Search on the Answer** and a **Greedy Approach**. It also features a custom, from-scratch implementation of the **Radix Sort** algorithm (backed by Counting Sort) to efficiently process arrays without relying on built-in sorting functions.

### 🎯 Exercise Task
A pet store sells $C$ hamsters. Each hamster has a base daily food requirement $H$ and a greed factor $G$. If multiple hamsters are kept together, each hamster consumes an additional $G$ packets of food for *every other* neighbor. Given a total daily food supply $S$, find the maximum number of hamsters you can afford to feed. 

*Example:* `S = 19, C = 4, hamsters = [[5, 0], [2, 2], [1, 4], [5, 1]]` 
*Result: 3 (We can pick the 1st, 2nd, and 4th hamsters).*

---

## ⚙️ Algorithm Explanation
The problem is solved efficiently using two main concepts:

1. **Binary Search on the Answer:** Instead of checking every possible number of hamsters sequentially, the algorithm uses binary search to guess the maximum number of hamsters (`mid`) we can buy, bounded between $0$ and $C$.
2. **Cost Calculation & Greedy Selection:** For a guessed number `mid`, the actual cost for each hamster $i$ to be part of that group is calculated as `cost = H_i + G_i * (mid - 1)`. 
3. **Custom Radix Sort:** To greedily pick the cheapest hamsters for our guessed size, the calculated costs are sorted using a custom implementation of **Radix Sort** (which processes digits one by one using Counting Sort). If the sum of the `mid` cheapest costs is $\le S$, we try buying more; otherwise, we try fewer.

### ⏱️ Complexity
* **Time Complexity:** $\mathcal{O}(\log C \times (C \cdot d))$, where $C$ is the total number of hamsters and $d$ is the maximum number of digits in the calculated costs. The binary search takes $\mathcal{O}(\log C)$ iterations, and in each iteration, the custom Radix Sort takes $\mathcal{O}(C \cdot d)$ time.
* **Space Complexity:** $\mathcal{O}(C)$ required for the output and counting arrays within the Counting Sort subroutine.

---

## 📁 Project Structure

```text
├── data.txt             # Input file containing S, C, and hamster data
├── lab2.py              # Core logic: Binary Search + Custom Radix Sort
├── test_lab2.py         # Unit tests and file parser
└── README.md