# Majority Element


a = [3, 1, 3, 3, 2]
n = len(a) // 2

# for i in a:
#     if a.count(i) > n:
#         print(i)
#         break
# print(-1)

cad = None
count = 0
for i in a:
    if count == 0:
        cad = i
    elif i == cad:
        count += 1
    else:
        count -= 1

print(a.count(cad))
