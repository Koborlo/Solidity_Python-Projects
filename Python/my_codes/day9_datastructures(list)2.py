inp = input('ENTER FILE NAME: ')
try:
    fhandle = open(inp)
except FileNotFoundError:
    print('FILE DOES DOES NOT EXIST!! ')
for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
    email = line.split()
    print(email[1])