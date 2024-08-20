arr = [2, 2, 5, 5, 20, 30, 30]

c = 0

for i in arr:
    if arr.count(i) == 1:
        c = i

print(c)
