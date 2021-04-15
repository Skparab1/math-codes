import time
import math
#superscripts! ² ³ ⁴ ⁵ ⁶ ⁷ ⁸
isquadratic = False
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
                solutions = str('   ' + str(roundsqrtval) + 'i  ' + '  -' + str(roundsqrtval) + 'i    ')
            else:
                solutions = str(roundval1) + ' + ' + str(roundsqrtval) + 'i  ,  ' + str(roundval1) + ' - ' + str(roundsqrtval) + 'i '
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
        processingnum += 1
    if foundfactors == '':
        foundornot = 'not found'
    return foundfactors, val1, val2, val3, val4, val5, val6, foundornot
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
wholestring = input('enter all the coeficients, seperated by spaces:   ')
a, b, c, d, e, f = stringslicer(wholestring)
print('\n'*50)
#print('a<',a,'>   b<',b,'>  c<',c,'>  d<',d,'>  e<',e,'>   f<',f,'>')
'''print('scanning inputs',end = ''), time.sleep(0.04), print('.',end = ''), time.sleep(0.04), print('.',end = ''), time.sleep(0.04), print('.'), time.sleep(0.04)
print('extracting variables',end = ''), time.sleep(0.04), print('.',end = ''), time.sleep(0.04), print('.',end = ''), time.sleep(0.04), print('.'), time.sleep(0.04)
print('factoring variables',end = ''), time.sleep(0.04), print('.',end = ''), time.sleep(0.04), print('.',end = ''), time.sleep(0.04), print('.'), time.sleep(0.04)
print('dividing factors',end = ''), time.sleep(0.04), print('.',end = ''), time.sleep(0.04), print('.',end = ''), time.sleep(0.04), print('.'), time.sleep(0.04)
print('doing synthetic division',end = ''), time.sleep(0.04), print('.',end = ''), time.sleep(0.04), print('.',end = ''), time.sleep(0.04), print('.'), time.sleep(0.04)
print('evaluating using quadratic formula',end = ''), time.sleep(0.04), print('.',end = ''), time.sleep(0.04), print('.',end = ''), time.sleep(0.04), print('.'), time.sleep(0.04)'''
if f == '' and e == '' and d == '' and c == '' and b == '':
    isquadratic = True
    print('You entered:   a = ', a)
    print('The equation detected was    y = ',a)
elif f == '' and e == '' and d == '' and c == '':
    isquadratic = True
    print('You entered:   a = ', a, '    b = ', b)
    bsign = '+ ' if int(float(b)) >= 0 else ''
    print('The equation detected was    y = ',a,'x ', bsign,b )
elif f == '' and e == '' and d == '':
    bsign = '+ ' if int(float(b)) >= 0 else ''
    csign = '+ ' if int(float(c)) >= 0 else ''
    isquadratic = True
    print('The equation detected was    y = ',a,'x² ', bsign,b,'x ',csign,c )
    print('You entered:   a = ', a, '    b = ', b, '    c = ', c)
# ² ³ ⁴ ⁵ ⁶ ⁷ ⁸
elif f == '' and e == '':
    lastval = d
    bsign = '+ ' if int(float(b)) >= 0 else ''
    csign = '+ ' if int(float(c)) >= 0 else ''
    dsign = '+ ' if int(float(d)) >= 0 else ''
    print('The equation detected was    y = ',a,'x³ ', bsign,b,'x² ',csign,c,'x ',dsign,d )
    print('You entered:   a = ', a, '    b = ', b, '    c = ', c, '    d = ', d)
elif f == '':
    lastval = e
    bsign = '+ ' if int(float(b)) >= 0 else ''
    csign = '+ ' if int(float(c)) >= 0 else ''
    dsign = '+ ' if int(float(d)) >= 0 else ''
    esign = '+ ' if int(float(e)) >= 0 else ''
    print('You entered:   a = ', a, '    b = ', b, '    c = ', c, '    d = ', d, '    e = ', e)
    print('The equation detected was    y = ',a,'x⁴ ',bsign,b,'x³ ',csign,c,'x² ',dsign,d,'x ',esign,e)
else:
    lastval = f
    bsign = '+ ' if int(float(b)) >= 0 else ''
    csign = '+ ' if int(float(c)) >= 0 else ''
    dsign = '+ ' if int(float(d)) >= 0 else ''
    esign = '+ ' if int(float(e)) >= 0 else ''
    fsign = '+ ' if int(float(f)) >= 0 else ''
    print('You entered:   a = ', a, '    b = ', b, '    c = ', c, '    d = ', d, '    e = ', e, '    f = ', f)
    print('The equation detected was    y = ',a,'x⁵',bsign,b,'x⁴ ',csign,c,'x³ ',dsign,d,'x² ',esign,e,'x ',fsign,f)
