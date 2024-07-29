# deep copy nested list

a = [1,2]
b = [3,4]

data_list = [a,b, 9]
data_list_copy = data_list.copy()
print(f"data list = {data_list}")
print(f"data list copy = {data_list_copy}")

# mengambil data

data = data_list[1][1]
print(data)

# addres list
print(f"addres data list = {hex(id(data_list))}")
print(f"addres data list copy = {hex(id(data_list_copy))}")

# addres dari member
print(f"addres member data list[0][0] = {hex(id(data_list[0][0]))}")
print(f"addres member data list copy[0][0] = {hex(id(data_list_copy[0][0]))}")

data_list[0][1] = 5
data_list[2] = 10
print(f"data list = {data_list}")
print(f"data list copy = {data_list_copy}")

# menggunakan deep copy
from copy import deepcopy

data_list = [a,b,9]
data_deepcopy = deepcopy(data_list)

print(f"addres data list = {hex(id(data_list))}")
print(f"addres data deepcopy = {hex(id(data_deepcopy))}")

print(f"addres member data list[0] = {hex(id(data_list[0]))}")
print(f"addres member data deep copy[0] = {hex(id(data_deepcopy[0]))}")

data_list[0][1] = 30
print(f"data list = {data_list}")
print(f"data list copy = {data_list_copy}")
print(f"data deepcopy = {data_deepcopy}")
