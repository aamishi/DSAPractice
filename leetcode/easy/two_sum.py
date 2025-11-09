"""
Leetcode 01 - Easy
Two Sum
"""


def two_sum(arr: list[int], target: int) -> [int, int]:
    """
    Two sum solution
    """
    seen_so_far = dict()
    for i in range(len(arr)):
        if target - arr[i] not in seen_so_far:
            print("curr:", arr[i], "diff:", target - arr[i])
            seen_so_far[arr[i]] = i
            print(seen_so_far)
        else:
            print("index of diff:", seen_so_far[target - arr[i]], "index of curr:", i)
            return [seen_so_far[target - arr[i]], i]
    return [-1, -1]


if __name__ == "__main__":
    sample_arr = [5, 2, 4, 2]
    res = two_sum(sample_arr, 4)
    print(res)
