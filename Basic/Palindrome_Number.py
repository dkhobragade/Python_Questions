# Palindrome number



a = int(input())
num=0
while a>0:
    mod = a%10
    num = (num*10) + mod
    a=a//10
print(num)

if(a==num):
    print("Palindrome number")
else:
    print("Not a Palindrome number")

