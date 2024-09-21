# Middle of Three


A = 978
B = 518
C = 300

a = min(A, B, C)
print(a)
b = max(A, B, C)
if A != a and A != b:
    print(A)
elif B != a and B != b:
    print(B)
else:
    print(C)
