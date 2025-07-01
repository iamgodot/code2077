# Binary Search

Binary seearch is an efficient search algorithm based on the divide-and-conquer strategy.

Given a list of elements in sorted order, it can significantly reduce the search times by halving the search range in each iteration, until the target element is found or the search interval becomes empty.

- Time complexity: O(logn)
- Space complexity: O(1)

Be careful with the suitable conditions for binary search:

1. Elements need to be sorted
2. Elements need to be array-based instead of linked-list-based
3. For smaller datasets, linear search is faster while binary search takes around 4-6 operations per iteration

## Implementation

### With no duplicates

```python
def bs(nums: list, target: int) -> int:
    res = -1
    left, right = 0, len(nums) - 1

    while left <= right:
        # Don't have to write left + (right-left)//2 in Python
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    # For the insertion index when target is not found, return left
    return res
```

### With duplicates

When there're duplicates, we usually want to find the leftmost or rightmost index of target.

For the leftmost index:

```python
def bs_left(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    if not 0 <= left <= len(nums) - 1:
        return -1
    return left if nums[left] == target else -1
```

For the rightmost index:

```python
def bs_right(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    # if not 0 <= left - 1 <= len(nums) - 1:
    if not 0 <= right <= len(nums) - 1:
        return -1
    # return left - 1 if nums[left - 1] == target else -1
    return right if nums[right] == target else -1
```

for bisect left or right, if target is larger than the largest, left will be len(nums) and right be len(nums) - 1; if target is smaller than the smallest, left will be 0 and right be -1.

if target doesn't exist, left will be index to insert it.

so after the search, we need to check for the boundary first, then check if the target is equal to the element at the index.

## Questions

1. [Find Minimum in Rotated Sorted Array](./rotated_array.py)
1. [Search in Rotated Sorted Array](./rotated_array.py)
1. [Find Peak Element](./find_peak_element.py)
