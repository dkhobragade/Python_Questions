# Two_Repeated_Elements

# arr = [1, 2, 1, 3, 4, 3]
arr = [1, 2, 2, 1]


a = set()
# for i in range(len(arr)):
#     print(arr[i : len(arr)])
#     if arr[i] in arr[i + 1 : len(arr)]:
#         a.append(arr[i])
# print("a", a)

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] == arr[j]:
            a.add(arr[i])
print(a)
