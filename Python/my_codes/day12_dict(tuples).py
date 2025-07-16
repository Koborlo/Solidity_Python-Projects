bag = dict()
while True:
    inp = input('Enter File Name: ')
    try:
        fhandle = open(inp)
    except FileNotFoundError:
        print('File Not Found!Enter File:  ')
        continue
    for line in fhandle:
        line = line.rstrip()
        wordlist = line.split()
        for word in wordlist:
            bag[word] = bag.get(word,0 ) + 1
    bigword = None
    bigcount = None
    for key,value in bag.items():
        if bigcount is None:
            bigcount = value
        elif value > bigcount:
            bigcount = value
            bigword = key
    print('WORD:',bigword,'','APPEARED:',bigcount,'TIMES')
