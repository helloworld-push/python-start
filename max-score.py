myFile = open("input.txt", "r", encoding="utf8")
k = int(myFile.readline())
listMassive = []
for line in myFile:
    newLine = line.split()
    if int(newLine[-1]) >= 40 and int(newLine[-2]) >= 40 \
            and int(newLine[-3]) >= 40:
        listMassive.append(newLine)
myFile.close()
listMassive.sort(key=lambda a: int(a[-1]) + int(a[-2]) + int(a[-3]))
listMassive.reverse()
sumScore = []
for i in listMassive:
    sum = int(i[-1]) + int(i[-2]) + int(i[-3])
    sumScore.append(sum)
n = len(sumScore)


def competition(n, k, sumScore):
    if n <= k:
        return 0
    elif sumScore[k] == sumScore[0]:
        return 1
    for i in range(k, 0, -1):
        if sumScore[i] < sumScore[i - 1]:
            return sumScore[i - 1]

print(competition(n, k, sumScore))
