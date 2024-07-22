# operasi dan manipulasi string

# 1. menyambung string (concantenate)
nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah + "'"+ nama_akhir
print(nama_lengkap)

# menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string
d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

D = "D"
status = D in nama_lengkap
print("string " + D + " ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(10*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-10 : " + nama_lengkap[10])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0:3] : " + nama_lengkap[0:4])
print("index ke-[3:7] : " + nama_lengkap[3:7])
print("index ke-[2,4,6,8,10] : " + nama_lengkap[0:11:2])

# item paling kecil atau besar
print("nilai paling kecil dari " + nama_lengkap + " adalah = " + min(nama_lengkap))
print("nilai paling besar dari " + nama_lengkap + " adalah = " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah  "  + str(ascii_code))
data = 110
print("char dari 110 adalah : " + chr(data))

# operator dalam bentuk method

data = "otong surotong markotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " adalah = " + str(jumlah))
