word = 'I love gertrude so much i really wanna marry her.Shes the most beautiful woman I ever saw'
count = 0
for i in word:
    if i.lower() == 'i':
        count= count + 1
print(count)