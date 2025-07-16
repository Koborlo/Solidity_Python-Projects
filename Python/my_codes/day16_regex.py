import re
fhandle = open(input('Enter File Name: '))
for line in fhandle:
    line = line.rstrip()
    email = re.findall(r'^From (\S+@\S+)',line)
    if len(email) > 0:
            for i in email:
                print(i)