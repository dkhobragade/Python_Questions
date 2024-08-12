# Index_Of_An_Extra_Element

arr1 = [2, 4, 6, 8, 9, 10, 12]
arr2 = [2, 4, 6, 8, 10, 12]


index = -1
for i in range(len(arr1) + 1):
    if arr1[i] != arr2[i]:
        index = i
        break
print(index)
