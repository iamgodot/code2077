# Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/description/

from collections import Counter


def total_fruit(fruits: list) -> int:
    """
    Sliding window.

    Time: O(n)
    Space: O(n)
    """
    res = count = 0
    left = right = 0
    hashtable = Counter()
    while right < len(fruits):
        hashtable[fruits[right]] += 1
        count += 1
        while len(hashtable) > 2:
            if hashtable[fruits[left]] == 1:
                hashtable.pop(fruits[left])
            else:
                hashtable[fruits[left]] -= 1
            count -= 1
            left += 1
        res = max(res, count)
        right += 1

    return res


if __name__ == "__main__":
    assert total_fruit([1, 2, 1]) == 3
    assert total_fruit([0, 1, 2, 2]) == 3
    assert total_fruit([1, 2, 3, 2, 2]) == 4
    assert total_fruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
