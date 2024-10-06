# Single Number


arr = [1, 1, 2, 2, 2]

d = {}

for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

print(d)

for k, v in d.items():
    if v % 2 != 0:
        print(k)
        break
print(k, v)
