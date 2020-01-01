n = int(input())
step = tuple(range(1, n + 1))
for num in step:
    print(*tuple(range(1, num + 1)), sep='')
