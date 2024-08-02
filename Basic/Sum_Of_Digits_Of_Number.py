# Sum_Of_Digits_Of_Number


n = int(input())
sum=0
while n!=0:
    mod = int(n%10)
    sum = sum + mod
    n = n/10
print(sum)
