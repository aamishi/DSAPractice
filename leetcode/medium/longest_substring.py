"""
Leetcode 03 - Medium
Longest Substring with non-repeating characters
"""


def longest_substring(s: str) -> int:
    """sol"""
    left_index = 0
    longest_len = 0
    history = dict()  # last seen index
    for i, ch in enumerate(s):
        if ch in history and history[ch] >= left_index:
            left_index = history[ch] + 1
        history[ch] = i
        sliding_window = i - left_index + 1
        longest_len = max(sliding_window, longest_len)
    return longest_len


if __name__ == '__main__':
    res_1 = longest_substring("bookkeeping")
    print(res_1)
