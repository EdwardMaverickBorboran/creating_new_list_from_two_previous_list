# Create a program that will --

# Create a new list from two list using the following condition

# Given two list of numbers, write a program to create a new list such that the new list- 
# should contain odd numbers from the first list and even numbers from the second list.

# DEADLINE: JANUARY 26, 2024

# pseudocode

# Given:
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# Expected results:
# result list: [25, 35, 40, 60, 90]

# 2 given list of numbers
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# Creating an empty list
results_list = []

# Iterating the first list
for number in list1:
    if number % 2 != 0:
        results_list.append(number)

# Iterating the first list
for number in list2:
    if number % 2 == 0:
        results_list.append(number)

print("Here is the new results:", results_list)




