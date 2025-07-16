cc = dict()
words = ['gwen','csev','zhen','gwen' , 'csev', 'fhan','csev', 'zhen']
for i in words:
    cc[i] = cc.get(i,0) + 1
print(cc)


