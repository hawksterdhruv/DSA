import random
import time

N = 4000

# while N < 10000000:
#     t = time.time()
unsorted_list = [random.randint(0, N * 10) for a in range(N)]

# print(unsorted_list)

for i in range(1, N):
    for j in range(i, 0, -1):
        if unsorted_list[j - 1] > unsorted_list[j]:
            unsorted_list[j - 1], unsorted_list[j] = unsorted_list[j], unsorted_list[j - 1]
    # print(time.time() - t)
    # N = N * 2
# print(unsorted_list)
