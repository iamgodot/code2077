# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    对于重叠的区间，更新两端的范围，
    在第一个右侧不重叠区间出现后，先插入合并的区间。

    Time: O(n)
    Space: O(1)
    """
    res = []
    left, right = newInterval
    insert_merge = False
    for i, j in intervals:
        if j < left:
            res.append([i, j])
        elif i > right:
            if not insert_merge:
                res.append([left, right])
                insert_merge = True
            res.append([i, j])
        else:
            left = min(left, i)
            right = min(right, j)
    if not insert_merge:
        res.append([left, right])
    return res


# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    一开始要先排序，默认会按照先左后右的顺序。

    Time: O(nlogn)
    Space: O(logn)
    """
    intervals.sort()
    res = []
    for interval in intervals:
        if not res or interval[0] > res[-1][1]:
            res.append(interval)
        else:
            res[-1][1] = max(interval[1], res[-1][1])
    return res


# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。


def erase(intervals: List[List[int]]) -> int:
    """
    转化为求非重叠区间的最大数量，然后用区间总数减去即可得到结果。
    首先排序区间，以右边界为准，从小到大；
    从最左边开始，寻找右边界最靠左的区间，然后以该区间为准，寻找下一个
    不重叠的右边界最靠左的区间，依次类推。
    最终的区间个数就是非重叠区间的最大数量。

    Time: O(nlogn)
    Space: O(logn)
    """
    intervals.sort(key=lambda x: x[1])
    count, bound = 0, -float("inf")
    for interval in intervals:
        if interval[0] >= bound:
            count += 1
            bound = interval[1]

    return len(intervals) - count


if __name__ == "__main__":
    assert erase([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert erase([[1, 2], [1, 2], [1, 2]]) == 2
    assert erase([[1, 2], [2, 3]]) == 0
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
