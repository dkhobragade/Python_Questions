# Delete alternate characters


s = "Geeks"

c = ""
for i in range(len(s)):
    if i % 2 == 0:
        c += s[i]

print(c)
