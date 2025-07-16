bag = dict()
count = 1
while True:
    inp = input('Enter word: ')
    if inp not in bag:
        bag[inp] = count
    else:
        bag[inp] =  bag[inp] + 1
    print(bag)
