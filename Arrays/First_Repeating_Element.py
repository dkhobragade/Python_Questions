# First Repeating Element

arr = [1, 5, 3, 4, 3, 5, 6]

for i in range(len(arr)):
    if arr.count(arr[i]) > 1:
        print(i + 1)
        break
