# episode latihan logika dan komparasi


# membuat gabungan area rentang dari angka

# ++++3-----10++++
# kasus gabungan
inputUser = float(input("masukan angak yang bernilai kurang sari 3 atau lebih dari 10 : "))

# ++++3----
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari 3", isKurangDari)

# ----10++++
# memeriksa angak lebih dari 10
isLebihdari = (inputUser > 10)
print("lebih dari 10 =", isLebihdari)

# +++++3-----10+++++
isCorrect = isKurangDari or isLebihdari
print("angka yang anda masukkan : ", isCorrect)

# -----3+++++10-----
# kasus irisan
inputUser = float(input("\nmasukkan angak yang bernilai lebih dari 3 dan kurang dari 10 : "))

# ----3++++
isLebihDari = (inputUser > 3)
print("lebih dari 3 : ", isLebihDari)

# ++++10----
isKurangDari = (inputUser < 10)
print("kurang dari 10 : ", isKurangDari)

# ----3++++10----
isCorrect =isLebihDari and isKurangDari
print("angka yang anda masukkan : ", isCorrect)
