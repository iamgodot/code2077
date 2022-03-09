# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
# 回文串 是正着读和反着读都一样的字符串。


from typing import List


# 时间复杂度 O(n * 2^n)
# 空间复杂度 O(n ^ 2)
def partition(s: str) -> List[List[str]]:
    def is_p(string: str) -> bool:
        i, j = 0, len(string) - 1
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1

        return True

    def bt(start: int):
        length = len(s)
        if start == length:
            res.append(path.copy())
            return
        for i in range(start, length):
            sub_s = s[start : i + 1]
            if is_p(sub_s):
                path.append(sub_s)
                bt(i + 1)
                path.pop()

    res, path = [], []
    bt(0)
    return res


if __name__ == "__main__":
    print(partition("a"))
