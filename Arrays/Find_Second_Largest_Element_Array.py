# Find Second largest element in an array

arr = [12, 35, 1, 10, 34, 1]
first = 0
second = 0
a = []
b = []
for i in arr:
    a.append(i)
i = 0
while len(a) > 0:
    po = a.pop()
    if po > first:
        first = po
    else:
        b.append(po)
print(a)
print(b)
