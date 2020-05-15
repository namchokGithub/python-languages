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
