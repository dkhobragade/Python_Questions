# Print first letter of every word in the string

S = "geeks for geeks"
print(S.split(" "))
a = ""
for i in S.split(" "):
    a += i[0]
print(a)
