n = int(input())
i, s = 1, 0

while i <= n:
    s = s + (1 / (i**2))
    i = i + 1

print(round(s, 6))
