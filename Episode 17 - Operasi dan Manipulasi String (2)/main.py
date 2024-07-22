# operator dalam bentuk methods

## merubah case dari string
# merubah semua ke lower case
alay = "aKu KeCe AbieesZzzZZzzZzz"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

# pengecekan dengan isX method
3
# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay To Be Orkay"
cek_judul = judul.istitle() # hasil bool

print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith() <-- keren
cek_start = "makhasin muhammad".startswith("makhasin")
print("start = " + str(cek_start))

cek_end = "makhasin muhammad".endswith("muhammad")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm'.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split("ehm"))

## alokasi karakter rjust() ljust() center()

kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

tengah = "tengah".center(20, "*")
print("'" + tengah + "'")

# kebalikan dari diatas strip()
tengah = tengah.strip("*") # menghilangakan tanda "*"
print("'" + tengah + "'")

## capitalize() <-- Membuat karakter pertama di string menjadi uppercase
tes_capitalize = "ayam goreng enak"
cek_hasil = tes_capitalize.capitalize()
print(cek_hasil)

tes_capitalize = "AYAM GORENG ENAK"
cek_hasil = tes_capitalize.capitalize()
print(cek_hasil)


## casefold() <-- sama dengan lower() bedanya, casefold() mengkonversi karakter tidak umum menjadi lowercase karakter umum Contoh  : 'ß' (german) = menjadi 'ss'
tes_casefold = "außen IS AN GERMAN WORD"
cek_hasil = tes_casefold.casefold()
print(cek_hasil)

## swapcase() <-- Uppercase jadi lowercase dan kebalikannya
tes_swapcase = "Ayam Goreng Suharti"
cek_hasil = tes_swapcase.swapcase()
print(cek_hasil)

## expandtabs () <-- Mengatur lebar tab (\t)
tes_expandtabs = "Ayam\tGoreng\tSuharti"
cek_hasil = tes_expandtabs.expandtabs(25)
print(cek_hasil)
