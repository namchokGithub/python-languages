# Python Operators
# https://www.w3schools.com/python/python_operators.asp

print("=== Python Arithmetic Operators ===")

# print(1+2)
# print(1+-2)
# print(1-2)
# print(1-+3)
# print(2*3)
# print(1/5)
# print(2%3)
# print(2**2)
# print(12//5)

print("=== Python Assignment Operators ===")

# x=4
# x+=3
# x-=3
# x*=4
# x/=2
# x%=1
# x//=2
# x**=2

# x=10
# x&=2
# x|=5

x=5
# x^=2
x>>=3
x<<=3

# print(x)

print("=== Python Comparison Operators ===")

if 2==3: 
    print(True)
if 2!=3: 
    print(True)
if 2>3: 
    print(True)
if 2<3: 
    print(True)
if 2>=3: 
    print(True)
if 2<=3: 
    print(True)

print("=== Python Logical Operators ===")

if 2==3 and 3==3:
    print(True)

if 2==3 or 3==3:
    print(True)

if not(2==3 and 3==3):
    print(True)

print("=== Python Identity Operators ===")

x = ['van', 'bmw']
y = ['van', 'bmw']
z = x
print(x is z) # returns True because z is the same object as x
print(x is y) # returns False because x is not the same object as y, even if they have the same content
print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print("=== Python Membership Operators ===")

x = ['van', 'bmw']
print('banana' in x)
print('van' in x)
print('banana' not in x)