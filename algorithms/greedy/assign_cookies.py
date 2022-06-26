# 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
# 对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。


from typing import List


def assign(g: List[int], s: List[int]) -> int:
    """
    从最小尺寸的饼干开始，尽量满足胃口最小的孩子，以此类推。
    需要对两个列表排序，并且遍历饼干列表，过程中从胃口最小的孩子开始查找
    时间复杂度 O(m+n) 空间复杂度 O(1)
    """
    g.sort()
    s.sort()
    index = 0
    num_of_kids = len(g)
    for cookie in s:
        if index < num_of_kids and cookie >= g[index]:
            index += 1

    return index


if __name__ == "__main__":
    assert assign([1, 2, 3], [1, 1]) == 1
    assert assign([1, 2], [1, 2, 3]) == 2
    assert assign([1], []) == 0
    assert assign([10, 9, 8, 7], [5, 6, 7, 8]) == 2
