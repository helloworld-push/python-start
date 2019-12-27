a, b = int(input()), int(input())
if a < b:
    print(*tuple(range(a, b + 1)))
else:
    print(*tuple(range(a, b - 1, -1)))
