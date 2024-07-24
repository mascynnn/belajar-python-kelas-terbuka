# string width and alignment

# data 
data_nama = "makhasin"
data_umur = 19
data_tinggi = 170
data_nomor_sepatu = 34

# string standar
data_makhasin = f"nama = {data_nama}, umur = {data_umur}, tinggi badan = {data_tinggi}, nomor sepatu = {data_nomor_sepatu}"
print(5*"=" + "STRING STANDAR" + 5*"=")
print(data_makhasin)

# string multiline dengan enter, newline (\n)
data_makhasin = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi badan = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu}"
print(5*"=" + "STRING MULTILINE DENGAN ENTER" + 5*"=")
print(data_makhasin)

# string multiline kutip triplets ("""...""")
data_makhasin = f"""
nama         = {data_nama}, 
umur         = {data_umur}, 
tinggi badan = {data_tinggi}, 
nomor sepatu = {data_nomor_sepatu}
"""

print(5*"=" + "STRING MULTILINE KUTIP TRIPLETS" + 5*"=")
print(data_makhasin)

# string multiline (mengatur lebar)
data_makhasin = f"""
nama         = {data_nama:>10} 
umur         = {data_umur:>10} 
tinggi badan = {data_tinggi:>10} 
nomor sepatu = {data_nomor_sepatu:>10}
"""

print(5*"=" + "STRING MULTILINE MENGATUR LEBAR" + 5*"=")
print(data_makhasin)
