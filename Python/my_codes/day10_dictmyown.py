bag = dict()
words = list()
while True:
    inp = input('Enter File Name Here: ')
    fhandle = open(inp)
    for line in fhandle:
        line = line.rstrip()
        # line = line.split()
        # print(line)
        if line.startswith('From: '):
            line= line.split()
            word_ = line[1]
            word = word_.split('@')
            words.append(word[0])
            # print(words)
    for val in words:
        if val not in bag:
            bag[val] = 1
        else:
            bag[val] = bag[val] + 1

    print(bag)