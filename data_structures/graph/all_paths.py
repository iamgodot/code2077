# All Paths From Source to Target
# https://leetcode.com/problems/all-paths-from-source-to-target/


def all_paths(graph: list[list[int]]) -> list[list[int]]:
    def dfs(index):
        path.append(index)
        if len(graph) == index + 1:
            res.append(path[:])
        for nb in graph[index]:
            dfs(nb)
        path.pop()

    res, path = [], []
    dfs(0)
    return res


if __name__ == "__main__":
    assert all_paths([[1, 2], [3], [3], []]) == [[0, 1, 3], [0, 2, 3]]
