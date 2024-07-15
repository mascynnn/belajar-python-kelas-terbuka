# episode operator bitwise, operasi biner, binary

a = 10
b = 3

# bitwise OR (|)
print("\n====BITWISE OR '|'====")
c = a | b
print('nilai a ', a, 'binary = ', format(a, '08b'))
print('nilai b ', b, 'binary = ', format(b, '08b'))
print("--------------DI OR KAN '|'")
print('a | b = ', format(c, '08b'))

# bitwise AND (|)
print("\n====BITWISE AND '|'====")
c = a & b
print('nilai a ', a, 'binary = ', format(a, '08b'))
print('nilai b ', b, 'binary = ', format(b, '08b'))
print("--------------DI AND KAN '|'")
print('a & b = ', format(c, '08b'))

# bitwise XOR (|)
print("\n====BITWISE XOR '|'====")
c = a ^ b
print('nilai a ', a, 'binary = ', format(a, '08b'))
print('nilai b ', b, 'binary = ', format(b, '08b'))
print("--------------DI XOR KAN '|'")
print('a ^ b = ', format(c, '08b'))

# bitwise NOT (~)

print("\n====BITWISE NOT '~'====")
c = ~a
print('nilai a ', a, 'binary = ', format(a, '08b'))
print("--------------DI NOT KAN '~'")
print('~a = ', format(c, '08b'))

d = 0b00001010
e = 0b11111111
print('dinotkan dengan xor : ', format(d^e, '08b'))

# bitwise shift right >>
print("\n====BITWISE SHIFT RIGHT '>>'====")
c = a >> 2
print('nilai a ', a, 'binary = ', format(a, '08b'))
print('a >> 2 = ', format(c, '08b'))

# bitwise shift left <<
print("\n====BITWISE SHIFT LEFT '<<'====")
c = a << 2
print('nilai a ', a, 'binary = ', format(a, '08b'))
print('a << 2= ', format(c, '08b'))
