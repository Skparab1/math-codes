import time
from random import randint
def drawgraph(x_coordinate, y_coordinate):
    graph_drawer = 17
    while graph_drawer > 0:
        if y_coordinate == graph_drawer:
            if x_coordinate > 0:
                print((' '*50) +'_|_' , graph_drawer , '  '* x_coordinate, 'o')
            else:
                print('   '* (16 + x_coordinate) + ' o' + '   '* (-1 * x_coordinate) +'_|_' , graph_drawer)
        else:
            print((' '* 50) +'_|_' , graph_drawer)
        graph_drawer -= 1
    graph_drawer = -1
    graph_draw = -12
    print(' ',end='')
    while graph_draw <= 12:
        print(graph_draw,'|',end='')
        graph_draw += 1
    print('')
    while graph_drawer >= -17:
        if y_coordinate == graph_drawer:
            print((' '*50) +'_|_' , graph_drawer , '  '* x_coordinate, 'o')
        else:
            print((' '*50) +'_|_' , graph_drawer)
        graph_drawer -= 1
def letters_in_word_detector(word):
    word = word + 50*' '
    counter = 0
    letter = 'l'
    decider = 'no'
    while decider == 'no':
        letter = word[counter]
        if letter == ' ' :
            if (word[counter+1]) == ' ':
                if (word[counter+2]) == ' ':
                    if (word[counter+3]) == ' ':
                        decider = 'yes'
        counter += 1
    return counter
def calculate_y_val(x_value, negpos, coeficient , sign , shift):
    if negpos == 'negative' and sign == '-':
        y_value = (-1 * coeficient * x_value) - shift
    if negpos == 'negative' and sign == '+':
        y_value = (-1 * coeficient * x_value) + shift
    if negpos == 'positive' and sign == '-':
        y_value = (1 * coeficient * x_value) - shift
    if negpos == 'positive' and sign == '+':
        y_value = (1 * coeficient * x_value) + shift
    return y_value
def graph_positive(x_value, negpos, coeficient , sign , shift):
    if negpos == 'positive' and sign == '-':
        y_value = (1 * coeficient * x_value) - shift
    if negpos == 'positive' and sign == '+':
        y_value = (1 * coeficient * x_value) + shift
    
coeficient = ''
equation = input('please enter your equation in slope intercept format. ex: (y = -4567x + 1123\n  y = ')
letters = letters_in_word_detector(equation)
if equation[0] == '-':
    negpos = 'negative'
    this = 1
    letter = equation[this]
    while True:
        letter = equation[this]
        if letter == '+' or letter == '-' or letter == 'x' or letter == 'X':
            break
        coeficient = coeficient + letter
        this += 1
    this += 2
    sign = equation[this]
    this += 2
    yint = equation[this]
    if letters - 1 > this:
        this +=1
        yint = yint + equation[this]
    if letters - 2 > this:
        this +=1
        yint = yint + equation[this]
    if letters - 3 > this:
        this +=1
        yint = yint + equation[this]
    if letters - 4 > this:
        this +=1
        yint = yint + equation[this]
    if letters - 5 > this:
        this +=1
        yint = yint + equation[this]
    if letters - 6 > this:
        this +=1
        yint = yint + equation[this]
    

else:
    negpos = 'positive'
    this = 0
    letter = equation[this]
    while True:
        letter = equation[this]
        if letter == '+' or letter == '-' or letter == 'x' or letter == 'X':
            break
        coeficient = coeficient + letter
        this += 1
    this += 2
    sign = equation[this]
    this += 2
    yint = equation[this]
    if letters - 2 > this:
        this +=1
        yint = yint + equation[this]
    if letters - 2 > this:
        this +=1
        yint = yint + equation[this]
    if letters - 3 > this:
        this +=1
        yint = yint + equation[this]
    if letters - 4 > this:
        this +=1
        yint = yint + equation[this]
    if letters - 5 > this:
        this +=1
        yint = yint + equation[this]
    if letters - 6 > this:
        this +=1
        yint = yint + equation[this]
coeficient = int(coeficient)
yint = int(yint)
print('the equation is ' , negpos)
print('coeficient is ' , coeficient)
print('the sign is' , sign)
print('the y intercept is', yint)
print('x-y table\n')
print('___X_|_Y____')
print('-5   ' , calculate_y_val(-5,negpos,coeficient,sign,yint))
print('-4   ' , calculate_y_val(-4,negpos,coeficient,sign,yint))
print('-3   ' , calculate_y_val(-3,negpos,coeficient,sign,yint))
print('-2   ' , calculate_y_val(-2,negpos,coeficient,sign,yint))
print('-1   ' , calculate_y_val(-1,negpos,coeficient,sign,yint))
print(' 0   ' , calculate_y_val(0,negpos,coeficient,sign,yint))
print(' 1   ' , calculate_y_val(1,negpos,coeficient,sign,yint))
print(' 2   ' , calculate_y_val(2,negpos,coeficient,sign,yint))
print(' 3   ' , calculate_y_val(3,negpos,coeficient,sign,yint))
print(' 4   ' , calculate_y_val(4,negpos,coeficient,sign,yint))
print(' 5   ' , calculate_y_val(5,negpos,coeficient,sign,yint))
print(' 6   ' , calculate_y_val(6,negpos,coeficient,sign,yint))
print(' 7   ' , calculate_y_val(7,negpos,coeficient,sign,yint))
print(' 8   ' , calculate_y_val(8,negpos,coeficient,sign,yint))
print(' 9   ' , calculate_y_val(9,negpos,coeficient,sign,yint))
print(' 10  ' , calculate_y_val(10,negpos,coeficient,sign,yint))


x = input('enter x value of the point to graph')       
y = input('enter y value of the point to graph')          
x = int(x)
y = int(y)
drawgraph(x,y)
print(negpos)