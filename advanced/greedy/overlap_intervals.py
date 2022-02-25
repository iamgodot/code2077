# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。


from typing import List


def erase(intervals: List[List[int]]) -> int:
    """
    转化为求非重叠区间的最大数量，然后用区间总数减去即可得到结果。
    首先排序区间，以右边界为准，从小到大；
    从最左边开始，寻找右边界最靠左的区间，然后以该区间为准，寻找下一个
    不重叠的右边界最靠左的区间，依次类推。
    最终的区间个数就是非重叠区间的最大数量。
    """
    intervals.sort(key=lambda x: x[1])
    count, bound = 0, -float("inf")
    for interval in intervals:
        if interval[0] >= bound:
            count += 1
            bound = interval[1]

    return len(intervals) - count


# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Sort intervals by right bound of each interval.
    Iterate sorted intervals:
        If overlapped, go to next, otherwise merge previous ones and start again.
    """
    intervals.sort()
    start, end = intervals[0]
    res = []
    for interval in intervals[1:]:
        # Overlapped
        if interval[0] <= end:
            end = max(end, interval[1])
        else:
            res.append([start, end])
            start, end = interval

    res.append([start, end])
    return res


if __name__ == "__main__":
    assert erase([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert erase([[1, 2], [1, 2], [1, 2]]) == 2
    assert erase([[1, 2], [2, 3]]) == 0
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
