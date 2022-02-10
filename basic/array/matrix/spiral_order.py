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
        res.extend(matrix[up][left : right + 1])

    return res


# 一种很简洁的 Python 写法
def spiral_order2(self, matrix: List[List[int]]) -> List[int]:
    res = []
    while matrix:
        res += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]
    return res


# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 思路类似，时间复杂度 O(n^2)
def generate_matrix(n: int):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    left, right, up, down = 0, n - 1, 0, n - 1
    num = 1
    while left < right and up < down:
        for i in range(left, right):
            matrix[up][i] = num
            num += 1
        for j in range(up, down):
            matrix[j][right] = num
            num += 1
        for i in range(right, left, -1):
            matrix[down][i] = num
            num += 1
        for j in range(down, up, -1):
            matrix[j][left] = num
            num += 1
        left += 1
        right -= 1
        up += 1
        down -= 1

    if left == right and up == down:
        matrix[up][left] = num

    return matrix


if __name__ == "__main__":
    assert spiral_order([]) == []
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert spiral_order(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert spiral_order(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    assert generate_matrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert generate_matrix(1) == [[1]]
