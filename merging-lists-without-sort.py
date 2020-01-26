def merge(a, b):
    c = []
    i, k = 0, 0
    for x in range(len(a) + len(b)):
        if i < len(a) and k < len(b):
            if a[i] < b[k]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[k])
                k += 1
        elif i < len(a):
            c.append(a[i])
            i += 1
        elif k < len(b):
            c.append(b[k])
            k += 1
    return c
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))
