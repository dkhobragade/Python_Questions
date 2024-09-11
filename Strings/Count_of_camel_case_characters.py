# Count of camel case characters

S = "ckjkUUYII"
c = 0
for i in S:
    if i.isupper():
        c += 1

print(c)
