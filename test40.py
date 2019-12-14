n = 1
a, b, c = 0, 1, 1
while n != 0:
    n = int(input())
    if n == 0:
        continue
    if n != a:
        if b > c:
            c = b
        b = 1
    if n == a:
        b = b + 1
    a = n

if c != 1:
    print(c)
elif b > c:
    print(b)
else:
    print(c)
