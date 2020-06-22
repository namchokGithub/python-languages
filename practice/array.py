# Python Array
# https://www.w3schools.com/python/python_arrays.asp

cars = ['Ford', 'Volvo', "BMW"]

# Get value
print(cars[1])

# Modify value
cars[0] = "Toyota"

# Get langth
print(len(cars))

# Looping Array
for x in cars:
    print(x)

# Adding Array
cars.append('Honda')

# Removing
cars.pop(1)
cars.remove('Honda')

for x in cars:
    print(x)
