# Course Schedule
# https://leetcode.com/problems/course-schedule/description/


def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    Calculate edges and degrees.
    Create a queue and push in 0-degree points.
    Iterate the queue by poping and pushing:
        1. Pop one point and update degrees based on its edges
        2. Put the point in the result list
        3. Push any new 0-degree points into the queue.
    When the queue is empty, check if the result list includes all courses.

    Time: O(m+n) where m is number of edges and n is number of nodes
    Space: O(m+n)
    """

    from collections import defaultdict, deque

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
