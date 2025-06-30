# Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

from data_structures.tree import TreeNode


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Time: O(n)
    Space: O(h)
    """
    if not root or root is p or root is q:
        return root

    ancestor_left = lowest_common_ancestor(root.left, p, q)
    ancestor_right = lowest_common_ancestor(root.right, p, q)

    if ancestor_left and ancestor_right:
        return root
    else:
        return ancestor_left or ancestor_right


# Lowest Common Ancestor of a Binary Tree II
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/description/


def lowest_common_ancestor2(
    root: TreeNode, p: TreeNode, q: TreeNode
) -> TreeNode | None:
    exist_p = exist_q = False

    def traverse(node, p, q):
        if not node:
            return None
        # NOTE: here we have to do recursion first to validate
        # the exsistence of all the child nodes
        left = traverse(node.left, p, q)
        right = traverse(node.right, p, q)
        nonlocal exist_p, exist_q
        if node.val == p.val:
            exist_p = True
            return node
        if node.val == q.val:
            exist_q = True
            return node

        if left and right:
            return node
        else:
            return left or right

    res = traverse(root, p, q)
    return res if exist_p and exist_q else None


# Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/


def lowest_common_ancestor_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    We can use while loop to reduce the space complexity to O(1).

    Time: O(h), O(n) in the worst case
    Space: O(1)
    """
    ancestor = root
    while ancestor:
        if p.val < ancestor.val and q.val < ancestor.val:
            ancestor = ancestor.left
        elif p.val > ancestor.val and q.val > ancestor.val:
            ancestor = ancestor.right
        else:
            break
    return ancestor


if __name__ == "__main__":
    root = TreeNode(
        val=3,
        left=TreeNode(
            val=5,
            left=TreeNode(6),
            right=TreeNode(2, left=TreeNode(7), right=TreeNode(4)),
        ),
        right=TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(8)),
    )
    node = lowest_common_ancestor(root, TreeNode(5), TreeNode(1))
    print(node.val)
