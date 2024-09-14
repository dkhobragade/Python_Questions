# Crazy String


S = "geeksforgeeks"
# S = "Qh"


c = ""

isUp = S[0].isupper()
print(isUp)

for i in range(len(S)):
    if not isUp:
        if i % 2 == 0:
            c += S[i].lower()
        else:
            c += S[i].upper()
    else:
        if i % 2 != 0:
            c += S[i].lower()
        else:
            c += S[i].upper()


print(c)
