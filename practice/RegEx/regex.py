# Python RegEx
# https://www.w3schools.com/python/python_regex.asp

import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# # RegEx Functions
# # The findall() function returns a list containing all matches.
# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)

# txt = "The rain in Spain"
# x = re.findall("Portugal", txt)
# print(x)

# # The search() function searches the string for a match, 
# # and returns a Match object if there is a match.
# txt = "The rain in Spain"
# x = re.search("\s", txt)
# print("The first white-space character is located in position:", x.start())
# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)

# # The split() function returns a list where the string has been split at each match
# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)
# # You can control the number of occurrences by specifying the maxsplit parameter
# x = re.split("\s", txt, 1)
# print(x)

# # The sub() function replaces the matches with the text of your choice
# x = re.sub("\s", "9", txt)
# print(x)
# # You can control the number of replacements by specifying the count parameter
# x = re.sub("\s", "9", txt, 2)
# print(x)

# # []
# x = re.findall("[a-m]", txt)
# print(x)

# # Find all digit characters:
# txt = "That will be 59 dollars"
# x = re.findall("\d", txt)
# print(x)

# # Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
# txt = "hello world"
# x = re.findall("he..o", txt)
# print(x)

# # Starts with
# x = re.findall("^hello", txt)
# if x:
#   print("Yes, the string starts with 'hello'")
# else:
#   print("No match")

# # Check if the string ends with 'world':
# x = re.findall("world$", txt)
# if x:
#   print("Yes, the string ends with 'world'")
# else:
#   print("No match")

# # Check if the string contains "ai" followed by 0 or more "x" characters:
# # Zero or more occurrences
# txt = "The rain in Spain falls mainly in the plain!"
# x = re.findall("aix*", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# # Check if the string contains "ai" followed by 1 or more "x" characters:
# # One or more occurrences
# x = re.findall("aix+", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# # Check if the string contains "a" followed by exactly two "l" characters:
# # Exactly the specified number of occurrences
# x = re.findall("al{2}", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# # Check if the string contains either "falls" or "stays":
# # Either or
# x = re.findall("The|Yes|stays", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# #### Metacharacters
# txt = "The rain in Spain"
# # Check if the string starts with "The":
# # Returns a match if the specified characters are at the beginning of the string
# x = re.findall("\AThe", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")

# # Check if "ain" is present at the beginning of a WORD:
# # Returns a match where the specified characters are at the beginning or at the end of a word
# # (the "r" in the beginning is making sure that the string is being treated as a "raw string")
# x = re.findall(r"\bain", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# x = re.findall(r"ain\b", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# # Check if "ain" is present, but NOT at the beginning of a word:
# # Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# # (the "r" in the beginning is making sure that the string is being treated as a "raw string")
# x = re.findall(r"\Bain", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# # Check if the string contains any digits (numbers from 0-9):
# # Returns a match where the string contains digits (numbers from 0-9)
# x = re.findall("\d", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# # Return a match at every no-digit character:
# # Returns a match where the string DOES NOT contain digits
# x = re.findall("\D", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# # Returns a match where the string contains a white space character
# x = re.findall("\s", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# # Returns a match where the string DOES NOT contain a white space character
# x = re.findall("\S", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# # Returns a match where the string contains any word characters 
# # (characters from a to Z, digits from 0-9, and the underscore _ character)
# x = re.findall("\w", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# # Returns a match where the string DOES NOT contain any word characters
# # Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
# x = re.findall("\W", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# # Returns a match if the specified characters are at the end of the string
# # Check if the string ends with "Spain":
# x = re.findall("Spain\Z", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")

### Set
txt = "The rain in Spain"

# Returns a match where one of the specified characters (a, r, or n) are present
# Check if the string has any a, r, or n characters:
x = re.findall("[arn]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# Check if the string has any characters between a and n:
# Returns a match for any lower case character, alphabetically between a and n
x = re.findall("[a-n]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# Check if the string has other characters than a, r, or n:
# Returns a match for any character EXCEPT a, r, and n
x = re.findall("[^arn]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# Check if the string has any 0, 1, 2, or 3 digits:
# Returns a match where any of the specified digits (0, 1, 2, or 3) are present
x = re.findall("[0123]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

txt = "8 times. before 11:45 AM"

# Check if the string has any digits:
# Returns a match for any digit between 0 and 9
x = re.findall("[0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# Check if the string has any two-digit numbers, from 00 to 59:
# Returns a match for any two-digit numbers from 00 and 59
x = re.findall("[0-5][0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# Check if the string has any characters from a to z lower case, and A to Z upper case:
# Returns a match for any character alphabetically between a and z, lower case OR upper case
x = re.findall("[a-zA-Z]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# Check if the string has any + characters:
# In sets, +, *, ., |, (), $,{} has no special meaning, 
# so [+] means: return a match for any + character in the string
x = re.findall("[+.]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
