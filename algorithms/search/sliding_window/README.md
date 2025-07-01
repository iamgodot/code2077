# Sliding Window

For elements in a list or characters in a string, sometimes we can use sliding window technique to reduce time complexity from O(n^2)(Brute force) to O(n).

The essential condition is we know how to move or streth the window, depending on if it's fixed-size or variable-size.

Keywords: Anagrams, Substring

Caveats:

1. Check if it goes for maximum(longest) or minimum
2. If using a hash table, only characters we care matter
3. Check if it needs to return the substring or the length

## Questions

1. Fixed-size window
   1. [Find All Anagrams in a String](find_anagrams.py)
   2. [Permutation in String](permutation_in_string.py)
   3. [Sliding Window Maximum](sliding_window_maximum.py)
2. Variable-size window
   1. [Longest Substring Without Repeating Characters](longest_substring.py)
      1. [Longest Substring with At Most Two Distinct Characters](longest_substring.py)
      1. [Longest Substring with At Most K Distinct Characters](longest_substring.py)
   1. [Longest Repeating Character Replacement](longest_repeat_char_replacement.py)
   1. [Minimum Window Substring](min_window.py)
   1. [Minimum Size Subarray Sum](min_subarray.py)
   1. [Fruit Into Baskets](total_fruits.py)
