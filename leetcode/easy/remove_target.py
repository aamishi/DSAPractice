"""
Leetcode 27 - Easy
Remove target from array in place

Leetcode 283 - Easy
Remove 0s
"""


def remove_target(arr: list, target: int) -> int:
    """Solution"""
    uniq_boundary = -1
    swap_counter = 0
    for i in range(0, len(arr)):
        if arr[i] != target:
            print("unequal element is", arr[i], "at index", i)
            print(arr[i], "<-swap->", arr[uniq_boundary + 1])
            arr[i], arr[uniq_boundary + 1] = arr[uniq_boundary + 1], arr[i]
            # print(arr)
            uniq_boundary += 1
            swap_counter += 1
    return swap_counter


def move_zeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    uniq_boundary = -1
    for i in range(len(nums)):
        if nums[i] != 0:
            print(nums[i], "<-swap->", nums[uniq_boundary + 1])
            nums[uniq_boundary + 1], nums[i] = nums[i], nums[uniq_boundary + 1]
            print(nums, uniq_boundary)
            uniq_boundary += 1


if __name__ == "__main__":
    lst = [10, 11, 0, 2, 0, 21, 0]
    # res = remove_target(lst, 10)
    # print(res)

    move_zeroes(lst)
