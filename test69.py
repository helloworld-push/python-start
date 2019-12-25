def funk():
    p = int(input())
    if p != 0:
        funk()
    print(p)
funk()
