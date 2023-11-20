a = "Hello, World!"
print(a[1])

for i in a:
    print(i)

print(len(a))

if "wor".upper() in a.upper():
    print("Sim, 'Wor' está presente.")
else:
    print("Não, 'Wor' está presente.")

print(a[8:10])
print(a[:5])
print(a[3:])
print(a[-5:-2])

print(a.upper())
print(a.lower())
b = " Hello, World! "
print(b.strip())
print(a.replace('H','J'))
print(a.split(','))

c = 'Hello'
d = 'World'
print(c+d)
print(c + ' ' + d)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."

#https://www.w3schools.com/python/python_strings_methods.asp