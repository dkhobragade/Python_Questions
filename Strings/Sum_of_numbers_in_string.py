# Sum of numbers in string


s = "1abc23"


for i in s:
    if i.isalpha():
        s = s.replace(i, " ")

new = s.split()
c = 0
for i in new:
    c += int(i)

print(c)
