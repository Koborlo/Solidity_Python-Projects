stri = '    I am going to school okay and I fucking love this how am I suppose to bring this fucking comma'
stri = stri.rstrip()
print(stri)
stri = stri.upper()
print(stri)
print(len(stri))
for i in stri:
    if stri.find(i) < len(stri):
        print(i)
vic = stri.replace('LOVE','hate'.upper())
print(vic)