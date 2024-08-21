n = 10

s = 1

for i in range(1, n + 1):
    s = s * i

print(s)

a = []
for i in range(len(str(s))):
    re = s % 10
    a.append(re)
    s = s // 10
print(a[::-1])
