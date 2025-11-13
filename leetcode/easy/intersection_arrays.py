"""
Leetcode 349 - Easy
Intersection of 2 arrays
"""


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """sol"""
    res = set()
    history = dict()
    for e in nums1:
        history[e] = True

    for e in nums2:
        if e in history:
            res.add(e)
    return list(res)


if __name__ == "__main__":
    arr_1 = [0, 2, 4, 9, 16, 25]
    arr_2 = [-2, -1, 0, -1, 2, 2, 25, 16, 100, 10000, 2, 2, 2, 0, 0]

    res_1 = intersection(arr_1, arr_2)
    print(res_1)
