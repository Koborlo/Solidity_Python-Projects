import urllib.request,urllib.parse, urllib.error
fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
bag = dict()
for line in fhandle:
    line = line.decode().rstrip()
    line = line.split()
    for word in line:   bag[word] = bag.get(word,0) + 1
print(bag)