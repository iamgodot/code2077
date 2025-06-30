# Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/description/

from data_structures.tree import TreeNode
from data_structures.tree.traversal import levelorder


def num_of_bst(n: int) -> int:
    """
    定义 dp[i] 为 i 个数对应的互不相同的 BST 的个数。

    当 i 为 3 时，1,2,3 分别作为根节点，两边的组合总数加起来就是最终结果：

    dp[3] = dp[0] * dp[2] + dp[1] * dp[1] + dp[2] * dp[0]

    所以 dp[i] 是从 0~i-1 所有的子 dp 乘积的和得到的。

    初始化：dp[0] 应当为 1
    """
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    return dp[-1]


# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。


def generate_trees(n: int) -> list[TreeNode]:
    def build(left, right) -> list[TreeNode]:
        if left > right:
            return [None]
        res = []
        for i in range(left, right + 1):
            for child_left in build(left, i - 1):
                for child_right in build(i + 1, right):
                    root = TreeNode(i)
                    root.left = child_left
                    root.right = child_right
                    res.append(root)
        return res

    return build(1, n)


if __name__ == "__main__":
    assert num_of_bst(3) == 5
    trees = generate_trees(3)
    assert [levelorder(tree) for tree in trees] == [
        [[1], [2], [3]],
        [[1], [3], [2]],
        [[2], [1, 3]],
        [[3], [1], [2]],
        [[3], [2], [1]],
    ]
