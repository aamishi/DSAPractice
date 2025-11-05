"""
Traversal & Manipulation
"""
from array_class import Array


def left_to_right(arr: Array) -> None:
    """
    Traverse left to right
    - 0 to len
    """
    for i in range(arr.length):
        print(i)


def right_to_left(arr: Array) -> None:
    """
    Traverse right to left
    - len - 1 to 0
    """
    for i in range(arr.length - 1, 0, -1):
        print(i)


def running_sum_prefix(arr: Array) -> Array:
    """
    Return the running sum of an array
    [1, 2, 3, 4] -> [1, 3, 6, 10]
    """
    running_sum = Array(arr.length)
    sum_so_far = 0
    for i in range(arr.length):
        sum_so_far += arr.get(i)
        running_sum.insert(i, sum_so_far)
    return running_sum


def running_sum_suffix(arr: Array) -> Array:
    """
    For each index i, suffix sum = sum of all elements from that index to the end
    sum from i to length
    arr = [2, 4, 6, 8]
    suffix = [20, 18, 14, 8]
    """
    running_sum = Array(arr.length)
    sum_so_far = 0
    for i in range(arr.length, 0, -1):
        index = i - 1
        sum_so_far += arr.get(index)
        running_sum.set(index, sum_so_far)
        # print("insert index", index, "ssf", sum_so_far)
    return running_sum


def running_minimum(arr: Array) -> Array:
    """
    arr = [7, 3, 5, 2, 6, 1]
    returns [7, 3, 3, 2, 2, 1]
    """
    run_min = Array(arr.length)
    min_so_far = arr.get(0)
    for i in range(arr.length):
        if arr.get(i) < min_so_far:
            min_so_far = arr.get(i)
        run_min.append(min_so_far)
    return run_min


def running_maximum(arr: Array) -> Array:
    """
    arr = [-1, 3, 5, 2, 6, 1]
    returns -1, 3, 5, 5, 6, 6]
    """
    run_min = Array(arr.length)
    max_so_far = arr.get(0)
    for i in range(arr.length):
        if arr.get(i) > max_so_far:
            max_so_far = arr.get(i)
        run_min.append(max_so_far)
    return run_min


def swap_in_place(arr: Array) -> None:
    """
    Given an array of integers,
    reverse the array in-place so that
    the first element becomes the last
    the second becomes the second-last, and so on
    """
    # length = arr.length
    # for i in range(arr.length // 2, 0, -1):
    #     # print("reversed index", i - 1, "swaps with", length - i)
    #     temp_var = arr.get(i - 1)
    #     arr.set(i - 1, arr.get(length - i))
    #     arr.set(length - i, temp_var)

    start = 0
    end = arr.length - 1
    while start < end:
        temp = arr.get(start)
        arr.set(start, arr.get(end))
        arr.set(end, temp)
        start += 1
        end -= 1  # meet in the middle, end moves to the right for odd sized array


def equilibrium_index(arr: Array) -> int:
    """
    Given an array of integers: find the equilibrium index where the sum of all elements to the left
    equals the sum of all elements to the right, WITHOUT INCLUDING ITSELF

    Example:
    Input → [1, 7, 3, 6, 5, 6]
    Output → 3 (index)

    If no such index exists, return -1
    """
    total_sum = 0
    left_sum = 0
    length = arr.length
    for i in range(length):
        total_sum += arr.get(i)
        # print("total_sum", total_sum)

    for i in range(length):
        right_sum = total_sum - left_sum - arr.get(i)
        # print("reversed index", i, "swaps with", length - i)
        # print("left sum =", left_sum, "right sum=", right_sum, "total_sum", total_sum)
        if left_sum == right_sum:
            return i

        left_sum += arr.get(i)
    return -1


def rotate_by_k(arr: Array, k_steps) -> None:
    """
    Given an array nums and an integer k, rotate the array to the right by k steps
    so that the last k elements move to the front

    Example 1:
    Input → nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    Output → [5, 6, 7, 1, 2, 3, 4]

    Example 2:
    Input → nums = [-1, -100, 3, 99], k = 2
    Output → [3, 99, -1, -100]
    """
    # NOT OPTIMISED FOR TIME -> O(kn)
    # for i in range(arr.length, k_steps, -1):
    #     last_element = arr.get(arr.length - 1)
    #     print("last_element", last_element)
    #     arr.delete(arr.length - 1)
    #     arr.insert(0, last_element)
    #     print("arr", arr.elements)

    def reverse(start=0, end=arr.length - 1):
        while start < end:
            temp = arr.get(start)
            arr.set(start, arr.get(end))
            arr.set(end, temp)
            start += 1
            end -= 1

    reverse()
    reverse(start=0, end=k_steps - 1)
    reverse(start=k_steps, end=arr.length - 1)
    print("arr", arr)


def remove_occurrences(arr: Array, value: int) -> int:
    """
    Given an integer and an integer value, remove all occurrences of value in-place and return the
    new length of the array after removal
    """
    o_index = 0
    for r_index in range(arr.length):
        if arr.get(r_index) != value:
            # you replace with overwite index
            arr[o_index] = arr[r_index]
            o_index += 1
    return o_index


if __name__ == "__main__":
    elements = [-1, 3, 5, 2, 6, 1]
    sample_arr = Array(len(elements))
    for j in range(len(elements)):
        sample_arr.insert(j, elements[j])

    print(sample_arr)
    # left_to_right(sample_arr)
    # right_to_left(sample_arr)
    # rsp = running_sum_prefix(sample_arr)
    # rss = running_sum_suffix(sample_arr)
    # rmin = running_minimum(sample_arr)
    # rmax = running_maximum(sample_arr)
    # eqi = equilibrium_index(sample_arr)
    # rotate_by_k(sample_arr, 2)
    # swap_in_place(sample_arr)
    # rac = remove_occurrences(sample_arr, 6)

    # print("prefix", rsp)
    # print("suffix", rss)
    # print("running_minimum", rmin)
    # print("running_maximum", rmax)
    # print(sip)
    # print(eqi)
    # print(rac)
