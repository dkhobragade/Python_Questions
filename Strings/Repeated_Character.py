# Repeated Character

S = "abcde"


for i in S:
    if S.count(i) > 1:
        print(i)
        break
