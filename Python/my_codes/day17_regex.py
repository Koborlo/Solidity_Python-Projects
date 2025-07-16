import re
x = 'I sent $100 to kofi in his home '
jam = re.findall('\$[0-9.]', x)
print(jam)