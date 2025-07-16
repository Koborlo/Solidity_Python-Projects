d = {'car': 5, 'house': 20, 'yatch': 3, 'privateJet': 1}
list = []
for k,v in d.items():
    list.append((v,k))
list = sorted(list,reverse=True)
print(list)
b = {}
for k,v in list:
    b[v] = k
print(b)
