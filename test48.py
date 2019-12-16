p, x, y = int(input()), int(input()), int(input())

y2 = y + x * 100

x2 = x * (1 + (p * 31)/(365 * 100))**11
kop = (y2 * p) / 100

print(round(x2), round(kop % 100))
