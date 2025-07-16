count = 0
total = 0
while True:
    inp_ = input('ENTER INTEGER VALUE: ')
    if inp_.lower() == 'done':
        break
    try:
        inp_ = int(inp_)
    except ValueError:
        print('NO NUMBER ENTERED: ENTER A NUM!! ')
        continue
    count = count + 1
    total = total + inp_
    avg_ = total / count
    print('TOTAL:',total, 'COUNT: ',count)
print('TOTAL:',total, 'COUNT:',count, 'AVERAGE:',avg_)
