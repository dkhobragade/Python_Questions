# Count the characters

# S = "abc"
S = "geeksforgeeks"
N = 2

c = {}

for i in S:
    coun = S.count(i)
    if i not in c and coun >= N:
        c[i] = coun
print(len(c))
