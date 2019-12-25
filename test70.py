def IsPointInSquare(x, y):
    return x >= -1 and x <= 1 and y >= -1 and y <= 1
x, y = float(input()), float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
