# manipulasi list

# index 
data_list = ["asin","mascyn","acin"]

# mmengambil data list
data_0 = data_list[0]
print(f"data pertama : {data_0}")

data_akhir = data_list[-1]
print(f"data terakhir : {data_akhir}")

# mengambil info jumlah data list
jumlah_data = len(data_list)
print(f"jumlah data list : {jumlah_data}")

## manipulasi data list
# menabahkan data sesuai posisi
print(f"data sebelum ditambah : {data_list}")

data_list.insert(1,"makhasin")
print(f"data setelah ditambah : {data_list}")

# menambahkan data di akhir
data_list.append("akha")
print(f"data setelah ditambah diakhir : {data_list}")

# menambah list dengan list
list_baru = ["hasyim","khasin"]
data_list.extend(list_baru)
print(f"data list ditambah dengan list : {data_list}")

# merubah data
data_list[3] = "acynn"
print(f"data index[3] diubah : {data_list}")

# meremove data
data_list.remove("asin")
print(f"data asin diremove : {data_list}")

# meremove data paling belakang
data_akhir = data_list.pop()
print(f"data terakhir diremove yaitu : {data_akhir} sehingga data sekarang :\n{data_list}")
