# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5 # adalah assignment
print("\nnilai a = ", a)

# penambahan
a += 1 # artinya adalah a = a + 1
print("nilai a += 1, nilai a menjadi", a)

# pengurangan
a -= 1 # artinya adalah a = a - 1
print("nilai a -= 1, nilai a menjadi", a)

# perkalian
a *= 4 # artinya adalah a = a * 4
print("nilai a *= 4, nilai a menjadi", a)

# pembagian
a /= 2 # artinya adalah a = a / 2
print("nilai a /= 2, nilai a menjadi", a)


b = 10
print("\nnilai b = ", b)

# modulus 
b %= 3 # artinya adalah b = b % 3
print("nilai b %= 3, nilai b menjadi", b)

b = 10
print("nilai b = ", b)
# flooor division
b //= 3 # artinya adalah b = b // 3
print("nilai b //= 3, nilai b menjadi", b)

b = 10
print("nilai b = ", b)
b **= 3 # artinya adalah b = b **= 3
print("nilai b **= 3, nilai b menjadi", b)


# operasi bitwise

# OR
c = True
print("\nnilai c =", c)
c |= False
print("nilai c |= False =", "nilai c menjadi", c)
c = True
print("nnilai c =", c)
c |= True
print("nilai c |= False =", "nilai c menjadi", c)
c = False
print("nilai c =", c)
c |= False
print("nilai c |= False =", "nilai c menjadi", c)

# AND
c = True
print("\nnilai c =", c)
c &= False
print("nilai c &= False =", "nilai c menjadi", c)
c = True
print("nilai c =", c)
c &= True
print("nilai c &= False =", "nilai c menjadi", c)
c = False
print("nilai c =", c)
c &= False
print("nilai c &= False =", "nilai c menjadi", c)

# XOR
c = True
print("\nnilai c =", c)
c ^= False
print("nilai c ^= False =", "nilai c menjadi", c)
c = True
print("nilai c =", c)
c ^= True
print("nilai c ^= False =", "nilai c menjadi", c)
c = False
print("nilai c =", c)
c ^= False
print("nilai c ^= False =", "nilai c menjadi", c)

# SHIFT
d = 0b00001010
print("\nnilai d =", format(d, '08b'))
d >>= 2
print("nilai d >>= 2, nilai d menjadi", format(d, '08b'))
d <<= 1
print("nilai d <<= 1, nilai d menjadi", format(d, '08b'))
