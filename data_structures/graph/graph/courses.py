# 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。

# 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
# 返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。


from collections import defaultdict, deque
from typing import List


# 关键词：拓扑排序、入度
# 时间复杂度和空间复杂度都是 O(m+n) 也就是点（课程）和边（依赖关系）的和
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Calculate edges and degrees.
    Create a queue and push in 0-degree points.
    Iterate the queue by poping and pushing:
        1. Pop one point and update degrees based on its edges
        2. Put the point in the result list
        3. Push any new 0-degree points into the queue.
    When the queue is empty, check if the result list includes all courses.
    """

    edges = defaultdict(list)
    degrees = [0 for _ in range(numCourses)]
    dq = deque()
    res = []

    for re in prerequisites:
        edges[re[1]].append(re[0])
        degrees[re[0]] += 1

    for course, degree in enumerate(degrees):
        if not degree:
            dq.appendleft(course)

    while dq:
        course = dq.pop()
        for i in edges[course]:
            degrees[i] -= 1
            if degrees[i] == 0:
                dq.appendleft(i)
        res.append(course)

    return res if len(res) == numCourses else []
