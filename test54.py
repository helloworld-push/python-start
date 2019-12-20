string = str(input())

start = string.find('h')
string2 = string[-1::-1]
end = len(string) - string2.find('h')

part1 = string[0:start]
part2 = string[end:]

print(part1 + part2)
