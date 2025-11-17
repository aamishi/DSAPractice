"""
Leetcode - 88 - Easy
Merge two sorted arrays
"""


def merge_sorted_arrays(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """Sol"""
    mixed_point = m + n - 1
    rev_2 = n - 1
    rev_1 = m - 1
    while rev_1 >= 0 and rev_2 >= 0:
        if nums1[rev_1] > nums2[rev_2]:
            print("found greater in nums1")
            nums1[mixed_point] = nums1[rev_1]
            rev_1 -= 1
        else:
            print("found greater in nums2")
            nums1[mixed_point] = nums2[rev_2]
            rev_2 -= 1
        mixed_point -= 1
    while rev_2 >= 0:
        nums1[mixed_point] = nums2[rev_2]
        rev_2 -= 1
        mixed_point -= 1


if __name__ == "__main__":
    arr_1, s_1 = [0, 2, 3, 0, 0, 0], 3
    arr_2, s_2 = [2, 3, 6], 3
    arr_3, s_3 = [2, 5, 6], 0

    # merge_sorted_arrays(arr_1, s_1, arr_2, s_2)
    merge_sorted_arrays(arr_1, s_1, arr_3, s_3)
