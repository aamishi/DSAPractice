"""
Merge Sort
1. divide: into smaller arrays unit singleton arrays are formed
    i. recursive and will break at the base case, the return value will be used later by itself
2. conquer: sort the arrays
3. combine sorted arrays

Time-complexity: O(n comparisions x logn for splitting)

Space-complexity: O(n) for creating a temp arr -> result
"""


def merge_sort(arr: list, debug: bool = False) -> list:
    """Merge Sort"""

    # base: singleton array is already sorted - break for recursion
    # base_counter = 0
    if len(arr) <= 1:
        # base_counter += 1
        debug_log(debug, "singleton achieved", arr[0])
        return arr

    # divide step
    mid_point = len(arr) // 2
    left_arr = arr[:mid_point]
    right_arr = arr[mid_point:]
    debug_log(debug, f"Split: {arr} -> Left: {left_arr}, Right: {right_arr}")

    # conquer - obtain singletons and compare
    left_sorted = merge_sort(left_arr, debug)
    right_sorted = merge_sort(right_arr, debug)

    # combine
    final_merged = merge(left_sorted, right_sorted, debug)
    return final_merged


def merge(left: list, right: list, debug) -> list:
    """Merge Sort helper"""
    result = []
    i = j = 0
    debug_log(debug, "\tcomparing", left, "&", right)

    # this take O(n) time, cuz you still compare every element in each of the two lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            debug_log(debug, "\t\tsmaller found in left", left[i])
            result.append(left[i])
            i += 1
        else:
            debug_log(debug, "\t\tsmaller found in right", right[j])
            result.append(right[j])
            j += 1
        debug_log(debug, "\t\t\tadding smallest", result)

    # assert max(left) <= min(right)
    result.extend(left[i:])
    result.extend(right[j:])
    debug_log(debug, "\tadding remaining", result)
    debug_log(debug, "\t--------------------------------------------------")
    return result


def debug_log(debug, *args) -> None:
    """Debug helper"""
    if debug:
        print(*args)


if __name__ == "__main__":
    DEBUG = True
    # DEBUG = False
    lst_1 = [8, 3, -1, 5, 2, 1, 2, 1, 4, 3]
    # lst_1 = [2, 1, 4, 3]
    # res_1 = merge_sort(lst_1)
    res_1 = merge_sort(lst_1, debug=DEBUG)
    print(res_1)
