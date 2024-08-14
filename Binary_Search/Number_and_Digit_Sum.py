# # Number and the Digit Sum


def sumofDigits(n):
    s = 0
    while n != 0:
        rem = n % 10
        s = s + rem
        n = n // 10
    return s


def numberCount(n, k):
    low = 1
    high = n
    while low <= high:
        mid = (high + low) // 2
        s = sumofDigits(mid)
        if mid - s >= k:
            high = mid - 1
        else:
            low = mid + 1
    return high


if __name__ == "__main__":
    n = 13
    k = 3
    print("ok", numberCount(n, k))
