n = 1
a, b = 0, 0
while n != 0:
    n = int(input())
    if n == 0:
        continue
    if n == a:
        b = a
    if n > a:
        if b < a:
            b = a
        a = n
    if n < a and n > b:
        b = n

if b == 0:
    print(a)
else:
    print(b)
