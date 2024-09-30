# Check Equal Arrays

arr1 = [1, 2, 5, 4, 0]
arr2 = [2, 4, 5, 0, 1]


for i in range(len(arr1)):
    if arr1[i] in arr2:
        arr2.remove(arr1[i])
print(arr1, arr2)
