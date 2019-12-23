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
n = int(input())
print(MinDivisor(n))
