"""
Blind QuickSort
Algorithm:
1. select a pivot -> middle
2. all elements smaller than pivot go left
3. all elements bigger than pivot go right
4. repeat
TIME:
"""


def quick_sort_new_array(arr: list) -> list:
    """Quick Sort"""
    # base: singleton array
    if len(arr) <= 1:
        return arr
    pivot = arr[(len(arr) // 2)]
    left_arr = [i for i in arr if i < pivot]
    pivot_arr = [i for i in arr if i == pivot]
    right_arr = [i for i in arr if i > pivot]

    return quick_sort_new_array(left_arr) + pivot_arr + quick_sort_new_array(right_arr)


def quick_sort(arr: list, left=0, right=None) -> list:
    """Quick Sort"""
    if right is None:
        right = len(arr) - 1

    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)

    return arr


def partition(arr: list, left, right):
    """to bring the pivot to final sorted position - not sorting"""
    pivot = arr[right]
    smaller_index = left - 1  # at any given time, i will will hold a larger element

    # all elements except the pivot - which is last
    for larger_index in range(left, right):
        if arr[larger_index] <= pivot:
            smaller_index += 1
            arr[smaller_index], arr[larger_index] = arr[larger_index], arr[smaller_index]  # swap

    # after the loop ends, swap pivot after the smaller_index
    arr[smaller_index + 1], arr[right] = arr[right], arr[smaller_index + 1]
    return smaller_index + 1


if __name__ == "__main__":
    lst_1 = [8, 3, -1, 5, 2, 1]
    qs_1 = quick_sort(lst_1)
    print(qs_1)
