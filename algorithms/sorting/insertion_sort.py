"""
Insertion Sort Algorithm
Time Complexity = O(n)
"""


def insertion_sort(nums: list):
    """Sol"""
    for index in range(len(nums)):
        print("find correct index for", index, nums[index])
        correct_i = index
        while correct_i > 0 and nums[correct_i - 1] > nums[correct_i]:
            print("\tswapping")
            nums[correct_i - 1], nums[correct_i] = nums[correct_i], nums[correct_i - 1]
            correct_i -= 1
        print("\t\tcorrect index", correct_i)


if __name__ == "__main__":
    sample_array = [7, 14, 13, -3, 12]
    insertion_sort(sample_array)
    print(sample_array)
