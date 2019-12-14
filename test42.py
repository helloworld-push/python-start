a, b, c, a2, b2, c2 = int(input()), int(input()), int(input()), \
                int(input()), int(input()), int(input())

if a > b:
    (a, b) = (b, a)
if a > c:
    (a, c) = (c, a)
if b > c:
    (b, c) = (c, b)
if a2 > b2:
    (a2, b2) = (b2, a2)
if a2 > c2:
    (a2, c2) = (c2, a2)
if b2 > c2:
    (b2, c2) = (c2, b2)

if a == a2 and b == b2 and c == c2:
    print('Boxes are equal')
elif a <= a2 and b <= b2 and c <= c2:
    print('The first box is smaller than the second one')
elif a >= a2 and b >= b2 and c >= c2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
