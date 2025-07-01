# Insert Interval
# https://leetcode.com/problems/insert-interval/


def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    """
    Traverse all the intervals:
        1. If the current interval ends before the new interval begins, or if it begins after new interval ends, then they do not overlap and we can append the current interval to merged.
        2. Otherwise, they do overlap, and we merge them by updating the start of the previous interval if it is greater than the start of the current interval.
        3. If there's no intervals put after the new interval, we need to append the new interval after the loop.

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
            right = max(right, j)
    if not insert_merge:
        res.append([left, right])
    return res


# Merge Intervals
# https://leetcode.com/problems/merge-intervals/


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """
    First, we sort the list by their start values.
    Then, we insert the first interval into our merged list and continue considering each interval in turn as follows:
        1. If the current interval begins after the previous interval ends, then they do not overlap and we can append the current interval to merged.
        2. Otherwise, they do overlap, and we merge them by updating the end of the previous interval if it is less than the end of the current interval.

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


# Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/


def erase(intervals: list[list[int]]) -> int:
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
