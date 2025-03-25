# Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/description/


# 1. Brute force 直接暴力解法时间复杂度会达到 O(n*k)
# 2. 使用最大堆，这样每次直接取堆顶元素就可以得到最大值，遍历过程中先看滑走的是不是堆顶元素，再把新元素加入
# 到堆中，这样每次插入堆需要 O(logn) 的时间，最坏情况下的时间复杂就是 O(n*logn)，而空间复杂度显然是 O(n)
def max_sliding_window_with_heap(nums: list, k: int) -> list:
    """
    因为需要确定滑出元素，所以保存在堆中的结构是 <value, index>.
    另外 Python 默认的是最小堆，所以需要保存 value 的负值
    """
    import heapq

    heap = [(-nums[i], i) for i in range(k)]
    heapq.heapify(heap)
    res = [-heap[0][0]]

    for i in range(k, len(nums)):
        if heap[0][1] == i - k:
            heapq.heappop(heap)
        heapq.heappush(heap, (-nums[i], i))
        res.append(-heap[0][0])

    return res


# 3. 维护一个单调递减的双向队列，在线性的遍历过程中，此队列的队首永远是窗口的最大值，这样就可以 O(1) 获取结果
# 在维护过程中，为了保证队首最大，所以新元素要不断地与队尾元素做比较，直到找到更大的再加入队尾（但是一定要加入，因为有成为首领的希望）。
# 而比较过程中，小于新元素的队尾元素可以直接舍弃，因为有新元素在右侧顶着，所以不必担心会用到（留你何用）。
# 如果两者相同，那么就都要留着，因为窗口是滑动的，不能滑走旧的连新的也没了。
# 此时可以达到 O(n) 的时间复杂度，以及 O(k) 的空间复杂度。
# 其实不一定要用 deque，list 也可以完成同样的操作。
def max_sliding_window_with_deque(nums: list, k: int) -> list:
    from collections import deque

    dq, res = deque(), []

    for num in nums[:k]:
        while dq and dq[-1] < num:
            dq.pop()
        dq.append(num)

    res.append(dq[0])

    for i in range(len(nums) - k):
        if dq[0] == nums[i]:
            dq.popleft()

        while dq and dq[-1] < nums[i + k]:
            dq.pop()
        dq.append(nums[i + k])
        res.append(dq[0])

    return res


if __name__ == "__main__":
    for nums, k, res in ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]), (
        [-7, -8, 7, 5, 7, 1, 6, 0],
        4,
        [7, 7, 7, 7, 7],
    ):
        assert max_sliding_window_with_deque(nums, k) == res
        assert max_sliding_window_with_heap(nums, k) == res
