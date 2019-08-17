
def calculate(number):
    if (number == 0):
        return str(number)
    elif (number % 15 == 0):
        return 'fizzbuzz'
    elif (number % 3 == 0):
        return 'fizz'
    elif (number % 5 == 0):
        return 'buzz'
    return str(number)