numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]           # 3
# numbers[-1]          # 2
# numbers[3])           # 1
# numbers[:-1]         # [3,1,4,1,5,9]
# numbers[3:4]         # [1]
# 5 in numbers         # True
# 7 in numbers         # False
# "3" in numbers       # False
# numbers + [6, 5, 3]  # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Modifying the list
numbers[0] = "ten"
numbers[-1] = 1  # using -1 instead of 6

# Printing the modified list
print(numbers[1:6])

# Checking for the existence of an element in the list
print(9 in numbers)
