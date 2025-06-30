# Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: Node | None) -> Node | None:
    """
    通用解法，不论是二叉树是否完美。
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return None
    from collections import deque

    dq = deque([root])
    while dq:
        length = len(dq)
        for i in range(length):
            node = dq.pop()
            if i < length - 1:
                node.next = dq[-1]
            if node.left:
                dq.appendleft(node.left)
            if node.right:
                dq.appendleft(node.right)
    return root


def connect2(root: Node | None) -> Node | None:
    """
    外层循环遍历每一层，内层循环遍历每层的所有节点。
    Time: O(n)
    Space: O(1)
    """
    if not root:
        return None
    level = root
    while level.left:  # 因为是完美二叉树，所以 level.left 可以判断是否存在下一层
        leftmost = level
        while leftmost:
            leftmost.left.next = leftmost.right
            if leftmost.next:
                leftmost.right.next = leftmost.next.left
            leftmost = leftmost.next
        level = level.left
    return root


# 给定一个二叉树，其余条件同上


def connect3(root: Node | None) -> Node | None:
    """
    基本思路同上，但因为不是完美二叉树所以在横向遍历时需要虚拟头节点。
    Time: O(n)
    Space: O(1)
    """
    if not root:
        return None
    level = root
    while level:  # 这里就不能用 level.left
        leftmost = level
        dummy = cur = Node()
        while leftmost:
            if leftmost.left:
                cur.next = leftmost.left
                cur = cur.next
            if leftmost.right:
                cur.next = leftmost.right
                cur = cur.next
            leftmost = leftmost.next
        level = dummy.next
    return root
