def SumNum(p, q):
    if p == 0:
        return q
    return SumNum(int(input()), q + p)
p = int(input())
q = 0
print(SumNum(p, q))
