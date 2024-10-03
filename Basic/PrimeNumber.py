# Prime Number

n = 8

c = 0
for i in range(2, n):
    if n % i == 0:
        c = +1
        break
if c == 1:
    print("No prime")
else:
    print("prime")

print(n**0.5)
