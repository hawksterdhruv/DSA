import random

count = 0


def bin_search(needle, arr):
    global count
    count += 1
    if count >= 20:
        exit(1)

    n = len(arr)
    if n <= 0:
        return False

    if needle == arr[n // 2]:
        return True

    if needle < arr[n // 2]:
        # print("left", n // 2)
        return bin_search(needle, arr[: n // 2])
    else:
        # print("right", n // 2)
        return bin_search(needle, arr[n // 2 + 1 :])

    return False


if __name__ == "__main__":
    arr = list(range(128))
    # needle = float(input())
    needle = random.choice(list(range(128)))
    print(bin_search(needle, arr))

