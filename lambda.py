# Python Lambda
# https://www.w3schools.com/python/python_lambda.asp


# A lambda function is small anonymous funciton.
# A lambda function can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print(x(5))

xx = lambda a, b : a * b
print(xx(2, 1))

xxx = lambda a, b, c : a + b + c
print(xxx(5, 6, 7))

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(5))