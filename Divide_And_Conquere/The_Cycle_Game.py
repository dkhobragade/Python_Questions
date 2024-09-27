x = 3
y = 2
n = 3


for i in range(n):
    if i % 2 == 0:
        x = x * 2
    else:
        y = y * 2
w = x
z = y

print(max(w, z) // min(w, z))
