import math
while True :
    command = input('enter expression ')
    command = command + (' ' * 5)
    line = command[0] + command[1] + command[2] + command[3]
    if line in command:
        command = command.replace(line,' ')
    command = int(command)
    print(command)
    print(line)
    if line == 'sin ':
        print(math.sin(command))
    if line == 'cos ':
        print(math.cos(command))
    if line == 'tan ':
        print(math.tan(command))
    if line == 'csc ':
        print(1/(math.sin(command)))
    if line == 'sec ':
        print(1/(math.cos(command)))
    if line == 'cot ':
        print(1/(math.tan(command)))