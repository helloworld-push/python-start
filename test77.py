numbers = list(map(int, input().split()))
newList = ''
i = 0
for num in numbers:
    if num % 2 == 0:
        newList = newList + str(num) + ' '
    i += 1
print(*list(map(int, newList.split())))
