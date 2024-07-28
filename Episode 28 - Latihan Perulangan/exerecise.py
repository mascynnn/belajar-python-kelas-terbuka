# exrcise making a diamond
input_rows = int(input("how many rows??\nAnswer:"))

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

    if rows > input_rows:
        break

while True:
    if (rows % 2):
        spasi += 1
        print(" " * spasi,"*" *  rows)
        rows -= 1
    else:
        rows -= 1
        continue
    
    if rows < 1:
        break
