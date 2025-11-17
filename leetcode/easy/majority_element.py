"""
Leetcode - 169 - Easy
Majority element
"""
from collections import defaultdict


def majority_element(nums: list) -> int:
    """sol"""
    major_len = -(-(len(nums))//2)
    history = defaultdict(int)
    for e in nums:
        history[e] += 1
        if history[e] >= major_len:
            return e


def majority_element_boyer_moore(nums: list) -> int:
    """
    Boyer-Moore voting algorithm
    -> the last one standing will always be the majority element
    O(n)
    """
    candidate = nums[0]
    counter = 0
    for e in nums:
        if counter == 0:
            candidate = e
        elif e == candidate:
            counter += 1
        else:
            counter -= 1

        counter += 1 if e == candidate else -1

    return candidate


def majority_element_sorting(nums: list) -> int:
    """
    Using sorting algorithm with O(nlogn)
    """
    nums.sort()
    return nums[len(nums) // 2]


if __name__ == "__main__":
    res_1 = majority_element([2, 2, 1, 3, 2, 1, 1, 1])
    print(res_1)

    res_2 = majority_element_boyer_moore([1, 2, 2, 2, 1, 1, 1, 1, 4])
    print(res_2)

    res_3 = majority_element_sorting([0, 1, 2, 2, 1, 1, 1, 1, 4])
    print(res_3)
