import time
start_time = time.time()
print("Hello world!!")
print("Hallo dunia!!")

# ini adalah comment dalam python
""" ini adalah comment
line dalam python"""

a = 10
print(a)
# kita bisa mengcompile file python
# agar lebih cepat ketika dijalankan
# caranya dengan mengetik
# python -m py_compile main.py (nama file)
print(time.time() - start_time, "detik")
