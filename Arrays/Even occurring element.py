# Even occurring element

arr = [9, 12, 23, 10, 12, 12, 15, 23, 14, 12, 15]
a = []
for i in arr:
    if arr.count(i) % 2 == 0 and i not in a:
        a.append(i)
print(a)

arr = [9, 12, 23, 10, 12, 12, 15, 23, 14, 12, 15]
count = {}
a = []

# First pass: Count occurrences of each element
for i in arr:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

# Second pass: Collect elements with even counts, ensuring no duplicates
for i in arr:
    if count[i] % 2 == 0 and i not in a:
        a.append(i)

print(a)
