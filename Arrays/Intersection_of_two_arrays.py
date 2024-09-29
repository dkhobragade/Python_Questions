# Intersection of two arrays

a = [1, 2, 3, 4, 5, 6]
b = [3, 4, 5, 6, 7]

print(set(a) & set(b))
c = 0
for i in a:
    for j in b:
        if i ^ j == 0:
            c += 1
print(c)
