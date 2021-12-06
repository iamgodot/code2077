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

    return ''.join(stack)


if __name__ == '__main__':
    for str_in, str_out in ('abbaca', 'ca'), :
        assert remove_duplicates(str_in) == str_out
