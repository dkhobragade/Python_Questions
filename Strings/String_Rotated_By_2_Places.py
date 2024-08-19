a = "amazon"
b = "azonam"


if len(a) != len(b):
    print("NO")


print(a[2 : len(a)] + a[0:2])
print(a[len(a) - 2 : len(a)] + a[0 : len(a) - 2])
