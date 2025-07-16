import re
l = list()
fhandle = open(input('Enter File Name: '))
for line in fhandle:
    line = line.rstrip()
    # print(line)
    word = re.findall(r'\ba\S*|\S+a\S*', line)
    # print(word)
    for v in word:
        l.append(v)
        # print(l)
foo = dict()
for value in l:
    foo[value] = foo.get(value,0) + 1

bag = []
prot = []

for k,v in foo.items():
    links = re.findall(r'^htt.*\S', k)
    for word_ in links:
        links.append(word_)
    for vu in links:
        print(vu)