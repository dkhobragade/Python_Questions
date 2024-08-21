s = {"the", "quick", "brown", "fox", "quick"}
word1 = "the"
word2 = "fox"

count = 0
count1 = 0
slist = list(s)
for i in range(len(slist)):
    if slist[i] == word1:
        count = i
    elif slist[i] == word2:
        count1 = i
print(count, count1)
