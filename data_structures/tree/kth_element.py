from data_structures.tree import TreeNode


# Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/


def kth_smallest(root: TreeNode, k: int) -> int:
    """
    1. Traverse all the nodes then sort them, takes O(nlogn) time.
    2. Use a heap of size k and do a level traversal, takes O(nlogk) time.
    3. Inorder traversal, wen can do this either recursively or iteratively.

    Time: O(h+k)
    Space: O(h)

    Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

    We can store statistics for each node(how many nodes in its subtrees including itself) in a hash map, so search would take O(h) time(pre-couting takes O(n) time).
    We can also maintain a balanced BST, so search/insert/delete would all take O(logn) time.
    For space, we need O(n) to store all the nodes.
    """

    def traversal(node: TreeNode | None) -> None:
        if not node:
            return
        traversal(node.left)
        nonlocal k, res
        k -= 1
        if k == 0:
            res = node.val
            return
        traversal(node.right)

    res = -1
    traversal(root)
    return res


def kth_smallest2(root: TreeNode, k: int) -> int:
    stack = []
    cur = root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
    return -1


# Kth Largest Element in a BST


def kth_largest(root: TreeNode, k: int) -> int:
    def traversal(root) -> None:
        nonlocal res, k
        if not root:
            return
        traversal(root.right)
        k -= 1
        if k == 0:
            res = root.val
            return
        traversal(root.left)

    res = -1
    traversal(root)
    return res


def kth_largest_it(root, k) -> int:
    stack = []
    cur = root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.right
        else:
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.left
    return -1


if __name__ == "__main__":
    tree = TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4))
    assert kth_largest(tree, 2) == 3
    assert kth_smallest(tree, 2) == 2
