s = "123"

print(int("098"))

for i in range(len(s)):
    if (i == 0 and s[i] == "-") or s[i].isdigit():
        continue
    else:
        print(-1)
print(int(s))
