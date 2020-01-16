numbers = list(map(int, input().split()))
maxi = numbers.index(max(numbers))
mini = numbers.index(min(numbers))
numbers[mini], numbers[maxi] = numbers[maxi], numbers[mini]
print(*numbers)
