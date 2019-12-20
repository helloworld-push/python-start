string = str(input())
k = string.find('f')
string2 = string[-1::-1]
if string.find('f') == -1:
    print()
elif string.find('f', k + 1) == -1:
    print(string.find('f'))
else:
    print(string.find('f'), (len(string) - 1 - string2.find('f')))
