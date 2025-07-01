# Heap

Heap is a complete binary tree. Usually when we refer a max heap as the heap, while Python's heapq implementation is min heap.

For a max heap, the root is always the largest element in the heap, while it's the opposite for a min heap. In general, heap is implemented as an array, and the first element is the root.

The main operations of a heap are insert, delete and build. The time complexity of insert and delete are O(logn), while the time complexity of build is O(n).

For heap sort, the time complexity is O(nlogn), and the space complexity is O(1).

More details [here](https://aijishu.com/a/1060000000090217).

## Python heapq

Python uses a min heap by default.

- `heappush(heap, value)`
- `heappop(heap)`
- `heapify(heap)`
- `heappushpop(heap, value)`
- `heapreplace(heap, value)`

## Questions

1. [K Closest Points to Origin]()
2. [Find Median from Data Stream](median_finder.py)
3. [Task Scheduler](task_scheduler.py)
4. [Reorganize String](reorganize_string.py)
5. [Kth Largest Element](algorithms/search/top_k/kth_largest.py)
6. [First K Least Elements](algorithms/search/top_k/first_k_least.py)
7. [Top K Frequent Elements](algorithms/search/top_k/top_k.py)
8. [Merge k Sorted Lists](data_structures/linked_list/merge.py)
9. [Design Twitter](design_twitter.py)
10. [Meeting Rooms](algorithms/greedy/meeting_rooms.py)
