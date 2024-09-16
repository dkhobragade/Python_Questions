# Value equal to index value

arr = [15, 2, 45, 4, 7]

c = 0
for i in range(1, len(arr)):
    print(arr[i - 1], i)
    if arr[i - 1] == i:
        c += 1
print(c)
