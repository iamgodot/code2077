# Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/description/


def min_meeting_rooms(intervals: list[list[int]]) -> int:
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
