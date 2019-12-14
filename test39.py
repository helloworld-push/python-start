n = 1
a, b = 0, 1
while n != 0:
    n = int(input())
    if n == 0:
        continue

    if n > a:
        a = n
        b = 0
    if n == a:
        b = b + 1
print(b)
