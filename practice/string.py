# Python Strings
# https://www.w3schools.com/python/python_strings.asp

print("Hello")
print('Hello')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
cinsectetur adipiscing elit,
sed do eiusmod tempor imcididunt
ut labore et dolore magna aliqua."""

print(a)

# Strings are Arrays

a = "Hello, World!"
print(a[1])

# Slicing

b = "Hello, World!"
print(b[2:5])

# Negative Indexing
print(b[-5: -2])

# String Length
# The len() function returns the length of a string
print(len(a))

# String Methods
# The strip() method removes any whitespace from the beginning or the end
print(a.strip())

# The lower() method returns the string in lower case
print(a.lower())

# The upper() method returns the string in upper case
print(a.upper())

# The replace() method replaces a string with another string
print(a.replace("H", "K"))

# The split() method splits the string into substrings if it finds instances of the separator
print(a.split(","))

# Check String
txt = "The rain in Spain stays mainly in the plain"

x = "ain" in txt
print(x)

x = "ain" not in txt
print(x)

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

c = a + " " + b
print(c)

# String Format
age = 35
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.93
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))

# Escape Character
txt = "We are the so-called \"Vilings\" from the north"
print(txt)
txt = "We are the so-called \'Vilings\' from the north"
print(txt)
txt = "We are the so-called \\Vilings\\ from the north"
print(txt)
txt = "We are the so-called \nVilings\n from the north"
print(txt)
txt = "We are the so-called \rVilings\r from the north"
print(txt)
txt = "We are the so-called \tVilings\t from the north"
print(txt)
txt = "We are the so-called \bVilings\b from the north"
print(txt)
txt = "We are the so-called \fVilings\f from the north"
print(txt)
