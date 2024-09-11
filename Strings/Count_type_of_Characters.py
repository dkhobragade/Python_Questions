# Count type of Characters

S = "#GeeKs01fOr@gEEks07"

d = 0
u = 0
l = 0
a = 0
for i in S:
    if i.isdigit():
        d += 1
    elif i.isupper():
        u += 1
    elif i.islower():
        l += 1
    else:
        a += 1

print(u, l, d, a)
