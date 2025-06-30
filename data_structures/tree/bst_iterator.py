# Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/description/

from data_structures.tree import TreeNode


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.push_all_left(root)

    def next(self) -> int:
        if self.stack:
            cur = self.stack.pop()
            self.push_all_left(cur.right)
            return cur.val

    def push_all_left(self, node) -> None:
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self) -> bool:
        return len(self.stack) > 0
