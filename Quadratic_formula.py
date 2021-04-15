import math
while True :
    notentered, wordinabc, val1, val2, val3 = False, False, 0, 0, 0
    print('\n' * 50)
    a = input('please enter a ')
    print('\n' * 50), print('a = ',a)
    b = input('please enter b ')
    print('\n' * 50), print('a = ',a,'     b = ',b)
    c = input('please enter c ')
    w = (str(a) + str(b) + str(c))
    w = w.lower()
    if a == '' or b == '' or c == '' :
        notentered, a, b, c = True, '1', '8', '15'
    try:
        a, b, c = (float(a) if '.' in a else int(a)), (float(b) if '.' in b else int(b)), (float(c) if '.' in c else int(c))
        a, val1, val2, val3 = (99999 if a == 0 else a), (-1 * b), (-1 * b), ((b*b)-4*a*c)
        bsign, csign, astring, bstring, cstring, msquared, m = ('+ ' if b >= 0 else ' '), ('+ ' if c >= 0 else ' '), str(a), str(b), str(c), 'x² ', 'x '
        astring, bstring, astring, msquared, bstring, bsign, m, cstring, csign = ('' if astring == '1' else astring), ('' if bstring == '1' else bstring), ('' if astring == '0' else astring), ('' if astring == '0' else msquared), ('' if bstring == '0' else bstring), ('' if bstring == '0' else bsign), ('' if bstring == '0' else m), ('' if cstring == '0' else cstring), ('' if cstring == '0' else csign)
        equation = astring + msquared + bsign + bstring + m + csign + cstring
        print('\n' * 50)
        print('You entered: a =',a,'  b =',b,'  c =',c)
        print('\nThe equation detected is' , equation)
        print('\nThe solution(s) are')
        if val3 < 0:
            val3 = val3 * -1
            print ('         ____\n' , val1,' ±i √', val3 , '\n-------------------\n' ,'     ',       2*a )
            sqrtval, val1, = math.sqrt(val3), val1/(2*a)
            sqrtval = sqrtval/(2*a)
            print('\nFurthur simplified to:\n')
            roundval1 = round(val1,5)
            roundsqrtval = round(sqrtval,5)
            if val1 == 0:
                print('+',roundsqrtval,'i   ,     -',roundsqrtval,'i')
            else:
                print(roundval1 , '+',roundsqrtval, 'i  ,  ', roundval1 , '-',roundsqrtval, 'i ')
        else:
            val1 = val1 + math.sqrt(val3)
            val2 = val2 - math.sqrt(val3)
            val1 = (val1 / (2*a))
            val2 = (val2 / (2*a))
            print(val1 if val1 == val2 else val1, val2)
    except:
           wordinabc, a, b, c = True, '1', '8', '15'
    if a == 99999:
        print('\n' * 50)
        print('The equation you have entered is not quadratic and cannot be solved by the Quadratic formula')
    if notentered == True:
        print('\n' * 50)
        print('Please enter all values')
    if wordinabc == True:
        print('\n' * 50)
        print('Please enter numbers')
    input('\nPress enter to continue') 
    