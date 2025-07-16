#create a function
def miles_(numb):
    try:
        numb = float(numb)
    except ValueError:
        print('VALUE NOT A NUMBER!!! TRY AGAIN ')
        return
    numb = numb * 0.621371
    print('MILES: ', numb)
    return
while True:
    user_inp = input('ENTER NUMBER IN KILOMETERS: ')
    if user_inp.lower() == 'done':
        print('Exiting Code....')
        print('DONE!!!!')
        break

    miles_(user_inp)