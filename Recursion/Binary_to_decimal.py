b = "10001000"

print(int(b, 2))


a = 1
su = 0
for i in range(len(str(b)), 0, -1):
    if str(b)[i - 1] == "1":
        su = su + a
    a = a * 2
print(su)
