"""
Leetcode - 242. Easy
Is the pair an anagram?
"""


def is_anagram(s: str, t: str) -> bool:
    """sol"""
    count_s = [0] * 26
    count_t = [0] * 26
    a_ref = ord('a')

    if len(s) != len(t):
        return False

    for c in s:
        count_s[ord(c) - a_ref] += 1

    for c in t:
        if count_s[ord(c) - a_ref] == 0:
            return False
        count_t[ord(c) - a_ref] += 1

    return count_s == count_t


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))
