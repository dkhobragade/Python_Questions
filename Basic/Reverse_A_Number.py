# Reverse a Number


n= int(input())
reverse=0
while n>0:
    mod = int(n%10)
    reverse = (reverse *10 ) + mod
    n = n//10
print(reverse)
