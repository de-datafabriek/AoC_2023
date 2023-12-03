import re

class part:
    def __init__(self, lindex, start, end, value, type):
        self.lindex = lindex
        self.start = start
        self.end = end
        self.value = value
        self.type = type


file = open("./input.txt")
numbers = list()
symbols = list()
lindex = 0
for line in file:
    pattern = re.compile("[0-9]+")
    for match in list(pattern.finditer(line)):
        numbers.append(part(lindex, match.start(), match.end(), match.string[match.start():match.end()],'number'))
    pattern = re.compile("[^0-9|^.|^\n]")
    for match in list(pattern.finditer(line)):
        symbols.append(part(lindex, match.start(), match.end(), match.string[match.start():match.end()],'symbol'))
    lindex += 1

sum=0
for number in numbers:
    if any(s for s in symbols if s.type == 'symbol' 
           and s.lindex >= number.lindex -1 and s.lindex <= number.lindex +1 
           and s.start >= number.start -1 and s.end <= number.end - 1):
        print('lindex {} value {}'.format(number.lindex, number.value))
        sum += int(number.value)
print(sum)
sum = 0
for s in (s for s in symbols if s.value == '*'):
    print('lindex {} value {}'.format(s.lindex, s.value))
    
    gears = list(n for n in numbers if n.type == 'number'
           and n.lindex >= s.lindex -1 and n.lindex <= s.lindex +1
           and n.start <= s.start +1 and n.end >= s.start)
    if len(gears) < 2: continue
    product = 1
    for g in gears:
        product *= int(g.value)
    sum += product
print(sum)