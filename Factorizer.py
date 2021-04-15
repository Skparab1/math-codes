def factorfinder(number):
    number = int(number)
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
num = input("enter the number")
print(factorfinder(num))