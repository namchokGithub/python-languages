# Python Dictionaries
# https://www.w3schools.com/python/python_dictionaries.asp

# Example

thisdict = {
    "brand": "Ford"
    ,"model": "Mustang"
    ,"year": 1964
}

print(thisdict)

print("=== Accessing Items ===")

x = thisdict["model"]
print(x)
x = thisdict.get("brand")
print(x)

print("=== Change Values ===")

print(thisdict.get("year"))
thisdict["year"] = 1999
print(thisdict.get("year"))
