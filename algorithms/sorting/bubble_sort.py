"""
Blind Bubble Sort on Python's original array structure
"""


def bubble_sort(arr) -> None:
    """
    Bubble sort using list
    - check pair (i, i+1) ie (i, next element) and move the bigger one to the right
    """
    length = len(arr)
    check_counter = 0
    for index in range(length):
        # in each loop, you BUBBLE until you send one the biggest element to the right
        has_swapped = False
        check_counter += 1
        for element in range(0, length - index - 1):
            if arr[element] > arr[element + 1]:
                arr[element], arr[element + 1] = arr[element + 1], arr[element]
                has_swapped = True
        if not has_swapped:
            print("stopping early, array already sorted")
            break
    print(check_counter)


def bubble_sort_small_first(nums: list) -> None:
    """Bubbling smallest elements to the front first"""
    for index in range(len(nums) - 1, -1, -1):
        has_swapped = False
        for smallest in range(len(nums) - 1, len(nums) - index - 1, -1):
            if nums[smallest] < nums[smallest - 1]:
                nums[smallest - 1], nums[smallest] = nums[smallest], nums[smallest - 1]
        if not has_swapped:
            print("stopping early, array already sorted")
            break


if __name__ == "__main__":
    lst_1 = [2, 2, 0, -1, 8, 3, 10, 21]
    bubble_sort(lst_1)
    lst_2 = [1, 2, 3, 4, 5, 4]
    bubble_sort(lst_2)
    lst_3 = [12, 2, 0, -1, 8, 3, 10, 21]
    bubble_sort_small_first(lst_3)
