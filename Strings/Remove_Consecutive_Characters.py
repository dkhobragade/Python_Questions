# Remove Consecutive Characters


S = "aabaa"
# S = "aabb"
a = ""

for i in range(len(S)):
    print(S[i - 1], S[i])
    if i == 0 or S[i] != S[i - 1]:
        a += S[i]
print(a)
