# Missing in Array

n = 5
arr = [1, 2, 3, 5]
a = n * (n + 1) // 2
su = 0
for i in arr:
    su = su + i
print(a - su)
