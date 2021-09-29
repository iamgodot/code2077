# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。


# 时间复杂度 O(m*n)
def spiral_order(matrix: list) -> list:
    res = []
    m = len(matrix)
    n = len(matrix[0]) if m else 0
    left, right, up, down = 0, n - 1, 0, m - 1

    while left < right and up < down:
        for i in range(left, right):
            res.append(matrix[up][i])

        for i in range(up, down):
            res.append(matrix[i][right])

        for i in range(right, left, -1):
            res.append(matrix[down][i])

        for i in range(down, up, -1):
            res.append(matrix[i][left])

        left += 1
        right -= 1
        up += 1
        down -= 1

    if left == right:
        res.extend([matrix[i][left] for i in range(up, down + 1)])
    elif up == down:
        res.extend(matrix[up][left:right + 1])

    return res


if __name__ == '__main__':
    assert spiral_order([]) == []
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert spiral_order(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert spiral_order(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
