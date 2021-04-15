import math
print('type in the following format:   log 2 8  for log₂8')
fish = input('log ')
num = 0
reader = 'start'
first = ''
second = ''
try:
    while True:
        reader = fish[num]
        while reader != ' ':
            first = first + reader
            num += 1
            reader = fish[num]
        num += 1
        if first != '':
            break
except:
    print('')
try:
    while True:
        reader = fish[num]
        while reader != ' ':
            second = second + reader
            num += 1
            reader = fish[num]
        num += 1
        if second != '':
            break
except:
    print('')
first, second = int(first), int(second)
logged = math.log(second,first)
print('log ',first,second,'  = ',logged)
                
        