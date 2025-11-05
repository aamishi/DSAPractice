"""
Tasks:
- [ ]  Write `findMax(arr)` and `findMin(arr)`
- [ ]  Write `reverseArray(arr)`
- [ ]  Write `resizeArray(oldArr, newSize)`
"""
from array_class import Array


def find_max(arr: Array) -> int:
    """
    find the max element of the array
    """
    arr.check_non_empty()
    big = arr.get(0)
    for i in range(arr.length):
        if arr.get(i) > big:
            big = arr.get(i)
    return big


def find_min(arr: Array) -> int:
    """
    find the min element of the array
    """
    arr.check_non_empty()
    small = arr.get(0)
    for i in range(arr.length):
        if arr.get(i) < small:
            small = arr.get(i)
    return small


def reverse_array_new_array(arr: Array) -> Array:
    """
    Reverse a given array and return a new array
    Time Complexity:
    """
    arr.check_non_empty()
    reverse_arr = Array(arr.capacity)
    for i in range(arr.capacity):
        print(arr.get(i), "swapped with", arr.get(arr.length - 1 - i))
        reverse_arr.insert(i, arr.get(arr.length - 1 - i))

    return reverse_arr


def reverse_array_in_place(arr: Array) -> None:
    """
    Reverse a given array and return a new array
    Time Complexity:
    """
    arr.check_non_empty()
    for i in range(arr.length // 2):
        print(arr.get(i), "swapped with", arr.get(arr.length - 1 - i))
        arr.elements[i], arr.elements[arr.length - 1 - i] =\
            arr.elements[arr.length - 1 - i], arr.elements[i]


def reverse_array_slicing(arr: Array) -> Array:
    """
    Reverse a given array and return a new array
    Time Complexity:
    """
    arr.check_non_empty()
    reverse_arr = Array(arr.capacity)
    return reverse_arr


def reverse_array_recursion(arr: Array) -> Array:
    """
    Reverse a given array and return a new array
    Time Complexity:
    """
    arr.check_non_empty()
    reverse_arr = Array(arr.capacity)
    return reverse_arr


def resize_array_1(arr: Array, new_size: int) -> Array:
    """
    Resize an existing array to a new size
    """
    new_arr = Array(new_size)
    if arr.capacity > new_size:
        for i in range(new_size):
            if arr.get(i) is not None:
                new_arr.insert(i, arr.get(i))

    else:
        for i in range(arr.length):
            new_arr.insert(i, arr.get(i))

    return new_arr


def resize_array(arr: Array, new_size: int) -> Array:
    """
    Resize an existing array to a new size
    """
    new_arr = Array(new_size)
    min_elements = min(new_size, arr.capacity)
    for i in range(min_elements):
        new_arr.insert(i, arr.get(i))
    return new_arr


if __name__ == "__main__":
    elements = [4, -8, -21, 0, -2]
    sample_arr = Array(len(elements))
    # elements = [0, 4, 4, 4, 4]
    for j in range(len(elements)):
        sample_arr.insert(j, elements[j])
    sample_arr.append(6)

    # find_max(sample_arr)
    # find_min(sample_arr)
    # reverse_array_in_place(sample_arr)
    # reverse_array_slicing(sample_arr)
    # reverse_array_recursion(sample_arr)
    resized_1 = resize_array(sample_arr, 3)
    resized_2 = resize_array(sample_arr, 19)

    print(sample_arr)
    print("resized_1", resized_1, resized_1.capacity)
    print("resized_2", resized_2, resized_2.capacity)
