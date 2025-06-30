# Flood Fill
# https://leetcode.com/problems/flood-fill/description/


def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    """
    Could do either DFS or BFS.

    Time: O(m*n)
    Space: O(1)
    """
    rows, cols = len(image), len(image[0])
    color_orig = image[sr][sc]
    # NOTE: if color_orig == color, we'll get infinite recursion
    if color_orig == color:
        return image

    def traverse(i, j):
        if 0 <= i < rows and 0 <= j < cols and image[i][j] == color_orig:
            image[i][j] = color
            traverse(i - 1, j)
            traverse(i + 1, j)
            traverse(i, j - 1)
            traverse(i, j + 1)

    traverse(sr, sc)
    return image
