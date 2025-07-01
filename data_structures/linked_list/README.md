# Linked List

## Techniques

### Reverse list

Can also be used to reverse k nodes, just remember to include k in the while loop.

### 2 pointers

Can be used to locate any point with a slow and a fast pointer.

If both pointers are initialized to head, the middle point might be on the right half of the list. So for it to be on the left half, you need to set `slow, fast = head, head.next`.

### Dummy node

A dummy node can be used to handle possible empty lists. Sometimes it's not necessary, such as [Reorder List](reorder.py).

### Clean cut

When linking nodes together, remember to clean cut to avoid cycles, such as [Partition List](partition.py) and [Odd Even Linked List](odd_even.py).

### Other

Sometimes a doubly linked list or hash map comes in handy.

## Questions

1. Basic operations
   1. [Design Linked List](design_linked_list.py)
   2. [Remove Linked List Elements](remove_elements.py)
   3. [Remove Duplicates from Sorted List I && II](remove_elements.py)
   4. [Remove Nth Node From End of List](remove_from_end.py)
2. Cycle
   1. [Linked List Cycle I && II](cycle.py)
   2. [Intersection of Two Linked Lists](intersection_node.py)
3. Reverse
   1. [Reverse Linked List I && II](reverse_list.py)
   2. [Swap Nodes in Pairs](swap_pairs.py)
   3. [Reverse Nodes in k-Group](reverse_k_group.py)
4. Restructure
   1. [Sort List](sort.py)
   2. [Merge Two Sorted Lists](merge.py)
   3. [Merge k Sorted Lists](merge.py)
   4. [Add Two Numbers I && II](add_two_numbers.py)
   5. [Rotate List](rotate.py)
   6. [Reorder List](reorder.py)
   7. [Partition List](partition.py)
   8. [Odd Even Linked List](odd_even.py)
5. Hash map
   1. [Copy List with Random Pointer](copy_random_list.py)
   2. [LRU Cache](lru.py)
   3. [LFU Cache](lfu.py)
