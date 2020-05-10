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

