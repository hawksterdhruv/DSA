import random

import time
import math

N = 200000
# gap = 2
p_time = 1
# while N < 64001:
# t = time.time()
unsorted_list = [random.randint(0, N * 10) for a in range(N)]

# print(unsorted_list)


def get_gaps(x):
    l = math.log((5 * x + 4) / 9) / math.log(2.25) + 1
    l = int(l)
    op = []
    for i in range(l, 0, -1):
        val = math.ceil(0.2 * (9 * 2.25 ** (i - 1) - 4))
        # print(f"{val:10.2f} {math.ceil(val):10}")
        op.append(val)

    return op


for gap in get_gaps(N):
    # breakpoint()
    for i in range(gap, N):
        count = 0
        for j in range(i, 0, -gap):
            if j - gap >= 0 and unsorted_list[j - gap] > unsorted_list[j]:
                unsorted_list[j - gap], unsorted_list[j] = (
                    unsorted_list[j],
                    unsorted_list[j - gap],
                )
            else:
                break

    # n_time = time.time() - t

    # print(f"{N}, {n_time}, {n_time/p_time}")

    # p_time = n_time
    # N *= 2


# for i in range(1, N):
#     if unsorted_list[i - 1] > unsorted_list[i]:
#         print("FAILED")
#         break
# else:
#     print("SUCCESS")
