"""
Blind Selection Sort on Python's original array structure
"""


def selection_sort(arr) -> None:
    """
    Selection sort using list
    -> left to right, selecting SMALLEST first
    """
    length = len(arr)
    for index in range(length):
        # for each index, SELECT the minimum
        sorted_index = index
        for element in range(index, length):
            if arr[element] < arr[sorted_index]:
                sorted_index = element
        # once found, place it at the index where unsorted elements start by SWAPPING with i
        # as we want space O(n)
        arr[index], arr[sorted_index] = arr[sorted_index], arr[index]


def selection_sort_biggest_first(nums: list) -> None:
    """
    -> going right to left, selecting BIGGEST first
    """
    for i in range(len(nums) - 1, -1, -1):
        big_swap_index = i
        for b in range(i, -1, -1):
            if nums[b] > nums[big_swap_index]:
                big_swap_index = b
        nums[i], nums[big_swap_index] = nums[big_swap_index], nums[i]


if __name__ == "__main__":
    lst_1 = [2, 2, 0, -1, 8, 3, 10, 21, 19]
    selection_sort(lst_1)
    lst_2 = [2, 2, 190, -1, 8, 3, 10, 21, 1]
    selection_sort_biggest_first(lst_2)
