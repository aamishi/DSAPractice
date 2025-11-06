"""
Blind Selection Sort on Python's original array structure
"""


def selection_sort(arr) -> None:
    """
    Selection sort using list
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


if __name__ == "__main__":
    lst = [2, 2, 0, -1, 8, 3, 10, 21, 19]
    selection_sort(lst)
