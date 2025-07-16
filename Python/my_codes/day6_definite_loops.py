smallest_so_far = None
count = 0
total = 0
for i in [23,41,34,33,4,6,7,67,54,444,344,3,4,5,15,56,6]:
    count = count + 1
    total =  total + i
    if smallest_so_far is None:
        smallest_so_far = i
        print('Before',smallest_so_far)
    elif i < smallest_so_far :
        smallest_so_far = i
        print('After', smallest_so_far)
    print('After', smallest_so_far)
    print('COUNT:',count, 'TOTAL:', total)
