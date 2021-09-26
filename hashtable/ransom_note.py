# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，
# 判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。
# 如果可以构成，返回 true ；否则返回 false。
# 题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。
# 杂志字符串中的每个字符只能在赎金信字符串中使用一次。


# 使用哈希表，时间复杂度为 O(m+n)，空间复杂度视实现而定
# 使用 list 可以控制长度固定在 26，即常量；使用 dict 开销更大，最坏情况会是 O(m+n)
def decide_with_list(ransome_note: str, magazine: str) -> bool:
    hashtable = [0] * 26

    for i in magazine:
        hashtable[ord(i) - ord('a')] += 1

    for i in ransome_note:
        if not hashtable[ord(i) - ord('a')]:
            return False
        hashtable[ord(i) - ord('a')] -= 1

    return True


def decide_with_counter(ransome_note: str, magazine: str) -> bool:
    from collections import Counter

    c1, c2 = Counter(ransome_note), Counter(magazine)

    return len(c1 - c2) == 0


if __name__ == '__main__':
    for method in [decide_with_list, decide_with_counter]:
        assert method('a', 'b') is False
        assert method('aa', 'ab') is False
        assert method('aa', 'aab') is True
