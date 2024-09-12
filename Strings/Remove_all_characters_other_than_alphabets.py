# Remove all characters other than alphabets

S = "$Gee*k;s..fo, r'Ge^eks?"

a = ""

for i in S:
    if i.isalpha():
        a += i

print(a)
