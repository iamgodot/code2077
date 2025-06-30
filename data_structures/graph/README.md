# Graph

## Representation

- Adjacency matrix: cell values as weights
  - Pros: quick access
  - Cons: extra space
- Adjacency list: every node has a list of tuples (node, weight)
  - Pros: space-saving, efficient for edge processing
  - Cons: slow access
- Hash tables: every node has a hash table of connected nodes and edge weights
  - Pros: flexible, quick lookups
  - Cons: slightly more overhead compared to adjacency list

## Searching

**Remember to check if we can modify the graph in-place, otherwise create a copy of it.**

### DFS

```python
def dfs(matrix):
    if not matrix:
        return

    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def traverse(i, j):
        if (i, j) in visited:
            return
        visited.add((i, j))

        # NOTE: add relevant modifications

        for direction in directions:
            i_next, j_next = i + direction[0], j + direction[1]
            # NOTE: if checking out-of-boundary, use continue instead of return
            if 0 <= i_next < rows and 0 <= j_next < cols: # NOTE: add relevant checks
                traverse(i_next, j_next)

    for i in range(rows):
        for j in range(cols):
            traverse(i, j)
```

If we're updating the cell values, there's no need to use a visited set:

```python
def dfs(matrix):
    # WARNING: if updated value could be the same as original, add a check here to return early, see flood fill
    rows, cols = len(matrix), len(matrix[0])

    def traverse(i, j):
        if 0 <= i < rows and 0 <= j < cols: # NOTE: add relevant checks
            matrix[i][j] = "new value"
            traverse(i - 1, j)
            traverse(i + 1, j)
            traverse(i, j - 1)
            traverse(i, j + 1)

    for i in range(rows):
        for j in range(cols):
            traverse(i, j)
```

Could be multi-source DFS.

### BFS

```python
def bfs(matrix):
    if not matrix:
        return

    rows, cols = len(matrix), len(matrix[0])
    from collections import deque
    queue = deque()

    # NOTE: if need multiple starting points, add their coordinates here(maybe step too)

    # for i in range(rows):
        # for j in range(cols):
            # queue.appendleft((i, j, 0))

    queue.appendleft((0, 0))
    visited[node] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        row, col = queue.pop()

        # NOTE: if need to maintain levels, use a for loop here

        # for i in range(len(queue)):
             # ...
        # step += 1

        for direction in directions:
            row_next, col_next = row + direction[0], col + direction[1]
            if 0 <= row_next < rows and 0 <= col_next < cols and (row_next, col_next) not in visited:
                # NOTE: if we update cell values, there's no need to use a visited set, same as dfs
                queue.appendleft((row_next, col_next))
                visited.add((row_next, col_next))
    return matrix
```

**For multi-source BFS, probably no need to maintain levels.**

### Complexity

- Time: O(n)
- Space: O(n)

**For recursive DFS, remember the risk of stack overflow.**

### Corner cases

- Empty graph
- Graph with one or two nodes
- Disconnected graphs
- Graph with cycles

## Questions

- DFS
  - [Flood Fill](flood_fill.py)
  - [Number of Islands](num_island.py)
  - [Clone Graph](clone_graph.py)
  - [Max Area of Island](max_area.py)
  - [Island Perimeter](perimeter.py)
  - [Making A Large Island](largest_island.py)
  - [Surrounded Regions](surrounded_regions.py)
  - [All Paths From Source to Target](all_paths.py)
  - [Evaluate Division](eval_division.py)
- BFS
  - [Walls and Gates](walls_and_gates.py)
  - [Rotting Oranges](rotting_oranges.py)
  - [Is Graph Bipartite?](bipartite.py)
  - [Word Ladder](word_ladder.py)
- Topological sort
  - [Course Schedule I && II](courses.py)
  - [Minimum Height Trees](min_height_trees.py)

## Tips

1. Ask if the input grid is modifiable
2. Check if grid values are integer or string
3. For using a visited set, remember to add nodes to it
