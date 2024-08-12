# Array Leaders

# arr = [16, 17, 4, 3, 5, 2]
arr = [5, 10, 20, 40]
# arr = [30, 10, 10, 5]

a = []
# for i in range(len(arr)):
#     c = 0
#     for j in range(i + 1, len(arr)):
#         if arr[i] < arr[j]:
#             c = 10
#     if c != 10:
#         a.append(arr[i])
# print(a[-1])


t = float("-inf")
for i in range(len(arr)):
    print(arr[i : len(arr)])
    if arr[i] >= max(arr[i : len(arr)]):
        a.append(arr[i])

print(a)
