# Reorganize String
# https://leetcode.com/problems/reorganize-string/


def reorganizeString(s: str) -> str:
    """
    Each time we either pop out a different letter or need to pop a second time.

    Time: O(n * logk) where k is 26
    Space: O(k)
    """
    from collections import Counter
    from heapq import heapify, heappush, heappop

    counter = Counter(s)
    heap = [(-count, letter) for letter, count in counter.items()]
    heapify(heap)
    res = []
    while heap:
        count_most, letter_most = heappop(heap)
        if not res or letter_most != res[-1]:
            res.append(letter_most)
            if count_most + 1 < 0:
                heappush(heap, (count_most + 1, letter_most))
        else:
            if not heap:
                return ""
            count_second, letter_second = heappop(heap)
            res.append(letter_second)
            if count_second + 1 < 0:
                heappush(heap, (count_second + 1, letter_second))
            heappush(heap, (count_most, letter_most))
    return "".join(res)
