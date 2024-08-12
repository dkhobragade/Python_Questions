# The Penalty Shootout

s = "1012012112110"

c = 0

for i in range(1, len(s)):
    if s[i - 1] == "2" and s[i] == "1":
        c += 1
print(c)
