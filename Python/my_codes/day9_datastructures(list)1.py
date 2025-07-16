numlist = list()
while True:
    inp = input('ENTER NUMBER:  ')
    if inp.lower() == 'done':
        break
    try:
        inp = int(inp)
    except ValueError:
        print('WRONG VALUE!!! ENTER NUMBER!! ')
        continue
    numlist.append(inp)
    avg = sum(numlist)/ len(numlist)
print('AVERAGE: ',avg)