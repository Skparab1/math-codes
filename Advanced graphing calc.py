def stringslicer(string):
    a = ''
    b = ''
    c = ''
    d = ''
    e = ''
    f = ''
    #scanner below
    scanner = 0
    variables_scanned = 1
    if scanner < len(string):
        reader = string[scanner]
        if reader != ' ':
            while reader != ' ' and scanner < len(string):
                a = a + reader
                scanner += 1
                if scanner < len(string):
                    reader = string[scanner]
                else:
                    break
            variables_scanned += 1
            #print('came in to A and varscanned was ' ,variables_scanned, ' a is ', a)
            scanner += 1
            if scanner < len(string):
                reader = string[scanner]
            else:
                scanner, reader = 100,' '
            while reader != ' ':
                b = b + reader
                scanner += 1
                if scanner < len(string):
                    reader = string[scanner]
                else:
                    break
            variables_scanned += 1
            #print('came in to B and varscanned was ' ,variables_scanned, ' b is ', b)
            scanner += 1
            if scanner < len(string):
                reader = string[scanner]
            else:
                scanner, reader = 100,' '
            while reader != ' ':
                c = c + reader
                scanner += 1
                if scanner < len(string):
                    reader = string[scanner]
                else:
                    break
            variables_scanned += 1
            #print('came in to c and varscanned was ' ,variables_scanned, ' c is ', c)
            scanner += 1
            if scanner < len(string):
                reader = string[scanner]
            else:
                scanner, reader = 100,' '
            while reader != ' ':
                d = d + reader
                scanner += 1
                if scanner < len(string):
                    reader = string[scanner]
                else:
                    break
            variables_scanned += 1
            #print('came in to D and varscanned was ' ,variables_scanned, ' d is ', d)
            scanner += 1
            if scanner < len(string):
                reader = string[scanner]
            else:
                scanner, reader = 100,' '
            while reader != ' ':
                e = e + reader
                scanner += 1
                if scanner < len(string):
                    reader = string[scanner]
                else:
                    break
            variables_scanned += 1
            #print('came in to E and varscanned was ' ,variables_scanned, ' e is ', e)
            scanner += 1
            if scanner < len(string):
                reader = string[scanner]
            else:
                scanner, reader = 100,' '
            while reader != ' ':
                f = f + reader
                scanner += 1
                if scanner < len(string):
                    reader = string[scanner]
                else:
                    break
            variables_scanned += 1
            #print('came in to F and varscanned was ' ,variables_scanned, ' f is ', f)
        scanner += 1
    return a, b, c, d, e, f
def calculate_vals(a,b,c,d,e,f,x):
    if f == '' and e == '' and d == '' and c == '' and b == '':
        a = float(a)
        x = float(x)
        val = a
    elif f == '' and e == '' and d == '' and c == '':
        a = float(a)
        b = float(b)
        x = float(x)
        val = (a * x) + b
    elif f == '' and e == '' and d == '':
        a = float(a)
        b = float(b)
        c = float(c)
        x = float(x)
        val = (a * (x * x)) + (b * x) + c
    elif f == '' and e == '':
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        x = float(x)
        val = (a * (x * x * x)) + (b * (x * x)) + (c * x) + d
    elif f == '':
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        e = float(e)
        x = float(x)
        val = (a * (x * x * x * x)) + (b * (x * x * x)) + (c * (x * x)) + (d * x) + e
    else:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        e = float(e)
        f = float(f)
        x = float(x)
        val = (a * (x * x * x * x * x)) + (b * (x * x * x * x)) + (c * (x * x * x)) + (d * (x * x)) + (e * x) + f
    return val
wholestring = input('enter all the coeficients, seperated by spaces:   ')
a, b, c, d, e, f = stringslicer(wholestring)
if f == '' and e == '' and d == '' and c == '' and b == '':
    print('You entered:   a = ', a)
    print('The equation detected was    y = ',a)
elif f == '' and e == '' and d == '' and c == '':
    print('You entered:   a = ', a, '    b = ', b)
    bsign = '+ ' if int(b) >= 0 else ''
    print('The equation detected was    y = ',a,'x ', bsign,b )
elif f == '' and e == '' and d == '':
    bsign = '+ ' if int(b) >= 0 else ''
    csign = '+ ' if int(c) >= 0 else ''
    print('The equation detected was    y = ',a,'x² ', bsign,b,'x ',csign,c )
    print('You entered:   a = ', a, '    b = ', b, '    c = ', c)
