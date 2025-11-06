"""
Searching & Sorting Fundamentals
"""
from array_class import Array


def linear_search(arr: Array, value: int) -> (int, bool):
    """
    linear search for a value
    """
    for i in range(arr.length):
        if arr.get(i) == value:
            return (i, True)

    return (-1, False)


def binary_search(arr: Array, value: int) -> (int, bool):
    """
    binary search for a sorted array
    """
    left_cmp = 0
    right_cmp = arr.length - 1
    while left_cmp <= right_cmp:
        mid_point = (right_cmp + left_cmp) // 2
        if arr.get(mid_point) == value:
            return (mid_point, True)
        elif arr.get(mid_point) < value:  # go right
            left_cmp = mid_point + 1
        else:
            right_cmp = mid_point - 1
    return (-1, False)


def binary_search_first_occurrence_variant(arr: Array, value: int) -> (int, bool):
    """
    find the first occurrence of value via binary search for a sorted array
    """
    index_left = -1
    is_exists = False
    left_cmp = 0
    right_cmp = arr.length - 1
    while left_cmp <= right_cmp:
        mid_point = (right_cmp + left_cmp) // 2
        if arr.get(mid_point) >= value:
            if arr.get(mid_point) == value:
                index_left = mid_point
                is_exists = True
            right_cmp = mid_point - 1
        elif arr.get(mid_point) < value:  # go right
            left_cmp = mid_point + 1
        # else:
    return (index_left, is_exists)


def binary_search_last_occurrence_variant(arr: Array, value: int) -> (int, bool):
    """
    find the last occurrence of value via binary search for a sorted array
    """
    index_right = -1
    is_exists = False
    left_cmp = 0
    right_cmp = arr.length - 1
    while left_cmp <= right_cmp:
        mid_point = (right_cmp + left_cmp) // 2
        if arr.get(mid_point) <= value:
            if arr.get(mid_point) == value:
                index_right = mid_point
                is_exists = True
            left_cmp = mid_point + 1
        else:
            right_cmp = mid_point - 1
    return (index_right, is_exists)


def binary_search_insert_variant(arr: Array, value: int) -> int:
    """
    find the index of where a value SHOULD be inserted in a sorted array via binary
    """
    left_cmp = 0
    right_cmp = arr.length
    while left_cmp < right_cmp:
        mid_point = (right_cmp + left_cmp) // 2
        if arr.get(mid_point) >= value:  # go left
            right_cmp = mid_point
        else:  # go right
            left_cmp = mid_point + 1
        # else:
    return left_cmp


def selection_sort(arr: Array) -> None:
    """
    Selection sort
    """
    for i in range(arr.length):
        unsorted_index = i
        for k in range(i, arr.length):
            if arr.get(k) < arr.get(unsorted_index):
                unsorted_index = k
        temp = arr.get(i)
        arr.set(i, arr.get(unsorted_index))
        arr.set(unsorted_index, temp)


def bubble_sort(arr: Array) -> None:
    """
    bubble sort the biggest numbers to the right
    """
    def swap(first_index: int, last_index: int):
        """Swap two elements in arr"""
        temp = arr.get(first_index)
        arr.set(first_index, arr.get(last_index))
        arr.set(last_index, temp)

    for i in range(arr.length):
        print(i, "th element -", arr.get(i))
        for curr_index in range(0, arr.length - i - 1):
            print("\t", arr.get(curr_index), "gets compared to", arr.get(curr_index + 1))
            if arr.get(curr_index) > arr.get(curr_index + 1):
                print("\t\tswapping now")
                swap(curr_index, curr_index + 1)
        print("end of loop for", i)
        print(arr)


def is_sorted(arr: Array) -> bool:
    """return if an array is sorted"""
    for i in range(1, arr.length):
        if arr.get(i - 1) > arr.get(i):
            return False
    return True


if __name__ == "__main__":
    # elements = [9, 2, 104, 56, 6, 8]
    elements = [1, 2, 2, 2, 2, 4, 32]
    sample_arr = Array(len(elements))
    for element in range(len(elements)):
        sample_arr.insert(element, elements[element])

    print(sample_arr)
    # ls = linear_search(sample_arr, 6)
    # bs = binary_search(sample_arr, 8)
    # bs_left = binary_search_first_occurrence_variant(sample_arr, 8)
    # bs_right = binary_search_last_occurrence_variant(sample_arr, 60)
    # bs_insert = binary_search_insert_variant(sample_arr, 5)
    check_sort = is_sorted(sample_arr)
    # print("ls_______:", ls)
    # print("bs_______:", bs)
    # print("bs_right_:", bs_right)
    # print("bs_insert:", bs_insert)
    # selection_sort(sample_arr)
    # bubble_sort(sample_arr)
    print(check_sort)
