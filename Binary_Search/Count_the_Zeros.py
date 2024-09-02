arr = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]

low = 0
high = len(arr) - 1

while low <= high:
    mid = low + (high - low) // 2

    if arr[mid] == 0:
        high = mid - 1
    else:
        low = mid + 1
print(low, high)
