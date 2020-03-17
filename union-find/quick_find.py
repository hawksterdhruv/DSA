ar = list(range(10))


def union(a, b):
    key_1 = ar[a]
    key_2 = ar[b]

    for idx, gp in enumerate(ar):
        if gp == key_2:
            ar[idx] = key_1


def connected(a, b):
    return ar[a] == ar[b]


union(4, 3)
union(3, 8)
union(6, 5)
union(9, 4)
union(2, 1)
print(ar)
print(connected(0, 7))
print(connected(8, 9))
union(5, 0)
union(7, 2)
union(6, 1)
union(1, 0)
print(connected(0, 7))
print(ar)