#try:
if True:
    if isquadratic == False:
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
        print('\n\nStep 1:  Factorize the a coeficient')
        print('     you get ', afactors)
        print('\nStep 2:  Factorize the last coeficient of the polynomial')
        print('     you get ', lastfactors)
        print('\nStep 3:  Find the possible factors by dividing the factors of the last coeficient by the factors of a')
        print('     you get ', possible_factors)
        print('\nStep 4:  Do synthetic devision and find out which factor is divisible without remainder')
        finalfactors, val1, val2, val3, val4, val5, val6, foundornot = synthetic_devision(a,b,c,d,e,f,possible_factors, numsinlist)
        finalfactors = str(finalfactors)
        if 'not found' in foundornot:
            print('     we find that there are no factors that are devisible without remainder, so this polynomial is not factorable.')
        else:
            print('     we find that ', finalfactors, ' is a factor, and the coeficients remaining are ', val1,' ', val2,' ', val3,' ', val4,' ', val5,' ', val6)
            if val5 == '' and val6 == '':
                print('\nStep 5: Since we end up with a trinomial, we can use the quadratic formula')
                quadfactors = str(quadratic_formula(val1, val2, val3))
                print('     The quadratic formula gives us solutions ', quadfactors, ' and we had found factor ', finalfactors, 'using synthetic devision')
                finalfactors = finalfactors + ' ' + quadfactors
                print('\n\nThe factors of the polynomial are ', finalfactors)
            elif val6 == '':
                print('\nStep 5: Since we end up with a 4-term polynomial, we must use synthetic devision to find another factor')
                onefactor, val1, val2, val3, val4, val5, val6, foundornot = synthetic_devision(val1, val2, val3, val4, val5, val6, possible_factors, numsinlist)
                if 'not found' in foundornot:
                    print('     we find that there are no factors that are devisible without remainder, so the only factor of this polynomial is ', finalfactors)
                else:
                    print('     we find that ', onefactor, ' is another factor, and the coeficients remaining are ', val1,' ', val2,' ', val3,' ', val4,' ', val5,' ', val6)
                    print('\nStep 6: Now, since we end up with a trinomial, we can use the quadratic formula')
                    quadfactor = str(quadratic_formula(val1, val2, val3))
                    finalfactors = finalfactors + ' ' + str(onefactor) + quadfactor
                    print('     The quadratic formula gives us solutions ', quadfactor, ' and we had found factors ', finalfactors, ' and ', onefactor, ' using synthetic devision')
                    print('\n\nThe factors of the polynomial are ', finalfactors)
            else:
                print('\nStep 5: Since we end up with a 5-term polynomial, we must use synthetic devision to find another factor')
                onefactor, val1, val2, val3, val4, val5, val6, foundornot = synthetic_devision(val1, val2, val3, val4, val5, val6, possible_factors, numsinlist)
                if 'not found' in foundornot:
                   print('     we find that there are no factors that are divisible without remainder, so the only factor of this polynomial is ', finalfactors)
                else:
                    print('     we find that ', onefactor, ' is another factor, and the coeficients remaining are ', val1,' ', val2,' ', val3,' ', val4,' ', val5,' ', val6)
                    print('\nStep 6: Now, since we end up with a 4-term polynomial, we must use synthetic devision to find another factor')
                    twofactor, val1, val2, val3, val4, val5, val6, foundornot = synthetic_devision(val1, val2, val3, val4, val5, val6, possible_factors, numsinlist)
                    if 'not found' in foundornot:
                        print('     we find that there are no factors that are devisible without remainder, so the only factor of this polynomial is ', finalfactors)
                    else:
                        print('     we find that ', twofactor, ' is another factor, and the coeficients remaining are ', val1,' ', val2,' ', val3,' ', val4,' ', val5,' ', val6)
                        print('\nStep 7: Now, since we end up with a trinomial, we can use the quadratic formula')
                        quadfactor = str(quadratic_formula(val1, val2, val3))
                        print('     The quadratic formula gives us solutions ', quadfactor, ' and we had found factors ', finalfactors, ', ', onefactor, 'and ', twofactor, ' using synthetic devision')
                        finalfactors = finalfactors + ' ' + str(onefactor) + ' ' + str(twofactor) + quadfactor
                        print('\n\nThe factors of the polynomial are ', finalfactors)
    else:
        if b == '' and c == '':
            print('\n\nStep 1: Since you have entered an integer, this equation cannot be factored')
        else:
            if c != '':
                print('\n\nStep 1: Since this is a quadratic equation, we can use the quadratic formula to factor it')
                quadfactors = str(quadratic_formula(a,b,c))
                print('     The solutions given by the quadratic formula are ',quadfactors)
            else:
                print('\n\nStep 1: Since you have entered a linear equation, we must solve for the variable')
                a = float(a)
                b = float(b)
                negb = -1 * b
                factor = negb / a
                print('     The answer you get is ', factor)
#except:
#    print('Invalid inputs. please try again.')
    
    