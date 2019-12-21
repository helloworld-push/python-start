string = str(input())
substring = string[string.find('h') + 1:string.rfind('h')]

if substring.find('h') > -1:
    substring = substring.replace('h', 'H')
    print(string[0:string.find('h') + 1] + substring +
          string[string.rfind('h'):])
else:
    print(string)
