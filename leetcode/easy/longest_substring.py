"""
LeetCode 14 - Easy
Longest prefix
"""


def longest_substring(arr: list[str]):
    """sol"""
    res = ""
    lex_order = sorted(arr)
    for i in range(min(len(lex_order[0]), len(lex_order[-1]))):
        if lex_order[0][i] != lex_order[-1][i]:
            return res
        res = res + lex_order[0][i]
    return res


if __name__ == "__main__":
    sample_arr_1 = ["aab", "aa", "aabc", "aabcsd", "ab"]
    res_1 = longest_substring(sample_arr_1)
    print("res_1:", res_1)

    sample_arr_2 = ["hitlls", "hits", "hitiiiiitch"]
    res_2 = longest_substring(sample_arr_2)
    print("res_2:", res_2)

    sample_arr_3 = ["dog", "racecar", "car"]
    res_3 = longest_substring(sample_arr_3)
    print("res_3:", res_3)
