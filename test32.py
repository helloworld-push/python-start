x, y = int(input()), int(input())
i = 1
while x < y:
    x = x * 0.1 + x
    i = i + 1
print(i)
