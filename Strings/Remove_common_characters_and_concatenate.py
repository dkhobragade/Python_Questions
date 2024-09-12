# Remove common characters and concatenate

s1 = "aacdb"
s2 = "gafd"

a = ""

for i in s1:
    if i not in s2:
        a += i
print(a)

for i in s2:
    if i not in s1:
        a += i
print(a)
