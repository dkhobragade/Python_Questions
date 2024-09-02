# a = [10, 20, 15, 2, 23, 90, 90]
# a = [5, 10, 20, 15]
a = [1, 2, 3]

low = 0
high = len(a) - 1

while low <= high:
    mid = low + (high - low) // 2

    if (mid == 0 or a[mid] >= a[mid - 1]) and (
        mid == len(a) - 1 or a[mid] >= a[mid + 1]
    ):
        print(mid)
    elif mid < len(a) - 1 and a[mid + 1] > a[mid]:
        low = mid + 1
    else:
        high = mid - 1

print(a[low], a[high])