# ² ³ ⁴ ⁵ ⁶ ⁷ ⁸
elif f == '' and e == '':
    lastval = d
    bsign = '+ ' if int(b) >= 0 else ''
    csign = '+ ' if int(c) >= 0 else ''
    dsign = '+ ' if int(d) >= 0 else ''
    print('The equation detected was    y = ',a,'x³ ', bsign,b,'x² ',csign,c,'x ',dsign,d )
    print('You entered:   a = ', a, '    b = ', b, '    c = ', c, '    d = ', d)
elif f == '':
    lastval = e
    bsign = '+ ' if int(b) >= 0 else ''
    csign = '+ ' if int(c) >= 0 else ''
    dsign = '+ ' if int(d) >= 0 else ''
    esign = '+ ' if int(e) >= 0 else ''
    print('You entered:   a = ', a, '    b = ', b, '    c = ', c, '    d = ', d, '    e = ', e)
    print('The equation detected was    y = ',a,'x⁴ ',bsign,b,'x³ ',csign,c,'x² ',dsign,d,'x ',esign,e)
else:
    lastval = f
    bsign = '+ ' if int(b) >= 0 else ''
    csign = '+ ' if int(c) >= 0 else ''
    dsign = '+ ' if int(d) >= 0 else ''
    esign = '+ ' if int(e) >= 0 else ''
    fsign = '+ ' if int(f) >= 0 else ''
    print('You entered:   a = ', a, '    b = ', b, '    c = ', c, '    d = ', d, '    e = ', e, '    f = ', f)
    print('The equation detected was    y = ',a,'x⁵',bsign,b,'x⁴ ',csign,c,'x³ ',dsign,d,'x² ',esign,e,'x ',fsign,f)
print('x y table')
print('\n  x    y  ')
print('__________')
print('-10  | ', calculate_vals(a,b,c,d,e,f,-10))
print('-9   | ', calculate_vals(a,b,c,d,e,f,-9))
print('-8   | ', calculate_vals(a,b,c,d,e,f,-8))
print('-7   | ', calculate_vals(a,b,c,d,e,f,-7))
print('-6   | ', calculate_vals(a,b,c,d,e,f,-6))
print('-5   | ', calculate_vals(a,b,c,d,e,f,-5))
print('-4   | ', calculate_vals(a,b,c,d,e,f,-4))
print('-3   | ', calculate_vals(a,b,c,d,e,f,-3))
print('-2   | ', calculate_vals(a,b,c,d,e,f,-2))
print('-1   | ', calculate_vals(a,b,c,d,e,f,-1))
print('0    | ', calculate_vals(a,b,c,d,e,f, 0))
print('1    | ', calculate_vals(a,b,c,d,e,f, 1))
print('2    | ', calculate_vals(a,b,c,d,e,f, 2))
print('3    | ', calculate_vals(a,b,c,d,e,f, 3))
print('4    | ', calculate_vals(a,b,c,d,e,f, 4))
print('5    | ', calculate_vals(a,b,c,d,e,f, 5))
print('6    | ', calculate_vals(a,b,c,d,e,f, 6))
print('7    | ', calculate_vals(a,b,c,d,e,f, 7))
print('8    | ', calculate_vals(a,b,c,d,e,f, 8))
print('9    | ', calculate_vals(a,b,c,d,e,f, 9))
print('10   | ', calculate_vals(a,b,c,d,e,f, 10))
largest = max(calculate_vals(a,b,c,d,e,f,-10),calculate_vals(a,b,c,d,e,f,-9),calculate_vals(a,b,c,d,e,f,-8),calculate_vals(a,b,c,d,e,f,-7),calculate_vals(a,b,c,d,e,f,-6),calculate_vals(a,b,c,d,e,f,-5),calculate_vals(a,b,c,d,e,f,-4),calculate_vals(a,b,c,d,e,f,-3),calculate_vals(a,b,c,d,e,f,-2),calculate_vals(a,b,c,d,e,f,-1),calculate_vals(a,b,c,d,e,f,0),calculate_vals(a,b,c,d,e,f,1),calculate_vals(a,b,c,d,e,f,2),calculate_vals(a,b,c,d,e,f,3),calculate_vals(a,b,c,d,e,f,4),calculate_vals(a,b,c,d,e,f,5),calculate_vals(a,b,c,d,e,f,6),calculate_vals(a,b,c,d,e,f,7),calculate_vals(a,b,c,d,e,f,8),calculate_vals(a,b,c,d,e,f,9),calculate_vals(a,b,c,d,e,f,10))
least = min(calculate_vals(a,b,c,d,e,f,-10),calculate_vals(a,b,c,d,e,f,-9),calculate_vals(a,b,c,d,e,f,-8),calculate_vals(a,b,c,d,e,f,-7),calculate_vals(a,b,c,d,e,f,-6),calculate_vals(a,b,c,d,e,f,-5),calculate_vals(a,b,c,d,e,f,-4),calculate_vals(a,b,c,d,e,f,-3),calculate_vals(a,b,c,d,e,f,-2),calculate_vals(a,b,c,d,e,f,-1),calculate_vals(a,b,c,d,e,f,0),calculate_vals(a,b,c,d,e,f,1),calculate_vals(a,b,c,d,e,f,2),calculate_vals(a,b,c,d,e,f,3),calculate_vals(a,b,c,d,e,f,4),calculate_vals(a,b,c,d,e,f,5),calculate_vals(a,b,c,d,e,f,6),calculate_vals(a,b,c,d,e,f,7),calculate_vals(a,b,c,d,e,f,8),calculate_vals(a,b,c,d,e,f,9),calculate_vals(a,b,c,d,e,f,10))
least = -1 * least if least < 0 else least
largest = -1 * largest if largest < 0 else largest
mult = largest if largest >= least else least
#skipper = 10 if mult <= 10 else (50 if mult <= 50 else (100 if mult <= 100 else ( 150 if mult <= 150 else (200 if mult <= 200 else (300 if mult <= 300 else (400 if mult <= 400 else (500)))))))
skipper = mult
while str(int(skipper))[-1] != '0':
    skipper += 1
