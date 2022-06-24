# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
# 在 S 上反复执行重复项删除操作，直到无法继续删除。
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。


def remove_duplicates(s: str) -> str:
    stack = list()

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


# 给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。
# 你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。
# 在执行完所有删除操作后，返回最终得到的字符串。
# 本题答案保证唯一。


def remove_duplicates2(s: str, k: int) -> str:
    stack = []
    for char in s:
        if not stack or stack[-1][0] != char:
            stack.append([char, 1])
        else:
            _, num = stack.pop()
            stack.append([char, num + 1])
        if stack[-1][1] == k:
            stack.pop()
    return "".join([item[0] * item[1] for item in stack])


if __name__ == "__main__":
    for str_in, str_out in (("abbaca", "ca"),):
        assert remove_duplicates(str_in) == str_out
    assert remove_duplicates2("abcd", 2) == "abcd"
    assert remove_duplicates2("deeedbbcccbdaa", 3) == "aa"
    assert remove_duplicates2("pbbcggttciiippooaais", 2) == "ps"
