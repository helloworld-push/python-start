numbers = list(map(int, input().split()))
newList = ''
i = 1
for num in numbers:
    if i > len(numbers) - 1:
        break
    if num < numbers[i]:
        newList = newList + str(numbers[i]) + ' '
    i += 1
print(*list(map(int, newList.split())))
