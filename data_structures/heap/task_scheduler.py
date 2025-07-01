# Task Scheduler
# https://leetcode.com/problems/task-scheduler/


def leastInterval(tasks: list[str], n: int) -> int:
    """
    For each cycle, we either have enough tasks to fill in the slots or not,
    which is why we maintain task_count when idle time is needed.

    Time: O(n * logk) where k is 26
    Space: O(k)
    """
    from collections import Counter

    counter = Counter(tasks)
    pq = [-freq for _, freq in counter.items()]
    from heapq import heapify, heappush, heappop

    heapify(pq)
    time = 0
    while pq:
        cycle = n + 1
        store = []
        task_count = 0
        while cycle > 0 and pq:
            freq = heappop(pq)
            if freq + 1 < 0:
                store.append(freq + 1)
            task_count += 1
            cycle -= 1
        for x in store:
            heappush(pq, x)
        time += task_count if not pq else n + 1
    return time
