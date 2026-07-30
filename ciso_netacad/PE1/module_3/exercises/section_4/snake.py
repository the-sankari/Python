numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.
print("\nList length:", len(numbers))  # Printing the new value of the second element.
del numbers[3]  # Deleting the fourth element.
print("List contents after deleting the fourth element:", numbers)  # Printing list contents after deletion

my_list = []
for i in range(6):
    my_list.append(i + 1)  # Adding numbers 1 through 6 to the list.
print("\nList contents after adding numbers 1 through 6:", my_list)  # Printing list contents after adding numbers 1 through 6.

#####################
total = 0
for i in range(len(my_list)):
    total += my_list[i] # Adding each element of the list to the total.
print("Total:", total)  # Printing the total.