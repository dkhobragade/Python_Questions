str = "zvvo"

s = []
s.append(str[0])
for i in str[1:]:
    print(i)
    if i in s:
        continue
    else:
        s.append(i)
print("".join(s))
