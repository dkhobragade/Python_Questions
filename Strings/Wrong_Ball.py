# Wrong Ball


s = "RBRB"
c = 0
for i in range(1, len(s) + 1):
    if i % 2 == 0 and s[i - 1] == "R":
        c += 1
    elif i % 2 != 0 and s[i - 1] == "B":
        c += 1
print(c)
