data = "ini adalah string"
print(data)
print(type(data))

# 1.cara membuat string

'''
    1.dengan menggunakan single quote
    2. menggunakan double quote
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# mmenggunakan tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'nt it?')

# backslash
print("C:\\user\\mascynn")

#tab
print("ucup\t\totong, semakin jauh")

# backspace
print("ucup \botong")

# newline
print("baris pertama. \nbaris kedua.") # LF -> line feed : unix, macos, linux
print("baris pertama. \rbaris kedua") # CR -> carriage return : commodore, acorn, lisp
print("baris pertama. \n\rbaris kedua") # CRLF -> carriage return line feed : windows

# 3. string literal atau raw
 
# hati hati
print('C:\new folder')

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
    Nama : Makhasin Muhammad
    NPM  : 2315061084
""")

print(r"""
    Nama  : Makhasin Muhammad
    NPM   : 2315061084
    'C:\new folder'
""")
