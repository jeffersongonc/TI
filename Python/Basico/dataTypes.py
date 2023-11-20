print('##################')
print('Var: str')
x = "Hello World"
y = str("Hello World")
print(x, type(x))
print(y, type(y))
print('##################')

print('##################')
print('Var: int')
x = 20
y = int(20)
print(x, type(x))
print(y, type(y))
print('##################')

print('##################')
print('Var: float')
x = 20.5
y = float(20.5)
print(x, type(x))
print(y, type(y))
print('##################')

print('##################')
print('Var: complex')
x = 1j
y = complex(1j)
print(x, type(x))
print(y, type(y))
print('##################')

print('##################')
print('Var: list')
x = ["apple", "banana", "cherry"]
y = list(("apple", "banana", "cherry"))
print(x, type(x))
print(y, type(y))
print('##################')

print('##################')
print('Var: tuple')
x = ("apple", "banana", "cherry")
y = tuple(("apple", "banana", "cherry"))
print(x, type(x))
print(y, type(y))
print('##################')

print('##################')
print('Var: range')
x = range(6)
y = x
print(x, type(x))
print(y, type(y))
print('##################')

print('##################')
print('Var: dict')
x = {"name" : "John", "age" : 36}
y = dict(name="John", age=36)
print(x, type(x))
print(y, type(y))
print('##################')

print('##################')
print('Var: set')
x = {"apple", "banana", "cherry"}
y = set(("apple", "banana", "cherry"))
print(x, type(x))
print(y, type(y))
print('##################')

print('##################')
print('Var: frozenset')
x = frozenset({"apple", "banana", "cherry"})
y = frozenset(("apple", "banana", "cherry"))
print(x, type(x))
print(y, type(y))
print('##################')

print('##################')
print('Var: bool')
x = True
y = bool(5)
print(x, type(x))
print(y, type(y))
print('##################')

print('##################')
print('Var: bytes')
x = b"Hello"
y = bytes(5)
print(x, type(x))
print(y, type(y))
print('##################')

print('##################')
print('Var: bytearray')
x = bytearray(5)
y = x
print(x, type(x))
print(y, type(y))
print('##################')

print('##################')
print('Var: memoryview')
x = memoryview(bytes(5))
y = x
print(x, type(x))
print(y, type(y))
print('##################')

print('##################')
print('Var: None')
x = None
print(x, type(x))
print(y, type(y))
print('##################')

