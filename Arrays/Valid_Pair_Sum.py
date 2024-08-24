from itertools import product

# a = [3, -2, 1]
# a = [-1, -1, -1, 0]
a = [-4, 4, -5, 5, 3, -2, -3, -1, 2, 1]

# pairs = list(product(a, repeat=2))
# c = 0

# for i in pairs:
#     if sum(i) > 0:
#         c += 1
# # print(pairs)


# for i in range(1, len(a)):
#     su = a[i - 1] + a[i]
#     if su > 0:
#         c += 1
# if a[0] + a[len(a) - 1] > 0:
#     c += 1
# print(c)


count = 0
a.sort()
i = 0
j = len(a) - 1
while i < j:
    if a[i] + a[j] > 0:
        count += j - i
        j -= 1
    else:
        i += 1

print(count)
