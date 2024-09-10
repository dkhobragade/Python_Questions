# Find Substring from last of the Given String

X = "geeksforgeeks"
Y = "geeks"

if Y not in X:
    print(-1)
else:
    print(X.rfind(Y) + 1)
