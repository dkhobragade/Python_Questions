S = "i.like.this.program.very.much"

print(S.split("."))
b = ""
for i in S.split("."):
    print(i)
    b += i[::-1] + "."
print(b[0 : len(S)])
