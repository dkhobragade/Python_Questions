#  Prime number


n=int(input())
isPrime=0
for i in range(2,n):
    if n%i==0:
        isPrime=1
        break
if isPrime==1:
    print("Not a Prime")
else:
    print("Prime")
