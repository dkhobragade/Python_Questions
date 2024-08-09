# Repeated IDs

a = [8, 8, 6, 2, 1]
un = []
for i in a:
    if i in un:
        continue
    else:
        un.append(i)
print(un)
