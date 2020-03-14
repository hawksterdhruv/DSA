import random

unsorted_list = [random.randint(0, 100) for i in range(21)]

count = 0


def merge(ar1, ar2):
    n = len(ar1)
    m = len(ar2)
    i = 0
    j = 0
    final = []
    while i < n and j < m:
        if ar1[i] <= ar2[j]:
            final.append(ar1[i])
            i += 1
        else:
            final.append(ar2[j])
            j += 1

    if i < n:
        final += ar1[i:]
    if j < m:
        final += ar2[j:]

    return final


def merge_sort(ar):
    # global count
    # count += 1
    # if count >= 20:
    #     return
    if (n := len(ar)) <= 1:
        return ar
    return merge(merge_sort(ar[: n // 2]), merge_sort(ar[n // 2 :]))


if __name__ == "__main__":
    print(unsorted_list)
    l = merge_sort(unsorted_list)

    print(l)
