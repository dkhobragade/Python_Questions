# Prime_Number_Within_Range

n=int(input())
isPrime=0
a=[]
for i in range(2,n):
    c=0
    for j in range(2,n):
        if i%j==0:
            c+=1
    if(c==1):
        a.append(i)
print(a)
