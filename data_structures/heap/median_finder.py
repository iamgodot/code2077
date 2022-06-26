# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

# 例如，

# [2,3,4] 的中位数是 3

# [2,3] 的中位数是 (2 + 3) / 2 = 2.5

# 设计一个支持以下两种操作的数据结构：

# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。


import heapq


# 利用两个堆来维护中位数，注意大顶堆要取负数
# 时间复杂度 add 操作 O(logn) find 操作 O(1)
# 空间复杂度 O(n)
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.hq1 = []  # 较大的一半，小顶堆
        self.hq2 = []  # 较小的一半，大顶堆

    def addNum(self, num: int) -> None:
        if len(self.hq1) == len(self.hq2):
            heapq.heappush(self.hq1, -heapq.heappushpop(self.hq2, -num))
        else:
            heapq.heappush(self.hq2, -heapq.heappushpop(self.hq1, num))

    def findMedian(self) -> float:
        return (
            self.hq1[0]
            if len(self.hq1) > len(self.hq2)
            else (self.hq1[0] - self.hq2[0]) / 2
        )


# 进阶 1
# 如果数据流中所有整数都在 00 到 100100 范围内，那么我们可以利用计数排序统计每一类数的数量，并使用双指针维护中位数。

# 进阶 2
# 如果数据流中 99\%99% 的整数都在 00 到 100100 范围内，那么我们依然利用计数排序统计每一类数的数量，并使用双指针维护中位数。对于超出范围的数，我们可以单独进行处理，建立两个数组，分别记录小于 00 的部分的数的数量和大于 100100 的部分的数的数量即可。当小部分时间，中位数不落在区间 [0,100][0,100] 中时，我们在对应的数组中暴力检查即可。
