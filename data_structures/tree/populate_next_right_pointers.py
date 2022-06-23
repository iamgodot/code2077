# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

# 初始状态下，所有 next 指针都被设置为 NULL。


from typing import Optional


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


def connect(root: Optional[Node]) -> Optional[Node]:
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


def connect(root: Optional[Node]) -> Optional[Node]:
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


def connect(root: Node) -> Node:
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
