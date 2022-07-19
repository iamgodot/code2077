# 给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，返回 所需会议室的最小数量 。


from typing import List


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    模拟查找会议室的过程。
    如果堆中有已经结束的会议，那么直接复用，同时替换原有结束时间为最新；
    否则增加会议室，同时插入新的结束时间。

    Time: O(nlogn)
    Space: O(n) for heap
    """
    import heapq

    res = 0
    end_times = []
    intervals.sort()
    for interval in intervals:
        if not end_times or interval[0] < end_times[0]:
            res += 1
            heapq.heappush(end_times, interval[1])
        else:
            heapq.heappushpop(end_times, interval[1])
    return res
