n = int(input())
village = list(map(int, input().split()))
m = int(input())
shelters = list(map(int, input().split()))

for i in range(len(village)):
    village[i] = [village[i], village.index(village[i])]

for k in range(len(shelters)):
    shelters[k] = [shelters[k], shelters.index(shelters[k]) + 1]

village.sort()
shelters.sort()
result = []

for y in range(len(village)):
    for x in range(len(shelters)):
        if len(shelters) == 1:
            result.append([village[y][1], shelters[x][1]])
            break
        if abs(village[y][0] - shelters[x][0]) < \
           abs(village[y][0] - shelters[x + 1][0]):
            result.append([village[y][1], shelters[x][1]])
            break
        if (x + 1) == (len(shelters) - 1):
            result.append([village[y][1], shelters[x + 1][1]])
            break

result.sort()

print(*[j[1] for j in result])
