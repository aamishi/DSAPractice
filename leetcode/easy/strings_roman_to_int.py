"""
Leetcode: 13 Easy
Roman to Integer
"""


def roman_to_int(string: str) -> int:
    """sol"""
    characters = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    prev_value = 0
    total_sum = prev_value
    for i in range(len(string) - 1, -1, -1):
        print("string", string[i])
        if characters[string[i]] < prev_value:
            total_sum -= characters[string[i]]
            print(i, characters[string[i]], "minus", total_sum)
        else:
            total_sum += characters[string[i]]
            print(i, characters[string[i]], "plus", total_sum)
        prev_value = characters[string[i]]
    return total_sum


if __name__ == "__main__":
    res_1 = roman_to_int("IV")
    res_2 = roman_to_int("V")
    res_3 = roman_to_int("VI")
    res_4 = roman_to_int("L")
    res_5 = roman_to_int("MCMXCIV")

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)
    print(res_5)
