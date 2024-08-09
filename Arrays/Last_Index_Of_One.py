#  Last_Index_Of_One.py

s = "00001"
index = -1
for i in range(len(s)):
    if s[i] == "1":
        index = i
print(index)
