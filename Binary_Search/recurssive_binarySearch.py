# binarySearch


def recursive_binary_search(arr, low, high, key):

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return recursive_binary_search(arr, mid + 1, high, key)
        else:
            return recursive_binary_search(arr, low, mid - 1, key)


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 11
    result = recursive_binary_search(arr, 0, len(arr) - 1, x)
    print(result)
