n = float(input())
numbers = list(map(int, input().split()))
x = int(input())
newNumbers = []
for i in range(len(numbers)):
    n = abs(numbers[i] - x)
    newNumbers.insert(i, n)
res = newNumbers.index(min(newNumbers))
print(numbers[res])
