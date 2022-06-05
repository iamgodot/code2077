# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

from data_structures.tree import TreeNode


# 需要自底向上回溯，因此通过递归调用的时候获取返回值，再对其进行判断
# 时间复杂度 O(n)，空间复杂度最坏情况下 O(n)
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root.val == p.val or root.val == q.val:
        return root

    # 这里递归的含义要明确：
    # 1. 若树里面存在p，也存在q，则返回他们的公共祖先。
    # 2. 若树里面只存在p，或只存在q，则返回存在的那一个。
    # 3. 若树里面既不存在p，也不存在q，则返回null。
    ancestor_left = lowest_common_ancestor(root.left, p, q)
    ancestor_right = lowest_common_ancestor(root.right, p, q)

    if ancestor_left and ancestor_right:
        return root
    elif ancestor_left:
        return ancestor_left
    elif ancestor_right:
        return ancestor_right
    else:
        return None


# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。


# 前序遍历，从上到下即可
# 时间复杂度 O(logn) 最坏情况下 O(n)
# 空间复杂度 O(logn) 最坏情况下 O(n)
def lowest_common_ancestor2(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root.val > p.val and root.val > q.val:
        return lowest_common_ancestor2(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return lowest_common_ancestor2(root.right, p, q)
    else:
        return root


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
