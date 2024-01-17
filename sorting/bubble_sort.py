import random

unsorted_list = [random.randint(0, 100) for i in range(10)]
print(unsorted_list)

n = len(unsorted_list)

for i in range(n):
    for j in range(n - i - 1):
        if unsorted_list[j] > unsorted_list[j + 1]:
            unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    print(i, unsorted_list)

print(unsorted_list)
