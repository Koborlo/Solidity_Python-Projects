while True:
    def temperature_cal(celsius):
        if celsius.lower() == 'done':
            print('EXITING PROGRAMME:...')
            print('DONE')
            return
        try:
            celsius = int(celsius)
        except:
            celsius = -1
        fahrenheit = (celsius * 9 / 5) + 32
        if celsius == -1:
            print('WRONG VALUE! ENTER A NUMBER: ')
            return
        else:
            print('FAHRENHEIT TEMPERATURE:', fahrenheit)
            print('DONE!!!')
            return
    #takes user input as argument variable
    user_inp = input('ENTER CELSIUS TEMPERATURE:  ')
    if user_inp.lower() == 'done':
        break
    else:
        temperature_cal(user_inp)
        continue
