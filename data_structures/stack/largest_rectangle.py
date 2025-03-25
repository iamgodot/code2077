# Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/


def largest_rectangle_area(heights: list[int]) -> int:
    """
    1. Use brute-force to traverse each position and calculate the max length.

    Time: O(n^2)
    Space: O(1)

    2. Use 2 mono stacks to find the last/next smaller element for the max length.

    Time: O(n)
    Space: O(n)
    """
    n = len(heights)
    # NOTE: initial values
    lefts = [-1] * n
    rights = [n] * n

    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            lefts[i] = stack[-1]
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            rights[i] = stack[-1]
        stack.append(i)

    return max([heights[i] * (rights[i] - lefts[i] - 1) for i in range(n)])


def largest_rectangle_area2(heights: list[int]) -> int:
    """
    We can also use 1 mono stack to find both the left and right boundaries.

    Time: O(n)
    Space: O(n)
    """
    n = len(heights)
    lefts = [-1] * n
    rights = [n] * n

    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            # NOTE: Here we can update the next smaller element
            rights[stack[-1]] = i
            stack.pop()
        if stack:
            lefts[i] = stack[-1]
        stack.append(i)

    return max([heights[i] * (rights[i] - lefts[i] - 1) for i in range(n)])


if __name__ == "__main__":
    for func in [largest_rectangle_area, largest_rectangle_area2]:
        assert func([2, 1, 5, 6, 2, 3]) == 10
        assert func([2, 1, 2]) == 3
