# Second Largest


# a = [12, 35, 1, 10, 34, 1]

a = [32011, 123, 1045, 1205, 254, 28763, 6537, 3161]
# b.sort(reverse=True)
# print(b)

first = -1
second = -1


for i in range(len(a)):
    first = max(first, a[i])

print(first)
for i in range(len(a)):
    if a[i] != first:
        second = max(second, a[i])

print(second)
