# operasi logika boolean

# not, or, and, xor

# NOT
print('\n======LOGIKA NOT======')
a = True
c = not a
print('data a = ', a)
print('di NOT kan pada variabel c')
print('data c = ', c)

# OR
print('\n======LOGIKA OR======')
a = False
b = False
c = a or b
print(a, ' OR ', b, '=', c)

a = False
b = True
c = a or b
print(a, ' OR ', b, '=', c)

a = True
b = True
c = a or b
print(a, ' OR ', b, '=', c)

# AND
print('\n======LOGIKA AND======')
a = False
b = False
c = a and b
print(a, ' AND ', b, '=', c)

a = False
b = True
c = a and b
print(a, ' AND ', b, '=', c)

a = True
b = True
c = a and b
print(a, ' AND ', b, '=', c)

# XOR
print('\n======LOGIKA XOR======')
a = False
b = False
c = a ^ b
print(a, ' XOR ', b, '=', c)

a = False
b = True
c = a ^ b
print(a, ' XOR ', b, '=', c)

a = True
b = True
c = a ^ b
print(a, ' XOR ', b, '=', c)
