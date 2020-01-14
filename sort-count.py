def CountSort(A):
    countA = [0] * 101
    result = []
    for i in A:
        countA[i] += 1
    for nowA in range(101):
        result.append((str(nowA) + ' ') * countA[nowA])
    return result

A = list(map(int, input().split()))
print(*CountSort(A), sep='')
