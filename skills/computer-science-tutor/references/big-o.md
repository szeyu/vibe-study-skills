# Big-O Complexity Reference

## Complexity Classes

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

| Complexity | Name | Example | n=1000 |
|------------|------|---------|--------|
| O(1) | Constant | Array access | 1 |
| O(log n) | Logarithmic | Binary search | ~10 |
| O(n) | Linear | Linear search | 1,000 |
| O(n log n) | Linearithmic | Merge sort | ~10,000 |
| O(n²) | Quadratic | Bubble sort | 1,000,000 |
| O(n³) | Cubic | Matrix multiplication | 1,000,000,000 |
| O(2ⁿ) | Exponential | Recursive Fibonacci | Very large |
| O(n!) | Factorial | Permutations | Astronomically large |

---

## Visual Growth Comparison

```
Operations
    ^
    |                                    /
    |                                  /  O(n²)
    |                               /
    |                     ___------  O(n log n)
    |              ___---
    |       ___---_____________ O(n)
    |  ___--
    | /
    |__________________________ O(log n)
    |__________________________ O(1)
    +---------------------------------> n
```

---

## Common Operations Complexity

### Arrays
| Operation | Time |
|-----------|------|
| Access | O(1) |
| Search | O(n) |
| Insert at end | O(1) amortized |
| Insert at index | O(n) |
| Delete | O(n) |

### Hash Tables
| Operation | Average | Worst |
|-----------|---------|-------|
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Search | O(1) | O(n) |

### Binary Search Tree (Balanced)
| Operation | Time |
|-----------|------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |

---

## Sorting Algorithm Complexities

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) |

---

## How to Analyze Complexity

### Rules

1. **Drop constants:** O(2n) → O(n)
2. **Drop lower terms:** O(n² + n) → O(n²)
3. **Different inputs, different variables:** O(a + b), not O(n)

### Common Patterns

| Pattern | Complexity |
|---------|------------|
| Single loop (0 to n) | O(n) |
| Nested loops (both 0 to n) | O(n²) |
| Loop halving each iteration | O(log n) |
| Recursion (2 branches, depth n) | O(2ⁿ) |
| Divide and conquer (merge sort) | O(n log n) |

---

## Space Complexity

| Type | Example | Space |
|------|---------|-------|
| In-place | Swap sort | O(1) |
| Linear auxiliary | Merge sort temp array | O(n) |
| Recursion stack | DFS depth d | O(d) |
| Full copy | Clone array | O(n) |

---

## Amortized Analysis

**Average cost per operation over time**

Example: Dynamic array (ArrayList)
- Most appends: O(1)
- Occasional resize: O(n)
- Amortized: O(1) per append

---

## Tips for Interviews

1. Always state your assumptions
2. Analyze both time AND space
3. Consider average vs worst case
4. Mention trade-offs when relevant
