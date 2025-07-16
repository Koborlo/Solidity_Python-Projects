
def age_(calc):
    try:
        calc = int(calc)
    # If input is not a number, show an error.
    except ValueError:
        print( 'NOT A NUMBER!!! ENTER NUMBER:')
        return
    #If valid, calculate and show the number of days they’ve lived (approx.).
    days_lived = float( calc * 365)
    print('DAYS LIVED AT THIS AGE =', round(days_lived))
    return
while True:
    # Ask the user for their age.
    inp = input('ENTER AGE:  ')
    if inp.lower() == 'done':
        print('Exiting........Done!!!')
        break
    else:
        age_(inp)

