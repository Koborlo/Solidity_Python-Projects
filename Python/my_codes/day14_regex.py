import re
list_ = []
fhandle = open(input('Enter File Name: '))
for line in fhandle:
    print(line)
    line = line.rstrip()
    if re.search('^From.*@.*[0-9]+',line ):
        print(line)
        line = line.rstrip()
        email = re.findall(r'\S*a\S*',line)
        print(email)
        for v in email:
            list_.append(v)
