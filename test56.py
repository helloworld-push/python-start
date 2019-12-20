string = str(input())

start = string[:string.find(' ')]
end = string[(string.find(' ') + 1):]

print(end + ' ' + start)
