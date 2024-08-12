# Peak element

# arr = [1, 1, 1, 2, 1, 1, 1]
arr = [1, 1, 1]
index = -1
for i in range(1, len(arr)):
    if arr[i - 1] < arr[i]:
        index = i
if index == -1:
    print(0)
print(index)
