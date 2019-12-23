from math import sqrt


def MinDivisor(a):
    root = int(sqrt(a))
    i = 2
    while i < root:
        if a % i == 0:
            return i
        i += 1
    if a % root == 0 and root != 1:
        return root
    return a


def IsPrime(b):
    return b / MinDivisor(n) == 1
n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')
