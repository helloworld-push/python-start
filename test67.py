def ReduceFraction(p, q):
    if q == 0:
        return int(n / p), int(m / p)
    return ReduceFraction(q, p % q)

n, m = int(input()), int(input())
print(*ReduceFraction(n, m))
