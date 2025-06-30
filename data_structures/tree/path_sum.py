# Path Sum
# https://leetcode.com/problems/path-sum/description/


def has_path_sum(root: TreeNode, target_sum: int) -> bool:
    """
    Time: O(n)
    Space: O(h)
    """
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target_sum
    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(
        root.right, target_sum - root.val
    )


# Path Sum II
# https://leetcode.com/problems/path-sum-ii/description/


def path_sum(root: TreeNode, target_sum: int) -> list[list[int]]:
    """
    Time: O(n^2)
    Space: O(n)
    """

    def dfs(node: TreeNode, target: int) -> None:
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right and node.val == target:
            res.append(path[:])
        dfs(node.left, target - node.val)
        dfs(node.right, target - node.val)
        path.pop()

    path, res = [], []
    dfs(root, target_sum)
    return res


# Path Sum III
# https://leetcode.com/problems/path-sum-iii/description/


def path_sum2(root: TreeNode, target_sum: int) -> int:
    """
    Time: O(n^2)
    Space: O(n)
    """

    def dfs(node, target) -> int:
        if not node:
            return 0
        res = 0
        if node.val == target:
            res += 1
        return (
            res + dfs(node.left, target - node.val) + dfs(node.right, target - node.val)
        )

    if not root:
        return 0
    res = dfs(root, target_sum)
    return res + path_sum2(root.left, target_sum) + path_sum2(root.right, target_sum)


def path_sum3(root: TreeNode, target_sum: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """

    def dfs(node, total) -> int:
        if not node:
            return 0
        total += node.val
        res = prefix_sum[total - target_sum]
        prefix_sum[total] += 1
        res += dfs(node.left, total)
        res += dfs(node.right, total)
        prefix_sum[total] -= 1
        return res

    from collections import defaultdict

    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1
    return dfs(root, 0)
