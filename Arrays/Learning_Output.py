# Learning Output


N = 10
A = [7, 7, 7, 7, 7, 7, -9, -9, -9, 0]

p = 0
n = 0
z = 0

for i in A:
    if i == 0:
        z += 1
    elif i > 0:
        p += 1
    else:
        n += 1

print(N / p, N / n, N / z)
