# Value equal to index value


arr = [15, 2, 45, 4, 7]

c = 0

for i in range(len(arr)):
    if arr[i] == i + 1:
        c += 1
print(c)
