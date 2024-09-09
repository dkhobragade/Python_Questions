# Remove vowels from string


S = "welcome to geeksforgeeks"

a = "aeiouAEIOU"

d = ""
for i in S:
    if i not in a:
        d += i

print(d)
