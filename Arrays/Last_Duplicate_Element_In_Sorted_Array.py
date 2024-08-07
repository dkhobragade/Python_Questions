# arr = [1, 5, 5, 6, 6, 7]
arr = [8, 13]

num = -1
index = -1
for i in range(len(arr)):
    if arr[i - 1] == arr[i]:
        num = arr[i - 1]
        index = i
if index == -1:
    print(-1)
else:
    print(num, index)
