# Uncommon characters


A = "geeksforgeeks"
B = "geeksquiz"

c = ""

for i in A:
    if i not in B:
        c += i

for i in B:
    if i not in A:
        c += i

d = "".join(sorted(c))
print(d)
