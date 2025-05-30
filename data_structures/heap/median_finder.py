""" 
There are many ways to find the median:

1. Keep a list and sort it every time to get the median
2. Keep a sorted list by inserting in the right position(located via binary search)
3. Use 2 heaps
4. Couting sort

Try to reason with the given requirements for time complexity of each operation.

"""

# Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/

from heapq import heappush, heappushpop


class MedianFinder:
    """
    Use two heaps to maintain the median.
    One should use negative numbers to simulate a max heap in Python.

    Time: O(logn) for add, O(1) for find
    Space: O(n)
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low_heap = []  # For the larger half of the numbers
        self.high_heap = []  # For the smaller half of the numbers

    def addNum(self, num: int) -> None:
        if len(self.low_heap) == len(self.high_heap):
            heappush(self.low_heap, -heappushpop(self.high_heap, -num))
        else:
            heappush(self.high_heap, -heappushpop(self.low_heap, num))

    def findMedian(self) -> float:
        return (
            self.low_heap[0]
            if len(self.low_heap) > len(self.high_heap)
            else (self.low_heap[0] + (-self.high_heap[0])) / 2
        )
