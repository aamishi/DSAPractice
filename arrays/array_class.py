"""
Array Class
"""
from typing import Any


class Array:
    """
    Array Class
    """
    def __init__(self, capacity: int) -> None:
        """
        initialize with a fixed size
        - create a list of size capacity, filled with None values
        """
        self.capacity = capacity
        self.length = 0
        self.elements = [None] * capacity

    def __repr__(self) -> str:
        """For debugging"""
        return f"Array({[self.elements[i] for i in range(self.length)]})"

    def _index_out_of_bounds(self, index) -> None:
        """Index of out of bounds exception"""
        if index < 0 or index >= self.capacity:
            raise Exception("index out of bounds")

    def check_non_empty(self) -> None:
        """Invalid array empty exception"""
        if self.length == 0:
            raise ValueError("Array is empty")

    def __getitem__(self, index) -> Any:
        self._index_out_of_bounds(index)
        return self.elements[index]

    def __setitem__(self, index, value) -> Any:
        self._index_out_of_bounds(index)
        self.elements[index] = value

    def insert(self, index: int, value: Any) -> None:
        """
        - [_]  check if the array is full or dynamically insert by creating a new array
        - [x]  check if the index is valid
        - [x]  shift every element
        - [x] then add at index
        """
        ...
        if self.length >= self.capacity:
            # self.capacity *= 2
            # big_arr = [None] * self.capacity
            # for k in range(self.length):
            #     big_arr[k] = self.elements[k]
            # self.elements = big_arr
            raise Exception("Array full")

        self._index_out_of_bounds(index)

        for i in range(self.length, index, -1):
            self.elements[i] = self.elements[i-1]

        self.elements[index] = value
        self.length += 1

    def append(self, value) -> None:
        """
        Append at the last cell in self viz. @self.length
        """
        self.insert(self.length, value)

    def delete(self, index) -> None:
        """
        Delete element at index
        - [] remove element at index
        - [] shift everything to the left
        - [] reduce length
        """
        self._index_out_of_bounds(index)

        print("Removed:", self.elements[index])
        self.elements[index] = None

        for i in range(index, self.length - 1):
            self.elements[i] = self.elements[i+1]

        self.elements[self.length - 1] = None
        self.length -= 1

    def search(self, value) -> int:
        """
        linear search - o(n), brute force, no alg
        """
        for i in range(self.length):
            if self.elements[i] == value:
                print(value, "found at index:", i)
                return i
        print(value, "Not found in array")
        return -1

    def get(self, index) -> Any:
        """
        get element at index
        """
        self._index_out_of_bounds(index)
        # print("Element at given index [", index, "]:", self.elements[index])
        return self.elements[index]

    def set(self, index, value):
        """
        set element at index without moving
        """
        self._index_out_of_bounds(index)
        self.elements[index] = value


if __name__ == "__main__":
    arr = Array(5)

    for j in range(5):
        arr.insert(j, j * 11)
        # print(arr)

    arr.search(33)
    arr.search(5)
    arr.get(4)

    print(arr)
    for j in range(5):
        arr.delete(0)
        print(arr)
