# Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/


def eval_rpn(tokens: list) -> int:
    """
    Use a stack, but watch out for some details:
    1. Convert str to int
    2. Keep the floor value of the division result
    3. Check what to return when the stack is empty

    Time: O(n)
    Space: O(n)
    """
    stack = []

    for token in tokens:
        if token in "+-*/":
            num2 = stack.pop()
            num1 = stack.pop()
            # NOTE: we need to use int() to truncate toward zero
            stack.append(int(eval(f"{num1}{token}{num2}")))
        else:
            stack.append(int(token))

    return stack.pop()


if __name__ == "__main__":
    for tokens, res in (
        (["18"], 18),
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ):
        assert eval_rpn(tokens) == res
