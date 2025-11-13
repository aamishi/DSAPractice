"""
Leetcode - 42 Medium
Group anagrams
"""
from collections import defaultdict


def group_anagrams_klogk(arr: list[str]) -> list[list[str]]:
    """sol"""
    history = defaultdict(list)
    for i in range(len(arr)):
        history["".join(sorted(arr[i]))].append(arr[i])
    return list(history.values())


def group_anagrams_optimised(strs: list) -> list[list[str]]:
    """optimised solution"""
    anagrams = defaultdict(list)

    for word in strs:
        count = [0] * 26  # assuming lowercase a–z
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        anagrams[tuple(count)].append(word)
    return list(anagrams.values())


if __name__ == "__main__":
    sample_array = ["eat", "tea", "tan", "ate", "nat", "bat", "ant", "teeetteee", ""]
    res_1 = group_anagrams_klogk(sample_array)
    print(res_1)

    opt_1 = group_anagrams_optimised(sample_array)
    print(opt_1)
