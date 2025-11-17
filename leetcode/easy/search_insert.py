"""
LeetCode 35 - Easy
Search Insert Position
"""


def insert_position(nums: list[int], target: int) -> int:
    """sol"""
    current_index = 0
    while nums[current_index] < target and current_index + 1 < len(nums):
        current_index += 1
    if nums[current_index] < target:
        current_index += 1
    return current_index


if __name__ == "__main__":
    arr_1 = [1, 2, 3, 5]
    res_1 = insert_position(arr_1, 7)
    res_2 = insert_position(arr_1, 5)
    res_3 = insert_position(arr_1, 4)
    res_4 = insert_position(arr_1, -1)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)
