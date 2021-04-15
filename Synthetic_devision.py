def synthetic_devision(a,b,c,d,e,f,div):
    foundfactors = ''
    foundornot = 'found'
    processingnum = 0
    if True:
        processingval = float(div)
        val1 = float(a)
        calculator = processingval * float(a)
        val2 = float(b) + calculator
        calculator1 = val2 * processingval
        val3 = float(c) + calculator1
        calculator2 = val3 * processingval
        val4 = float(d) + calculator2
        vallast = val4
        val5, calculator3, calculator4, val6 = '', '', '', ''
        if e != '':
            calculator3 = val4 * processingval
            val5 = float(e) + calculator3
            vallast = val5
        if f != '':
            calculator4 = val5 * processingval
            val6 = float(f) + calculator4
            vallast = val6
        processingnum += 1
    return val1, val2, val3, val4, val5, val6, calculator, calculator1, calculator2, calculator3, calculator4
a = input('enter a value   ')
b = input('enter b value   ')
c = input('enter c value   ')
d = input('enter d value   ')
e = input('enter e value (if aplicable, else leave blank)   ')
f = input('enter f value (if aplicable, else leave blank)   ')
devisor = input('enter devisor')
val1, val2, val3, val4, val5, val6, calculator, calculator1, calculator2, calculator3, calculator4 = synthetic_devision(a,b,c,d,e,f,float(devisor))
print(devisor,'|  ',a,'  ',b,'  ',c,'  ',d,'  ',e,'  ',f)
print('-'* len(devisor),'|  ',calculator,'   ',calculator1,'   ',calculator2,'   ',calculator3,'   ',calculator4,'   ')
print(' '* len(devisor),'|  ',val1,'  ',val2,'  ',val3,'  ',val4,'  ',val5,'  ',val6,'  ')