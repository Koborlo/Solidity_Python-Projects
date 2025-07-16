while True:
    inp = input('ENTER FILE:  ')
    try:
        fhandle = open(inp)
    except FileNotFoundError:
        print('FILE ENTERED IS WRONG!!!')
        continue
    count = 0
    for line in fhandle:
        if not line.startswith('From:'):
            continue
        line = line.rstrip()
        count = count + 1
        print(line)
    print(count)