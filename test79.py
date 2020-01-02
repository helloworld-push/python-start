numbers = list(map(int, input().split()))
maxi = max(numbers)
for n in range(len(numbers) - 1, -1, -1):
    if numbers[n] == maxi:
        break
print(maxi, n)
