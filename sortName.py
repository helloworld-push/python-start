inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
students = list(map(str, inFile.readlines()))

for i in range(len(students)):
    students[i] = students[i].split()
    students[i].remove(students[i][2])

students.sort(key=lambda p: p[0])

for i in range(len(students)):
    students[i] = ' '.join(students[i]) + '\n'

print(*students, file=outFile)
inFile.close()
outFile.close()
