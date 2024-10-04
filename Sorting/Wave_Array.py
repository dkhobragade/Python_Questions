# Wave Array


# a = [2, 4, 7, 8, 9, 10]
a = [4, 1, 3, 9, 7]

# for i in range(0, len(a) - 1, 2):
#     a[i], a[i + 1] = a[i + 1], a[i]
# print(a)


# for i in range(len(a)):
#     for j in range(0, len(a) - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# print(a)


for i in range(len(a)):
    min_index = i
    for j in range(i + 1, len(a)):
        if a[min_index] > a[j]:
            min_index = j
    a[min_index], a[i] = a[i], a[min_index]
print(a)
