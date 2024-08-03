# Armstrong number


a= 1538

sum = 0
l= len(str(a))
while a>0:
    m = a % 10
    sum = sum + m**l
    a=a//10

if(a== sum):
    print("Armstrong")
else:
    print("Not a Armstrong")