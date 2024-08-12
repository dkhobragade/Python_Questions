# Move all zeroes to end of array

a = [3, 5, 0, 0, 4]

c = 0
for i in range(len(a)):
    if a[i] != 0:
        a[c] = a[i]
        c += 1
for i in range(c, len(a)):
    a[i] = 0
print(a)

# for i in range(len(a)):
#     if a[i] == 0:
#         a.pop(i)
#         a.append(0)
# print(a)
