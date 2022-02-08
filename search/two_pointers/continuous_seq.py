# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

from typing import List


# 从 1,2 开始：如果和大于等于 target 则左指针右移；否则右指针右移。直到不满足 i < j 为止
# 时间复杂度 O(n)
def find_continuous_seq(target: int) -> List[List[int]]:
    res = []
    i, j, total = 1, 2, 3
    while i < j:
        if total == target:
            res.append([num for num in range(i, j + 1)])
        if total >= target:
            total -= i
            i += 1
        else:
            j += 1
            total += j

    return res


if __name__ == "__main__":
    assert find_continuous_seq(15) == [[1, 2, 3, 4, 5], [4, 5, 6], [7, 8]]
