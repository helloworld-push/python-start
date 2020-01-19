n = int(input())
massivePart = []
for i in range(n):
    k = str(input())
    massivePart.append([k.split()[0] + '\n', int(k.split()[1])])
massivePart.sort(key=lambda p: -p[1])
print(*[j[0] for j in massivePart], sep='')
