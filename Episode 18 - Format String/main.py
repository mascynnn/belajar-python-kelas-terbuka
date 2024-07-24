# format string

# contoh generic
# string
nama = "makhasin"
format_str = f"halo {nama}"

print(format_str)

# boolean
boolean = True
format_str = f"nilai boolean = {boolean}"

print(format_str)

# angka
angka = 2005
format_str = f"angka biasa {angka}"

print(format_str)

# bilangan bulat
angka_bulat = 19
format_str = f"angka integer {angka_bulat:d}"

print(format_str)

# bilangan dengan ordo ribuan
angka_ribuan = 20000
format_str = f"ribuan {angka_ribuan:,}"

print(format_str)

# angka desimal
desimal = 2005.26291
format_str = f"desimal {desimal:.2f}"

print(format_str)

# menampilkan leading zero
leading_zero = 2005.2414
format_str = f"leading zero {leading_zero:010.2f}"
print(format_str)

# menampilkan tanda + plus atau - minus
angka_plus = 89.72379
angka_minus = -57
format_plus = f"angka plus {angka_plus:+.3f}"
format_minus = f"angka minus {angka_minus:+d}"

print(format_plus)
print(format_minus)

# format persentase
persentase = 0.450
format_str = f"persentase {persentase:.2%}"

print(format_str)

# melakukan operasi aritmatika dalam placeholder
harga = 5000
jumlah = 8

format_str = f"total harga Rp. {harga*jumlah:,}"
print(format_str)

# menampilkan angka lain (binary, octal, hexadesimal)
angka = 10
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hexadesimal = {hex(angka)}"

print("angka biasa = " + str(angka))
print(format_binary)
print(format_octal)
print(format_hex)
