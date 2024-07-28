# operasi list

data_angka = [3,5,7,8,2,7,9,2,7,9,7,9,0,2,5,0,2,4,5,7,8,3]
print(data_angka)

# count data

angka_2 = data_angka.count(2)
angka_7 = data_angka.count(7)
print(f"banyak angka 2 pada data adalah : {angka_2}")
print(f"banyak angka 7 pada data adalah : {angka_7}")

# ambil posisi data (index)
data_string = ["makhasin","muhammad","mascynn","asin"]
print(data_string)

index_asin = data_string.index("asin")
index_makhasin = data_string.index("makhasin")
print(f"index data asin adalah : {index_asin}")
print(f"index data makhasin adalah : {index_makhasin}")

# mengurutkan list
print(f"ini data angka sebelum diurutkan : {data_angka}")

data_angka.sort()
print(f"ini data angka setelah diurutkan : {data_angka}")

print(f"ini data string sebelum diurutkan : {data_string}")

data_string.sort()
print(f"ini data string setelah diurutkan : {data_string}")

# membalik data yang sudah diurutkan
data_angka.reverse()
print(f"ini data angka setelah dibalik : {data_angka}")
data_string.reverse()
print(f"ini data string setelah dibalik : {data_string}")
