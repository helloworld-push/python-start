a, b, c, d, e = int(input()), int(input()), int(input()), \
                int(input()), int(input())
if b <= d and c <= e or c <= d and b <= e:
    print('YES')
elif a <= d and c <= e or c <= d and a <= e:
    print('YES')
elif b <= d and a <= e or a <= d and b <= e:
    print('YES')
else:
    print('NO')
