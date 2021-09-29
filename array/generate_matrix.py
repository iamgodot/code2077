# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。


# 时间复杂度 O(n^2)
def generate_matrix(n: int) -> list:
    matrix = [[0 for i in range(n)] for i in range(n)]
    number = 1
    left, right, up, down = 0, n - 1, 0, n - 1

    while left < right and up < down:
        for i in range(left, right):
            matrix[up][i] = number
            number += 1

        for i in range(up, down):
            matrix[i][right] = number
            number += 1

        for i in range(right, left, -1):
            matrix[down][i] = number
            number += 1

        for i in range(down, up, -1):
            matrix[i][left] = number
            number += 1

        left += 1
        right -= 1
        up += 1
        down -= 1

    if n % 2:
        matrix[n // 2][n // 2] = number

    return matrix


if __name__ == '__main__':
    assert generate_matrix(0) == []
    assert generate_matrix(1) == [[1]]
    assert generate_matrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert generate_matrix(4) == [[1, 2, 3, 4], [12, 13, 14, 5],
                                  [11, 16, 15, 6], [10, 9, 8, 7]]  # noqa
