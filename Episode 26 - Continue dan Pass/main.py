# continue pas, and break

# pass -> berfungsi sebagai dummy tidak akan dieksekusi

# angka = 0

# while angka < 5:
#     angka += 1
#     if angka == 3:
#         pass # ini tidak akan dieksekusi
#     print(f"sekarang angka ke -> {angka}")

# continue

angka = 0

while angka < 5:
    angka += 1

    if angka == 3:
        print("skipp 3")
        continue

    print(f"angka sekarang -> {angka}")

print("finish")
