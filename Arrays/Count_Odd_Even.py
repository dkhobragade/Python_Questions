# Count_Odd_Even

arr = [1, 2, 3, 4, 5]
o = 0
e = 0
a = []
for i in arr:
    if i % 2 == 0:
        e += 1
    else:
        o += 1
a.append(o)
a.append(e)
print(a)
