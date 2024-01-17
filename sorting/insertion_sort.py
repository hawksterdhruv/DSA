import random

unsorted_list = [random.randint(0, 10) for a in range(10)]

print(unsorted_list)


def insert_shift_list(arr, i, j):
    arr = arr[0:j] + [arr[i]] + arr[j:i] + arr[i + 1 :]
    return arr


n = len(unsorted_list)
for i in range(1, n):
    for j in range(0, i):
        if unsorted_list[i] < unsorted_list[j]:
            unsorted_list = insert_shift_list(unsorted_list, i, j)
    print(i, unsorted_list)

print(unsorted_list)

