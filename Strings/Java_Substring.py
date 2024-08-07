S = "cdbkdub"
L = 0
R = 5

text = ""
for i in range(len(S)):
    if i >= L and i <= R:
        text += S[i]

print(text)
