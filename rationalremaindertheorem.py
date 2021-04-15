import time
a = input('enter a value   ')
b = input('enter b value   ')
c = input('enter c value   ')
d = input('enter d value (if aplicable, else leave blank)   ')
e = input('enter e value (if aplicable, else leave blank)   ')
f = input('enter f value (if aplicable, else leave blank)   ')
if f == '' and e == '' and 
def var_args(args):
    num = 0
    try:
        while True:
            hello = (args[num])
            num += 1
    except:
        print(' ')
    return num - 1
def factorfinder(number):
    number = int(number)
    if number < 0:
        number = number * -1
    factortry = 1
    factors = list(str(1))
    while factortry <= number:
        if number % factortry == 0:
            if factortry > 1:
                factors.append(str(factortry))
            else:
                factors = list(str(factortry))
        factortry += 1
    return (factors)
if a
afactors = factorfinder(a)
lastfactors = factorfinder(lastval)
afactornum = var_args(afactors)
lastfactornum = var_args(lastfactors)
univcounter = 0
numsinlist = 0
while univcounter <= afactornum:
    counter = 0
    while counter <= lastfactornum:
        onefactor = int(lastfactors[counter]) / int(afactors[univcounter])
        onefactor = round(onefactor,2)
        if univcounter == 0 and counter == 0:
            possible_factors = list(str(int(onefactor)))
            possible_factors.append(str(onefactor * -1))
            numsinlist += 2
        else:
            if str(onefactor) not in str(possible_factors):
                possible_factors.append(str(onefactor))
                possible_factors.append(str(onefactor * -1))
                numsinlist += 2
        counter += 1
    univcounter += 1
import math
def quadratic_formula(a,b,c):
    w = (str(a) + str(b) + str(c))
    w = w.lower()
    if a == '' or b == '' or c == '' :
        notentered, a, b, c = True, '1', '8', '15'
    if True:
        a = float(a)
        b = float(b)
        c = float(c)
        a, val1, val2, val3 = (99999 if a == 0 else a), (-1 * b), (-1 * b), ((b*b)-4*a*c)
        bsign, csign, astring, bstring, cstring, msquared, m = ('+ ' if b >= 0 else ' '), ('+ ' if c >= 0 else ' '), str(a), str(b), str(c), '㎡ ', 'm '
        astring, bstring, astring, msquared, bstring, bsign, m, cstring, csign = ('' if astring == '1' else astring), ('' if bstring == '1' else bstring), ('' if astring == '0' else astring), ('' if astring == '0' else msquared), ('' if bstring == '0' else bstring), ('' if bstring == '0' else bsign), ('' if bstring == '0' else m), ('' if cstring == '0' else cstring), ('' if cstring == '0' else csign)
        equation = astring + msquared + bsign + bstring + m + csign + cstring
        if val3 < 0:
            val3 = val3 * -1
            sqrtval, val1, = math.sqrt(val3), val1/(2*a)
            sqrtval = sqrtval/(2*a)
            roundval1 = round(val1,5)
            roundsqrtval = round(sqrtval,5)
            if val1 == 0:
                solutions = '+',roundsqrtval,'       -',roundsqrtval
            else:
                solutions = roundval1 , '+',roundsqrtval, 'i  ,  ', roundval1 , '-',roundsqrtval, 'i '
        else:
            val1 = val1 + math.sqrt(val3)
            val2 = val2 - math.sqrt(val3)
            val1 = round((val1 / (2*a)), 5)
            val2 = round((val2 / (2*a)), 5)
            solutions = ' ' + str(val1) if val1 == val2 else ' ' + str(val1) + ' ' + str(val2)
    return solutions
def synthetic_devision(a,b,c,d,e,f,possible_factors,numsinlist):
    foundfactors = ''
    foundornot = 'found'
    processingnum = 0
    while processingnum <= numsinlist - 1:
        processingval = float(possible_factors[processingnum])
        print('when you do synthetic devision on ',processingval)
        val1 = float(a)
        calculator = processingval * float(a)
        val2 = float(b) + calculator
        calculator = val2 * processingval
        val3 = float(c) + calculator
        calculator = val3 * processingval
        val4 = float(d) + calculator
        vallast = val4
        val5, val6 = '', ''
        if e != '':
            calculator = val4 * processingval
            val5 = float(e) + calculator
            vallast = val5
        if f != '':
            calculator = val5 * processingval
            val6 = float(f) + calculator
            vallast = val6
        if vallast == 0:
            foundfactors = str(processingval)
            break
        print('remainder is ',vallast)
        processingnum += 1
    if foundfactors == '':
        foundornot = 'not found'
    print(foundfactors, ' was found as a factor')
    return foundfactors, val1, val2, val3, val4, val5, val6, foundornot
print('\n\nStep 1:  Factorize the a coeficient')
print('     you get ', afactors)
print('\nStep 2:  Factorize the last coeficient of the polynomial')
print('     you get ', lastfactors)
print
finalfactors, val1, val2, val3, val4, val5, val6, foundornot = synthetic_devision(a,b,c,d,e,f,possible_factors, numsinlist)
finalfactors = str(finalfactors)
if val5 == '' and val6 == '':
    finalfactors = finalfactors + str(quadratic_formula(val1, val2, val3))
elif val6 == '':
    onefactor, val1, val2, val3, val4, val5, val6, foundornot = synthetic_devision(val1, val2, val3, val4, val5, val6, possible_factors, numsinlist)
    finalfactors = finalfactors + ' ' + str(onefactor) + str(quadratic_formula(val1, val2, val3))
else:
    onefactor, val1, val2, val3, val4, val5, val6, foundornot = synthetic_devision(val1, val2, val3, val4, val5, val6, possible_factors, numsinlist)
    finalfactors = finalfactors + ' ' + str(onefactor)
    onefactor, val1, val2, val3, val4, val5, val6, foundornot = synthetic_devision(val1, val2, val3, val4, val5, val6, possible_factors, numsinlist)
    finalfactors = finalfactors + ' ' + str(onefactor) + str(quadratic_formula(val1, val2, val3))
print('Possible factors are for A are: ', afactors)
print('Possible factors are for last coeficient are: ', lastfactors)
print('Possible factors are : ', possible_factors)
if 'not found' in foundornot:
    finalfactors == 'This polynomial could not be factorized'
    print('This polynomial could not be factorized')
else:
    print('After doing synthetic devision, the confirmed factors of this polynomial are below:\n',finalfactors)