gap = skipper/10
print(gap)
import turtle
graphdrawer = turtle.Turtle()
graphdrawer.color("blue")
graphdrawer.pensize(3)
graphdrawer.speed(-1)
graphdrawer.left(90)
j = 0
while j <= 3:
    i = 1
    while i <= 10:
        graphdrawer.forward(20)
        graphdrawer.right(90)
        graphdrawer.forward(7)
        graphdrawer.left(90)
        if j != 3:
            graphdrawer.write(i*gap)
        graphdrawer.left(90)
        graphdrawer.forward(14)
        graphdrawer.left(90)
        if j == 3:
            graphdrawer.write(i*gap)
        graphdrawer.left(90)
        graphdrawer.forward(7)
        graphdrawer.left(90)
        i += 1
    graphdrawer.forward(20)
    graphdrawer.right(135)
    graphdrawer.forward(20)
    graphdrawer.right(180)
    graphdrawer.forward(20)
    graphdrawer.left(90)
    graphdrawer.forward(20)
    graphdrawer.right(180)
    graphdrawer.forward(20)
    graphdrawer.right(135)
    graphdrawer.forward(220)
    graphdrawer.right(90)
    j += 1
#each 20m segment is worth gap
gap = 20 / gap
pointdraw = turtle.Turtle()
pointdraw.turtlesize(0.56)
pointdraw.speed(10000)
pointdraw.shape("circle")
pointdraw.color("red")
pointdraw.pensize(4)
pointdraw.penup()
pointdraw.goto(0, gap * calculate_vals(a,b,c,d,e,f,0))
pointdraw.pendown()
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * 1, gap * calculate_vals(a,b,c,d,e,f,1))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * 2, gap * calculate_vals(a,b,c,d,e,f,2))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * 3, gap * calculate_vals(a,b,c,d,e,f,3))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * 4, gap * calculate_vals(a,b,c,d,e,f,4))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * 5, gap * calculate_vals(a,b,c,d,e,f,5))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * 6, gap * calculate_vals(a,b,c,d,e,f,6))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * 7, gap * calculate_vals(a,b,c,d,e,f,7))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * 8, gap * calculate_vals(a,b,c,d,e,f,8))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * 9, gap * calculate_vals(a,b,c,d,e,f,9))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * 10, gap * calculate_vals(a,b,c,d,e,f,10))
pointdraw.penup()
pointdraw.goto(0, gap * calculate_vals(a,b,c,d,e,f,0))
pointdraw.pendown()
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * -1, gap * calculate_vals(a,b,c,d,e,f,-1))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * -2, gap * calculate_vals(a,b,c,d,e,f,-2))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * -3, gap * calculate_vals(a,b,c,d,e,f,-3))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * -4, gap * calculate_vals(a,b,c,d,e,f,-4))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * -5, gap * calculate_vals(a,b,c,d,e,f,-5))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * -6, gap * calculate_vals(a,b,c,d,e,f,-6))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * -7, gap * calculate_vals(a,b,c,d,e,f,-7))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * -8, gap * calculate_vals(a,b,c,d,e,f,-8))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
input()
pointdraw.goto(gap * -9, gap * calculate_vals(a,b,c,d,e,f,-9))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")
pointdraw.goto(gap * -10, gap * calculate_vals(a,b,c,d,e,f,-10))
pointdraw.color("green")
pointdraw.stamp()
pointdraw.color("red")