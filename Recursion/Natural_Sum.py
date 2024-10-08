n = 10

su = 0
for i in range(1, n + 1):
    if su == n:
        break
    su = su + i
    print(su)
print(i)
