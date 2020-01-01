n = int(input())
stroke = tuple(range(1, n + 1))
num = ''
print('+___ ' * n)
for number in stroke:
    num += ('|' + str(number) + ' / ')
print(num)
print('|__\ ' * n)
print('|    ' * n)
