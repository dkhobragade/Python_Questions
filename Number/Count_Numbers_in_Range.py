# Count Numbers in Range

L = 1
R = 10


d = 0

for i in range(L, R):
    if i % 3 == 0:
        d += 1

print(d)
