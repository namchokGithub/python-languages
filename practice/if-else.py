# Python If ... Else
# https://www.w3schools.com/python/python_conditions.asp

print("=== Elif ===")

a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are aqual")

print("=== Else ===")

a = 300
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("=== a is greater than b")

print("=== Short Hand if ===")

# If you have only one statement to execute, you can put it on the same line as the if statement
if a > b: print("a is greater than b")

print("=== Short hand if else ===")

# Put it all on the same line
print("A") if a < b else print("B")

# you can also have multiple else statements on the same line.
print("A") if a > b else print("=") if a == b else print("B")
