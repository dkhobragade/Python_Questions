# Anagram

a = "geeksforgeeks"
b = "forgeeksgeeks"

sa = "".join(sorted(a))
sb = "".join(sorted(b))

for i in range(len(a)):
    if sa[i] != sb[i]:
        print(a[i], False)
        break
print(True)
