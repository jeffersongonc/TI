print('#### Int ####')
x = 1
y = 35656222554887711
z = -3255522

print(x, type(x))
print(y, type(y))
print(z, type(z))

print('### Float ###')
x = 1.10
y = 1.0
z = -35.59

print(x, type(x))
print(y, type(y))
print(z, type(z))

print('## Complex ##')
x = 3+5j
y = 5j
z = -5j

print(x, type(x))
print(y, type(y))
print(z, type(z))

print('#### Conversions ####')

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(x, type(x))
print(float(x), type(float(x)))
print(complex(x), type(complex(x)))

print(y, type(y))
print(int(y), type(int(y)))
print(complex(y), type(complex(y)))

print(z, type(z))
print('Não pode converter complex')
#print(int(z), type(int(z)))
#print(float(z), type(float(z)))

print('#### Random ####')

import random as r

for i in range(10):
    print(r.randrange(1, 100))