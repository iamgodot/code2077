# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。


# 时间复杂度：O(n*n!)
# 空间复杂度：O(n*n!)
def permute(nums: list) -> list:
    length = len(nums)

    def bt(used):
        if len(path) == length:
            res.append(path[:])
            return
        for i in range(length):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            bt(used)
            used[i] = False
            path.pop()

    res, path = [], []
    bt([False] * length)
    return res


# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。


def permute_unique(nums: list) -> list:
    length = len(nums)

    def bt(used):
        if len(path) == length:
            res.append(path[:])
            return
        for i in range(length):
            if not used[i]:
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                path.append(nums[i])
                used[i] = True
                bt(used)
                used[i] = False
                path.pop()

    nums.sort()  # 因为要对重复数字进行剪枝所以排序
    res, path = [], []
    bt([False] * length)
    return res


if __name__ == "__main__":
    assert permute([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert permute([0, 1]) == [[0, 1], [1, 0]]
    assert permute([1]) == [[1]]
    assert permute_unique([1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert permute_unique([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
