# Assignment 6: Medians, Order Statistics & Elementary Data Structures

## Overview
This repository contains implementations for **Assignment 6**, focused on two main parts:  

### Part 1 – Selection Algorithms
- **Deterministic algorithm (Median of Medians)** – guarantees worst-case linear time selection.
- **Randomized algorithm (Quickselect)** – expected linear time selection.
- Includes empirical performance analysis on different input types (random, sorted, reverse-sorted).

### Part 2 – Elementary Data Structures
- Implemented from scratch in Python:
  - Arrays
  - Stacks
  - Queues
  - Linked Lists
- Includes analysis of time and space complexity, and discussion of practical applications.

---

## Repository Structure
### /MSCS532_Assignment6

│

├── PART1.py # Deterministic & Randomized selection implementations

├── PART2_data_structures.py # Arrays, Stacks, Queues, Linked List implementations

├── MSCS 532 Assignment6 # Detailed report with code screenshots & analysis

└── README.md # This file

---


## Requirements
- Python 3.x
- No additional libraries required (uses standard Python only)
- Optional: `time` module for measuring execution time in Part 1

---

## Usage Instructions

### Part 1 – Selection Algorithms
Run the Python script:
```bash
python part1_selection_algorithms.py
```

# Example usage inside PART1.py:
```
arr = [9, 2, 7, 4, 6, 3, 1]
k = 3

# Deterministic selection
print(deterministic_select(arr, k))

# Randomized selection
print(randomized_select(arr, k))
```
### Part 2 – Data Structures

Run the Python script:
```
python part2_data_structures.py
```

# Example usage inside PART2.py:
```
# Array example
arr = MyArray()
arr.insert(5)
arr.insert(10)
print(arr.access(1))  # Output: 10

# Stack example
stack = Stack()
stack.push(7)
stack.push(12)
print(stack.pop())    # Output: 12

# Queue example
queue = Queue()
queue.enqueue(3)
queue.enqueue(8)
print(queue.dequeue())  # Output: 3

# Linked List example
ll = LinkedList()
ll.insert(15)
ll.insert(20)
ll.delete(15)
``` 
# Observations & Analysis
## Part 1 – Selection Algorithms

- Deterministic (Median of Medians) ensures O(n) worst-case performance.

- Randomized (Quickselect) is faster on average but may vary depending on pivot selection.

- Empirical testing shows deterministic algorithm is stable, while randomized algorithm can vary slightly.

## Part 2 – Data Structures

- Arrays: fast access (O(1)), slower insertion/deletion (O(n))

- Linked Lists: efficient insertion/deletion (O(1)), slower random access (O(n))

- Stacks & Queues: array-based implementations provide efficient LIFO/FIFO operations

- Practical applications include task scheduling, expression evaluation, dynamic data handling.
