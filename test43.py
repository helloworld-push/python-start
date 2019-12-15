a, b, c = float(input()), float(input()), float(input())

p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** .5
if s % 1 == 0:
    print(round(s))
else:
    print(round(s, 6))
