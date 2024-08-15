# Bubble Sort

a = [3, 5, 2, 4, 1]

for i in range(len(a)):
    for j in range(0, len(a) - i - 1):
        print(a[i], a[j])
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
