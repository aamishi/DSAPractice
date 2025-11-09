"""
Leetcode 26 - Easy
Remove duplicates from sorted array
"""


def remove_duplicates(arr: list) -> int:
    """Solution"""
    # for i in range(len(arr)):
    uniq_boundary = 0
    counter_todo = 1  # todo remove
    for i in range(1, len(arr)):
        print("new element is", arr[uniq_boundary])
        if arr[i] > arr[uniq_boundary]:
            uniq_element = arr[i]
            print("new element is at index", i)
            print(uniq_element, "<-swap->", arr[uniq_boundary + 1])
            arr[i], arr[uniq_boundary + 1] = arr[uniq_boundary + 1], arr[i]
            print(arr)
            uniq_boundary += 1
            counter_todo += 1
    return counter_todo


if __name__ == "__main__":
    lst = [2, 2, 4, 5, 5, 5, 6, 6, 6, 6]
    res = remove_duplicates(lst)
    print(res)
