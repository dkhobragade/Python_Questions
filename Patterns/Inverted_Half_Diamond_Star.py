# Inverted_Half_Diamond_Star


n=4
j=n
k=n
o=1
for i in range(1,2*n):
    if(j>0):
        print(" "*(j - 1),"*"*i)
        j-=1
    else:
        print(" "*o,"*"*(k-1))
        o+=1
        k-=1
