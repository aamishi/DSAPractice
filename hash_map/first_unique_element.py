"""Find the first unique elememt in an array"""


def first_unique(arr: list) -> int:
    """sol"""
    history = dict()
    for i in arr:
        if i in history:
            history[i] += 1
        else:
            history[i] = 1

    for e in arr:
        if history[e] == 1:
            return e
    return -1


if __name__ == "__main__":
    sample_1 = [1, 2, 3, 2, 1]
    sample_2 = [1, 1, 5, 2, 2, 3]
    sample_3 = [1, 1, 1, 1]

    res_1 = first_unique(sample_1)
    res_2 = first_unique(sample_2)
    res_3 = first_unique(sample_3)

    print(res_1)
    print(res_2)
    print(res_3)
