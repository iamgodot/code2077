# 堆

- [第 k 大的数](algorithms/search/top_k/kth_largest.py)
- [前 k 小个数](algorithms/search/top_k/first_k_least.py)
- [前 k 的高频数](algorithms/search/top_k/top_k.py)
- [k 路归并](data_structures/linked_list/merge_k_lists.py)
- [设计推特](design_twitter.py)
- [数据流中位数](median_finder.py)

堆通常实现为一种完全二叉树（但并不一定），因为易于存储并且方便索引。

Heap 分为最大堆和最小堆两种，其中最大堆的根节点（堆顶）是整个堆中元素值最大的。对于 Heap 来说，最重要的特性就是每个节点的值都大于（小于）左右子节点的元素值。另外，Heap 一般通过数组而不是链表实现，在数组中，第一个元素代表根节点，下标为 k 的元素的左右子节点的下标分别为 2k + 1 和 2k + 2.

基于 Heap 的特点，优先级队列也分为两种：

1. 最大优先队列：基于最大堆，无论入队顺序如何，都是最大的元素先出队
2. 最小优先队列：基于最小堆，无论入队顺序如何，都是最小的元素先出队

其中入队和出队操作的时间复杂度都是 O(logn).

## 操作

Heap 主要有三种操作，分别是插入、删除和构建：

- 插入：在最后一个子节点的位置放置新元素（也就是数组最后的下标），然后根据元素值自底向上调整，也就是把大于父节点的子节点相互交换。插入操作的时间复杂度为 O(logn)
- 删除：把根节点的元素删除，并且替换为最后一个子节点，之后根据元素值从上到下进行调整。删除操作的时间复杂度也是 O(log)
- 构建：构建就是把一个无序的完全二叉树调整为二叉堆，本质上是从最后一个非叶子节点开始，把所有的非叶子节点依次做必要的下沉调整。整体的时间复杂度为 O(n)

## 排序

参考[这篇](https://aijishu.com/a/1060000000090217)。

- 时间复杂度：O(nlogn) 其中初始化建堆需要 O(n)
- 空间复杂度：O(1)

## Python

一般来说常用的堆默认是最大堆，而 Python 提供的 heapq 实现的是最小堆的结构。常用的接口如下：

- `heappush(heap: list, value)`: 插入新元素
- `heappop(heap: list)`: 弹出堆顶元素
- `heapify(heap: list)`: 把一个列表转换为 heap
- `heappushpop(heap: list, value)`: 先向 heap 插入一个新元素，再弹出新 heap 的堆顶元素
- `heapreplace(heap: list, value)`: 用新元素替换 heap 的堆顶元素
