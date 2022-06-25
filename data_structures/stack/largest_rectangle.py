# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。


from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    """
    暴力解法可以遍历每个位置，然后计算左右可以延伸的最大长度。
    Time: O(n^2)
    Space: O(1)

    也使用单调栈分别找出 last 和 next smaller element 来确认延伸长度。
    Time: O(n)
    Space: O(n)
    """
    n = len(heights)
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


def largest_rectangle_area2(heights: List[int]) -> int:
    """
    在单调栈的基础上，可以只进行一次遍历。
    Time: O(n)
    Space: O(n)
    """
    n = len(heights)
    lefts = [-1] * n
    # 注意遍历完成之后 rights 可能有未更新的部分，所以提前初始化为 n
    rights = [n] * n

    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            # 这里在 pop 之前可以巧妙地更新 next smaller element
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
