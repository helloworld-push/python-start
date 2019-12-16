from math import floor

p, x, y = int(input()), int(input()), int(input())

perpoc = p / 100
pvkop = (x * 100) + y

depStart = pvkop

depEnd = ((depStart * (1 + perpoc)))

depEndfloor = floor(depEnd)
depEndfract = depEnd - depEndfloor

if depEndfract > 0.9999:
    depEnd = depEndfloor + 1
else:
    depEnd = depEndfloor

x = floor(depEnd / 100)
y = depEnd - (x * 100)

print(x, y)
