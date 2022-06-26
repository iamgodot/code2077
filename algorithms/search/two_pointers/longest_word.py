# 给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
# 如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。


def find_longest_word(s: str, dictionary: list) -> str:
        res = ""
        for word in dictionary:
            i = j = 0
            length_s, length_word, length_res = len(s), len(word), len(res)
            while i < length_s and j < length_word:
                if s[i] == word[j]:
                    i += 1
                    j += 1
                    continue
                i += 1
            if j < length_word:
                continue
            if length_word > length_res or (length_word == length_res and word < res):
                res = word

        return res


if __name__ == "__main__":
    assert (
        find_longest_word("abpcplea", dictionary=["ale", "apple", "monkey", "plea"])
        == "apple"
    )
    assert find_longest_word("abpcplea", dictionary=["a", "b", "c"]) == "a"
