# Find Index


# arr = [1, 2, 3, 4, 5, 5]
# key = 5

arr = [6, 5, 4, 3, 1, 2]
key = 4

a = []

for i in range(len(arr)):
    if arr[i] == key:
        a.append(i)
print([a[0], a[-1]])
