fname = open('love')
dict = {}
list = []
for line in fname:
    line = line.rstrip()
    words= line.split()
    for w in words:
        dict[w] = dict.get(w,0) + 1
print(list)
list = sorted([(v,k) for k,v in dict.items()],reverse = True)
print(list)

# print(sorted([(v,k) for k,v in dict.items()],reverse = True))
# for k,v in dict.items():
#     list.append((v,k))
#     list = sorted(list,reverse=True)
# print(list)
for k,v in list[:10]:
    print(v,k)

