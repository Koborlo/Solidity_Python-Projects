bag = dict()
while True:
    inp = input('Enter File Name:')
    try:
        fhandle = open(inp)
    except FileNotFoundError:
        print('File Does Not Exist! Try Again!!!: ')
        continue
    for line in fhandle:
        line = line.rstrip()
        line = line.split()
        for i in line:
            bag[i] = bag.get(i,0) + 1
    print(bag)
