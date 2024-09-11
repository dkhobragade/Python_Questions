# Display longest name

# names = ["Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks"]
names = [
    "nkkUFNu",
    "xZrz",
    "mnMg",
    "Ook",
    "tlyhNkO",
    "UGz",
    "RCDDIUT",
    "ioj",
    "a",
    "yzp",
]

# a = {}
# for i in names:
#     a[i] = len(i)
# print(a)

# print(max(a, key=a.get))


str = ""

for i in names:
    if len(i) > len(str):
        str = i
print(str)
