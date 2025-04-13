# Combination Sum
# https://leetcode.com/problems/combination-sum/description/


def combination_sum1(candidates: list, target: int) -> list:
    """
    Time: O(n*2^n)
    Space: O(n)
    """

    length = len(candidates)
    res, path = [], []

    def bt(start) -> None:
        sum_ = sum(path)
        if sum_ == target:
            res.append(path.copy())
            return
        for i in range(start, length):
            num = candidates[i]
            if num > target - sum_:
                return
            path.append(num)
            bt(i)  # NOTE: use i instead of i+1 since we can reuse elements
            path.pop()

    # NOTE: if smaller elements are after larger ones, we might miss some combinations
    candidates.sort()
    bt(0)
    return res


# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。
# 注意：解集不能包含重复的组合。


# 时间复杂度：O(n*2^n) 其中 n 作为 candidates 的长度，对每个元素来说，都面临 n 次选或不选的判断，所以这是一个比较宽松的上界
# 空间复杂度：O(n)
def combination_sum2(candidates: list, target: int) -> list:
    def bt(start) -> None:
        sum_ = sum(path)
        if sum_ == target:
            res.append(path.copy())
            return
        for i in range(start, len(candidates)):
            num = candidates[i]
            # 剪枝
            if num > target - sum_:
                return
            # 注意是 start
            if i > start and num == candidates[i - 1]:
                continue
            # 回溯三部曲：操作 -> 递归 -> 撤销
            path.append(num)
            bt(i + 1)  # 每个数字只能使用一次，所以递归时 i 要 +1
            path.pop()

    # 这里必须排序，因为如果值小的元素在后面，会造成答案丢失，因为遍历时只会考虑当前元素及后面的元素
    candidates.sort()
    res, path = [], []
    bt(0)
    return res


# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 说明：
# 所有数字都是正整数。
# 解集不能包含重复的组合。


# 时间复杂度：O(c(9, k)*k)
# 空间复杂度：O(9) -> O(1)
def combination_sum3(k: int, n: int) -> list:
    def bt(k, n, start) -> None:
        length, total = len(path), sum(path)
        if total > n:
            return
        if total == n and length == k:
            res.append(path.copy())
            return
        for i in range(start, 9 - (k - length) + 1):
            path.append(i + 1)
            bt(k, n, i + 1)
            path.pop()

    res, path = [], []
    bt(k, n, 0)
    return res


if __name__ == "__main__":
    assert combination_sum1([2, 3, 6, 7], 7) == sorted([[7], [2, 2, 3]])
    assert combination_sum2([10, 1, 2, 7, 6, 1, 5], 8) == [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6],
    ]
    assert combination_sum3(3, 7) == [[1, 2, 4]]
    assert combination_sum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
