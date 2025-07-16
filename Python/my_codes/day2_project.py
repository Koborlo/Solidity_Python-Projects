inp = input('ENTER AGE: ')
temp = input('ENTER TEMPERATURE: ')
try:
    v = int(inp)
except ValueError:
    print('NOT A NUMBER')

try:
    t = int(temp)
except ValueError :
    print('NOT A NUMBER')
if v < 13:
    print('CHILD')
elif v < 18:
    print('TEENAGER')
elif v >= 18:
    print('ADULT')
else:
    print('NOT A NUMBER!')
if t <= 10:
    print('COLD')
elif t < 20:
    print('COOL')
elif t >= 30:
    print('HOT')
else:
    print('NOT A NUMBER')
if v >= 18 and t >= 30:
    print('STAY HYDRATED')
elif v < 13 and t < 10:
    print('WEAR WARM CLOTHES')
elif v > 13 and v < 18:
    print('NICE WEATHER TODAY!')