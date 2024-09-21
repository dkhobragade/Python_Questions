# How Many X's?

L = 10
R = 19
X = 1


d = 0
for i in range(L + 1, R):
    d += str(i).count(str(X))
print(d)
