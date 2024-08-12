# String_With_Numbers_At_Its_End

# s = "geek5"
s = "gwfchbznorpwvj000014"
c = 0

d = ""
for i in range(len(s)):
    if s[i].isalpha():
        c += 1
    else:
        d = s[i:]
        break
if c == int(d):
    print(1)
else:
    print(0)
