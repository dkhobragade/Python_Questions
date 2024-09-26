s = [4, 3, 1, 10, 2, 6]

a = []
b = []
for i in s:
    a.append(i)

for i in range(len(a)):
    b.append(a.pop())
print(b)
