inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
students = list(map(str, inFile.readlines()))
k = int(students[0])
students.remove(students[0])
sortStudents = []
sortStudents1 = []
count = 0


for i in range(len(students)):
    students[i] = students[i].split()
    if (int(students[i][-1]) >= 40 and int(students[i][-2]) >= 40 and int(students[i][-3])) >= 40:
        sortStudents.append(int(students[i][-1]) + int(students[i][-2]) + int(students[i][-3]))

sortStudents.sort(key=lambda p: -p)

for j in range(len(sortStudents)):
    if len(sortStudents) <= k:
        break
    if sortStudents[j] == max(sortStudents):
        count += 1
    if j <= (k - 1) and sortStudents[j] != sortStudents[k]:
        sortStudents1.append(sortStudents[j])

if k == 0:
    print(0, file=outFile)
elif count > k:
    print(1, file=outFile)
elif len(sortStudents) <= k:
    print(0, file=outFile)
else:
    print(min(sortStudents1),  file=outFile)

inFile.close()
outFile.close()
