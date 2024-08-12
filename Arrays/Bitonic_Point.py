# Bitonic Point


arr = [1, 15, 25, 45, 42, 21, 17, 12, 11]

# print(max(arr))

index = 0
for i in range(1, len(arr)):
    if arr[i - 1] < arr[i]:
        index = arr[i]
    else:
        break
print(index)
