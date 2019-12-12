n = int(input())
if 11 <= n <= 19 or n % 10 == 0 or 5 <= n % 10 <= 9:
    print(n, 'korov')
elif n % 10 == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')
