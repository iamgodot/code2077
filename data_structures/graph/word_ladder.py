# Word Ladder
# https://leetcode.com/problems/word-ladder/description/


def ladderLength(beginWord: str, endWord: str, wordlist: list[str]) -> int:
    """
    Need to form a combination dict before BFS.

    Time: O(m^2*n) m as len(wordlist), n as len(beginWord)
    Space: O(m^2*n)
    """
    if endWord not in wordlist:
        return 0
    from collections import deque, defaultdict

    queue = deque()
    visited = set()
    combinations = defaultdict(list)  # generics: list of words in wordlist

    length = len(beginWord)
    for word in wordlist:
        for i in range(length):
            combinations[word[:i] + "*" + word[i + 1 :]].append(word)

    count = 1
    queue.appendleft((beginWord, count))
    visited.add(beginWord)
    while queue:
        word, count = queue.pop()
        for i in range(length):
            key = word[:i] + "*" + word[i + 1 :]
            for matched_word in combinations[key]:
                if matched_word == endWord:
                    return count + 1
                else:
                    visited.add(matched_word)
                    queue.appendleft((matched_word, count + 1))
            combinations[key].clear()
    return 0
