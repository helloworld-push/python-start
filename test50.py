a, b, c = float(input()), float(input()), float(input())
D = b**2 - (4 * a * c)

if D > 0:
    x1 = (-b - D**.5) / (2 * a)
    x2 = (-b + D**.5) / (2 * a)
    if x2 > x1:
        print(round(x1, 6), round(x2, 6))
    else:
        print(round(x2, 6), round(x1, 6))
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    print()
