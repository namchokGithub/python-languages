# Python Scope
# https://www.w3schools.com/python/python_scope.asp

# Local Scope
def myfunc():
    x = 300
    print(x)

myfunc()

# Fucntion Inside Function
def mufunc2():
    x = 300
    def myinnnerfunc():
        print(x)
    myinnnerfunc()

mufunc2()

# Global Scope
x = 120

def myfunc3():
    print(x)

myfunc3()
print(x)

# Naming Veriables
x = 199

def myfunc4():
    x = 111
    print(x)

myfunc4()
print(x)

# Global Keyword
y = 111

def myfunc5():
    global y 
    y = 300

myfunc5()

print(y)
