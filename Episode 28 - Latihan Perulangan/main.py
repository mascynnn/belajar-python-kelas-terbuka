import os
# looping exercise making triangle

# 1. using for loop
os.system("cls")
input_rows = int(input("How many row of triangle??\nAnswer:"))
print("\n")

rows = 1
# dummy variable
for i in range(input_rows):
    print("*" * rows)
    rows += 1
print(f"{input_rows} rows triangles have been created with for loop!!\n")

# 2. using while loop
rows = 1
while True:
    print("*" * rows)
    rows += 1

    if rows > input_rows:
        break
print(f"{input_rows} rows triangles have been created with while loop!!\n")

# using while loop to print odd numbers
rows = 1
while True:
    if (rows % 2):
        print("*" * rows)
        rows += 1
    else:
        rows += 1
        continue

    if rows > input_rows:
        break

odd_triangles = (input_rows // 2) + 1
print(f"{odd_triangles} triangles with rows of odd numbers from 0 to {input_rows} have been created with while loop!!\n")

# using while loop to print equilateral triangles
rows = 1
spasi = input_rows // 2
while True:
    if (rows % 2):
        print(" " * spasi, "*" * rows)
        spasi -= 1
        rows += 1
    else:
        rows += 1
        continue

    if rows > int(input_rows):
        break
odd_triangles = (input_rows // 2) + 1
print(f"{odd_triangles} equilateral triangles with rows of odd numbers from 0 to {input_rows} have been created with while loop!!\n")
