# Rearrange a string

s = "AC2BEW3"

a = "0123456789"
su = 0
b = ""

for i in s:
    if i in a:
        su = su + int(i)
    else:
        b = b + i

print(su)
print("".join(sorted(b)) + str(su))
