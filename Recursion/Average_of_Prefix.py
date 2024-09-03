a = [10, 20, 30, 40, 50]

b = []

for i in range(len(a)):
    c = sum(a[: i + 1]) // len(a[: i + 1])
    b.append(c)

print(b)
