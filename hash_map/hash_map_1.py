"""Hash Map theory and basics"""
from typing import Type


def count_frequency(arr: list) -> dict:
    """count the frequency of all elements in a list"""
    history = dict()
    for i in range(len(arr)):
        if arr[i] in history:
            history[arr[i]] += 1
        else:
            history[arr[i]] = 1
    return history


def first_non_repeating_char(s: str) -> str:
    """Find first non-repeating character in a string

    """
    history = dict()
    for i in range(len(s)):
        if s[i] not in history:
            history[s[i]] = 1
        else:
            history[s[i]] += 1

    for k in range(len(s)):
        if history[s[k]] == 1:
            return s[k]
    return "NONE"


if __name__ == "__main__":
    hash_brown = dict()
    sample_array = [1, 4, 2, 6, 2, 2, 3, 4, 3, 21, 1, 2, 0, -1, "got ya!", "got ya!"]
    res_1 = count_frequency(sample_array)
    print(res_1)

    res_2 = first_non_repeating_char("leetcodelater")
    print(res_2)
