i, n = 0, 1
while n != 0:
    n = int(input())
    if n == 0:
        continue
    if n % 2 == 0:
        i = i + 1
print(i)
