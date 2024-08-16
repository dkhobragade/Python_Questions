# Smaller and Larger

a = [1, 5, 8, 10, 11, 12, 19]
x = 5
s = 0
l = 0
b = []
for i in a:
    if i == x:
        s += 1
        l += 1
    elif i <= x:
        s += 1
    elif i >= x:
        l += 1
b.append(s)
b.append(l)

print(b)
