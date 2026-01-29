# Algorithm Patterns Reference

Common algorithm patterns with templates and examples.

## Sorting Algorithms

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space | Stable |
|-----------|-------------|------------|--------------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

---

## Searching Algorithms

### Linear Search
```python
def linear_search(arr, target):  # O(n)
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

### Binary Search (Iterative)
```python
def binary_search(arr, target):  # O(log n)
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

## Graph Algorithms

### BFS (Breadth-First Search)
```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result
```
**Use for:** Shortest path (unweighted), level-order traversal

### DFS (Depth-First Search)
```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result
```
**Use for:** Cycle detection, topological sort, connected components

### Dijkstra's Algorithm
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        curr_dist, node = heapq.heappop(pq)
        if curr_dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances
```
**Use for:** Shortest path (weighted, non-negative)

---

## Dynamic Programming Patterns

### Fibonacci (Memoization)
```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

### Fibonacci (Tabulation)
```python
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

### Common DP Problems

| Problem | State | Recurrence |
|---------|-------|------------|
| Fibonacci | dp[i] = i-th fib | dp[i] = dp[i-1] + dp[i-2] |
| Climbing Stairs | dp[i] = ways to reach i | dp[i] = dp[i-1] + dp[i-2] |
| Coin Change | dp[i] = min coins for i | dp[i] = min(dp[i-c]) + 1 |
| Longest Common Subsequence | dp[i][j] = LCS of s1[:i], s2[:j] | dp[i][j] = dp[i-1][j-1]+1 or max(...) |
| 0/1 Knapsack | dp[i][w] = max value | dp[i][w] = max(skip, take) |

---

## Two Pointers Pattern

```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

---

## Sliding Window Pattern

```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```
