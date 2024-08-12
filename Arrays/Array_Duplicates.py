# Array Duplicates

arr = [2, 3, 1, 2, 3]
a = []
for i in range(len(arr)):
    if arr[i] in arr[i + 1 : len(arr)]:
        a.append(arr[i])

print(a)
