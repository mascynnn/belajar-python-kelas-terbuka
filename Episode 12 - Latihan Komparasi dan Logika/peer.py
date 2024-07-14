# PR
# 1). -----0+++++5-----8++++11----
# 2). +++++0-----5+++++8----11++++

# 1). -----0+++++5-----8++++11----
inputUser = float(input("Masukkan bilangan\n'lebih besar dari 0 dan lebih kecil dari 5' atau\n'lebih besar dari 8 dan lebih kecil dari 11' : "))
print("\nangka ", inputUser)

# --0+++5--
and0_5 = ((inputUser > 0) and (inputUser < 5))
print("lebih besar dari 0 dan lebih kecil dari 5 : ", and0_5)

# --8++11--
and8_11 = ((inputUser > 8) and (inputUser < 11))
print("lebih besar dari 8 dan lebih kecil dari 11 : ", and8_11)

# -----0+++++5-----8++++11----
result_1 = and0_5 or and8_11
print("\nHASIL DARI ANGKA ANDA : ", result_1)



# 2). +++++0-----5+++++8----11++++
inputUser = float(input("\nMasukkan bilangan\n'lebih kecil dari 0 ' atau\n'lebih besar dari 5 dan lebih kecil dari 8' atau\n'lebih besar dari 11' : "))
print("\nangka ", inputUser)

# +++0
smaller_0 = inputUser < 0
print("lebih kecil dari 0 : ", smaller_0)

# 5+++8
and5_8 = ((inputUser > 5) and (inputUser < 8))
print("lebih besar dari 5 dan lebih kecil dari 8 : ", and5_8)

# 11++++
bigger_11 = inputUser > 11
print("lebih besar dari 11 : ",bigger_11)

# +++++0-----5+++++8----11++++
result_2 = smaller_0 or and5_8 or bigger_11
print("\nHASIL DARI ANGKA ANDA : ", result_2)
