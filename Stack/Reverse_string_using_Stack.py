S = "GeeksforGeeks"

a = []
b = ""
for i in S:
    a.append(i)

for i in range(len(a)):
    b += a.pop()
print(b)
