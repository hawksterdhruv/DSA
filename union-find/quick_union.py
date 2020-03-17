ar = list(range(10))


def union(a, b):
    key_1 = ar[a]
    key_2 = ar[b]

    while ar[a] != a:
        a = ar[a]

    while ar[b] != b:
        b = ar[b]

    ar[b] = a


def connected(a, b):
    while ar[a] != a:
        a = ar[a]

    while ar[b] != b:
        b = ar[b]

    return a == b


print(ar)
union(4, 3)
union(3, 8)
print(ar)
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
