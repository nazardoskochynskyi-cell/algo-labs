# String Matching Algorithm using DFA 🔍

## 📝 Project Overview
This repository contains the implementation of a string matching algorithm using a **Deterministic Finite Automaton (DFA)**. The algorithm efficiently searches for all occurrences of a specific pattern (`needle`) within a given text (`haystack`).

### 🎯 Exercise Task
Create a function in Python that takes two strings: `haystack` (arbitrary text) and `needle` (the string to search for). The program must find and return the starting indices of all occurrences of `needle` in `haystack` using the finite state machine approach.

---

## ⚙️ Algorithm Explanation
The DFA string matching algorithm works in two main phases:

1. **Preprocessing (Building the Transition Table):** A 2D transition table (`TF`) is constructed from the `needle`. This table dictates the next state of the automaton based on the current state and the next input character.
2. **Searching:** The `haystack` is processed character by character. The state updates according to the transition table. If the automaton reaches the final state (equal to the length of the `needle`), a match is found.

### ⏱️ Complexity
* **Time Complexity:** * Table generation: `O(m * |Σ|)`, where `m` is the length of the pattern and `|Σ|` is the number of unique characters in the pattern.
  * Searching: `O(n)`, where `n` is the length of the text.
  * **Overall Time Complexity: `O(n + m * |Σ|)`**
* **Space Complexity:** `O(m * |Σ|)` to store the transition table.

---

## 📁 Project Structure

```text
├── src/
│   └── dfa.py           # Core implementation of the DFA algorithm
├── tests/
│   └── test_dfa.py      # Unit tests using the unittest framework
└── README.md