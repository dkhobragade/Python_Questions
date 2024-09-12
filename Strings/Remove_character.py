# Remove character

string1 = "computer"
string2 = "cat"


a = ""
for i in string1:
    if i not in string2:
        a += i

print(a)
