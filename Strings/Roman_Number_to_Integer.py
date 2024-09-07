# Roman Number to Integer

s = "V|"

co = 0

dict = {
    "|": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

for i in s:
    co = co + dict[i]

if "IV" in s:
    co -= 2
if "IX" in s:
    co -= 2
if "XL" in s:
    co -= 20
if "XC" in s:
    co -= 20
if "CD" in s:
    co -= 200
if "CM" in s:
    co -= 200

print(co)
