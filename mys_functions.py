def summary(a,b):
    y = a+b
    return y

#define the function: 'even or odd'
def evenOrOdd(number):
    remainder = number%2
    if remainder == 0:
        return 'even'
    else:
        return 'odd'

def sumEven(a,b,c):
    if evenOrOdd(a) == 'even' and evenOrOdd(b) == 'even':
        y = summary(a,b)
    elif evenOrOdd(b) == 'even' and evenOrOdd(c) == 'even':
        y = summary(b,c)
    elif evenOrOdd(a) == 'even' and evenOrOdd(c) == 'even':
        y = summary(c,a)
    else:
        y = 'no two even numbers'
    return y