# Data Structures Reference

Common data structures with operations and implementations.

## Arrays

**Fixed-size, contiguous memory**

| Operation | Time |
|-----------|------|
| Access by index | O(1) |
| Search (unsorted) | O(n) |
| Insert at end | O(1)* |
| Insert at position | O(n) |
| Delete | O(n) |

---

## Linked Lists

**Nodes with pointers**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

| Operation | Singly | Doubly |
|-----------|--------|--------|
| Access | O(n) | O(n) |
| Insert at head | O(1) | O(1) |
| Insert at tail | O(n) | O(1) |
| Delete (given node) | O(n) | O(1) |

---

## Stacks (LIFO)

```python
stack = []
stack.append(x)     # Push
top = stack.pop()   # Pop
top = stack[-1]     # Peek
```

**Use cases:** Undo, DFS, expression evaluation, parenthesis matching

---

## Queues (FIFO)

```python
from collections import deque
queue = deque()
queue.append(x)       # Enqueue (right)
front = queue.popleft()  # Dequeue (left)
```

**Use cases:** BFS, task scheduling, buffering

---

## Hash Tables

**Key-value pairs with O(1) average operations**

```python
d = {}
d[key] = value      # Insert/Update
value = d.get(key)  # Retrieve
del d[key]          # Delete
key in d            # Check existence
```

| Operation | Average | Worst |
|-----------|---------|-------|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Delete | O(1) | O(n) |

---

## Binary Trees

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Traversals

```python
# Inorder (Left, Root, Right) - BST gives sorted order
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val)
        inorder(node.right)

# Preorder (Root, Left, Right)
def preorder(node):
    if node:
        print(node.val)
        preorder(node.left)
        preorder(node.right)

# Postorder (Left, Right, Root)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val)
```

---

## Binary Search Trees

**Left < Root < Right**

| Operation | Average | Worst (unbalanced) |
|-----------|---------|-------------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

---

## Heaps

**Complete binary tree with heap property**

- **Min-heap:** Parent ≤ children
- **Max-heap:** Parent ≥ children

```python
import heapq

# Min-heap
heap = []
heapq.heappush(heap, val)
smallest = heapq.heappop(heap)

# Max-heap (negate values)
heapq.heappush(heap, -val)
largest = -heapq.heappop(heap)
```

| Operation | Time |
|-----------|------|
| Insert | O(log n) |
| Extract min/max | O(log n) |
| Get min/max | O(1) |
| Heapify | O(n) |

---

## Graphs

**Representations:**

### Adjacency List
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

### Adjacency Matrix
```python
#     A  B  C  D
# A [[0, 1, 1, 0],
# B  [1, 0, 0, 1],
# C  [1, 0, 0, 1],
# D  [0, 1, 1, 0]]
```

| Representation | Space | Add Edge | Check Edge | Find Neighbors |
|---------------|-------|----------|------------|----------------|
| Adjacency List | O(V+E) | O(1) | O(degree) | O(1) |
| Adjacency Matrix | O(V²) | O(1) | O(1) | O(V) |

---

## Tries (Prefix Trees)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```

**Use cases:** Autocomplete, spell check, prefix matching
