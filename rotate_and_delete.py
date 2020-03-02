T = int(input())
# print(T)


def basic_implementation(ar, N):
    for k in range(0, N - 1):
        ar = [ar[-1]] + ar[:-1]
        temp = n - k - 1
        if temp > 0:
            del ar[temp]
        else:
            del ar[0]
        n = len(ar)
    print(ar[0])


def optimized_implementation(ar, N):
    if N == 1:
        print(ar[0])
    elif N % 2 == 0:
        print(ar[(N - 2) // 4 + 2 - 1])
    else:
        print(ar[(N - 2) // 4 + 3 - 1])


for t in range(T):
    # N = int(input())
    N = t + 1
    n = N
    # ar = list(map(int, input().strip().split()))
    ar = list(range(1, N + 1))
    optimized_implementation(ar, N)
    basic_implementation(ar, N)
    # print(ar[0], "-->", N)
