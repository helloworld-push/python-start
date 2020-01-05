numbers = list(map(int, input().split()))
k = int(input())
numbers[k] = ''
print(*list(map(int, (' '.join(map(str, numbers))).split())))
