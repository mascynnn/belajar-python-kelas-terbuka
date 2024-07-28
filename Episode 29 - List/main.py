## list

list_number = [1,2,3,4,5]
print(list_number)

list_string =  ["makhasin", "muhammad", "mascynn"]
print(list_string)

list_boolean = [True, False, False, True]
print(list_boolean)

list_campuran = [1, "makhasin", True, 2, False]
print(list_campuran)

## advanced list
# dengan range
list_range = range(0,10,2) # (start, end, step)
print(list_range)
print(list(list_range))

# dengan for loop (list comprehention)
list_for = [i**2 for i in range(0,10)]
print(list_for)

# dengan for dan if
list_for_if = [i for i in range(0,10) if i != 5]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i %2 == 0]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i %2 != 0]
print(list_for_if)
