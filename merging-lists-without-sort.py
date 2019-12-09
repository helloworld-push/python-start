def merge(a, b):
    c = a + b
    for i in range(len(a), len(c)):
        for k in range(len(c)):
            if c[k] >= c[i]:
                c.insert(k, c[i])
                c.pop(i + 1)
    return c
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))
