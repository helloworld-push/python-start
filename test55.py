string = str(input())

k = string.find('f')

if string.find('f', k + 1) != -1:
    print(string.find('f', k + 1))
elif string.find('f') != -1:
    print(-1)
elif string.find('f') == -1:
    print(-2)
