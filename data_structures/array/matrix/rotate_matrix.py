# Rotate Image
# https://leetcode.com/problems/rotate-image/


def rotate(matrix) -> None:
    """
    Time: O(n^2)
    Space: O(1)
    """
    if not matrix:
        return

    n = len(matrix)
    for row in range(n // 2):
        for column in range((n + 1) // 2):
            # find next three points
            # (row, column) -> (column, n-1-row) -> (n-1-row, n-1-column) -> (n-1-column, row)
            point1 = matrix[row][column]
            point2 = matrix[column][n - 1 - row]
            point3 = matrix[n - 1 - row][n - 1 - column]
            point4 = matrix[n - 1 - column][row]
            # swap four points
            (
                matrix[column][n - 1 - row],
                matrix[n - 1 - row][n - 1 - column],
                matrix[n - 1 - column][row],
                matrix[row][column],
            ) = (point1, point2, point3, point4)

    return matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(matrix)
    assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    matrix = [[1]]
    rotate(matrix)
    assert matrix == [[1]]
    matrix = [[1, 2], [3, 4]]
    rotate(matrix)
    assert matrix == [[3, 1], [4, 2]]
