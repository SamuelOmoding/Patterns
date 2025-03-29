def patterns():
    rows = 5
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        nums = "".join(str(j) for j in range(1, i + 1))
        print(spaces + nums + nums[-2::-1])
        
    for i in range(rows - 1, 0, -1):
        spaces = " " * (rows - i)
        nums = "".join(str(j) for j in range(1, i + 1))
        print(spaces + nums + nums[-2::-1])
patterns()    