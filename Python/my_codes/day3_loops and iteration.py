while True:
    celsius = input('ENTER CELSIUS TEMPERATURE:  ')
    if celsius.lower() == 'done':
        print('EXITING PROGRAMME:...')
        print('DONE')
        break
    try:
        celsius = int(celsius)
    except:
        celsius = -1
    fahrenheit = (celsius * 9/5) + 32
    if celsius == -1:
        print('WRONG VALUE! ENTER A NUMBER: ')
        continue
    else:
        print('FAHRENHEIT TEMPERATURE:',fahrenheit)
        print('DONE!!!')