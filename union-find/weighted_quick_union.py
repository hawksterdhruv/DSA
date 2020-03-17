N = 10

ar = list(range(N))
size = [1] * N


def union(a, b):
    if connected(a, b):
        return

    while ar[a] != a:
        a = ar[a]

    while ar[b] != b:
        b = ar[b]

    if size[a] < size[b]:
        ar[a] = b
        size[b] += 1
    else:
        ar[b] = a
        size[a] += 1


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
print(size)
union(6, 5)
union(9, 4)
union(2, 1)
print(ar)
print(size)
print(connected(0, 7))
print(connected(8, 9))
union(5, 0)
union(7, 2)
union(6, 1)
union(1, 0)
print(connected(0, 7))
print(ar)
