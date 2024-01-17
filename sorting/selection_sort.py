import random

unsorted_list = [random.randint(0, 100) for i in range(21)]
print(unsorted_list)
n = len(unsorted_list)
for i in range(n):
    min_index = i
    for j in range(i, n):
        # print(j)
        if unsorted_list[j] < unsorted_list[min_index]:
            min_index = j
    unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]

print(unsorted_list)
