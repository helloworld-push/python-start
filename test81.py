numbers = list(map(int, input().split()))
newList = ''
for num in numbers:
    if num > 0:
        newList = newList + str(num) + ' '
newList = list(map(int, newList.split()))
print(min(newList))
