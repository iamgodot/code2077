# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


# 1. BruteForce
# 2. 二分，这里没有直接对每行或每列二分
# 而是先从第一行和第一列找出边界，然后在边界内的小矩阵
# 对每行进行二分
# 时间复杂度 O(logm + logn + j*logi) 其中 i 是行边界，j 是列边界
def find_number(matrix: list, target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    def find_border(nums, target) -> int:
        i = j = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    n, m = len(matrix), len(matrix[0])
    row_first, column_first = matrix[0], [line[0] for line in matrix]
    j, i = find_border(column_first, target), find_border(row_first, target)

    if row_first[i - 1] == target or column_first[j - 1] == target:
        return True

    def bs(nums, target) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    # 这里没有检查 i j 的大小然后再对长度较大的进行二分
    # 因为如果对列二分，切片的时候对内存并不友好，会造成较高的成本
    for x in range(j):
        if bs(matrix[x][:i], target):
            return True

    return False


# 3. 可以从左下角或右上角直接进行线性搜索
# 时间复杂度 O(m+n)
def find_number2(matrix, target) -> bool:
    # 这里隐式检查了 matrix 的合理性
    i, j = len(matrix) - 1, 0
    while i >= 0 and j < len(matrix[0]):
        val = matrix[i][j]
        if val > target:
            i -= 1
        elif val < target:
            j += 1
        else:
            return True

    return False


if __name__ == "__main__":
    for method in [find_number, find_number2]:
        assert (
            method(
                [
                    [1, 4, 7, 11, 15],
                    [2, 5, 8, 12, 19],
                    [3, 6, 9, 16, 22],
                    [10, 13, 14, 17, 24],
                    [18, 21, 23, 26, 30],
                ],
                5,
            )
            is True
        )
        assert (
            method(
                [
                    [1, 4, 7, 11, 15],
                    [2, 5, 8, 12, 19],
                    [3, 6, 9, 16, 22],
                    [10, 13, 14, 17, 24],
                    [18, 21, 23, 26, 30],
                ],
                20,
            )
            is False
        )
