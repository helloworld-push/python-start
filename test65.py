def power(a, b):
    if b == 0:
        return a
    if b != 0:
        return power(a + 1, b - 1)
a, b = int(input()), int(input())
print(power(a, b))
