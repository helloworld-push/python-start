n = int(input())
village = list(map(int, input().split()))
m = int(input())
shelters = list(map(int, input().split()))

for i in range(n):
    village[i] = [village[i], i + 1, 0]

for i in range(m):
    shelters[i] = [shelters[i], i + 1]

village.sort()
shelters.sort()

start = 0
for i in range(n):
    minimum = 10e10
    for j in range(start, m):
        tmp = abs(village[i][0] - shelters[j][0])
        if tmp < minimum:
            idx = j
            minimum = tmp
            village[i][2] = shelters[j][1]
        else:
            break
    start = idx

village.sort(key=lambda idx: idx[1])

print(*[j[2] for j in village])
