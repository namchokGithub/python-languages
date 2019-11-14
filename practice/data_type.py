print('Text Type:	str')
print('Numeric Types:	int, float, complex')
print('จำนวนเชิงซ้อน (อังกฤษ : complex number)')
print('Sequence Types:	list, tuple, range')
print('Mapping Type:	dict')
print('Boolean Type:	bool')
print('Binary Types:	bytes, bytearray, memoryview \n\n')

# Setting the Data Type

x = 5
print(type(x))

x = "Hello World"
print(type(x))

x = 20
print(type(x))

x = 20.5
print(type(x))

x = 1j
print(x)
print(type(x))

x = ["apple", "banana", "cherry"]
print(x)
print(type(x))

x = ("apple", "banana", "cherry")
print(x)
print(type(x))

x = range(6)
print(x)
print(type(x))

x = {"name" : "John", "age" : 36}
print(x)
print(type(x))

x = {"apple", "banana", "cherry"}
print(x)
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

x = True
print(x)
print(type(x))

x = b"Hello"
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))

# Setting the Specific Data Type

x = str("Hello World")
print(x)
print(type(x))

x = int(20)
print(x)
print(type(x))

x = float(20.5)
print(x)
print(type(x))

x = complex(1j)
print(x)
print(type(x))

x = list(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = tuple(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = range(6)
print(x)
print(type(x))

x = dict(name="John", age=36)
print(x)
print(type(x))

x = set(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = frozenset(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = bool(5)
print(x)
print(type(x))

x = bytes(5)
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))